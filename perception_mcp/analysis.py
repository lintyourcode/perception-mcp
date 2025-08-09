import httplib2
import os

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm import RequestParams
from mcp_agent.workflows.llm.augmented_llm_anthropic import AnthropicAugmentedLLM
from pydantic import BaseModel

_SYSTEM_PROMPT = """You are an expert media analysis assistant. You are given a file and a question. You must answer the question about the file. The file will be an image, audio file or video.

1. Use ffprobe to analyze the file and get its metadata.
2. Find at least two different fal.ai models that can answer the user's question about the provided file, using the `search` tool. Research their capabilities and limitations.
3. Cross-reference the results from ffprobe and at least two fal.ai models. If the results are not consistent, ask additional models until the results are consistent. If the results are still not consistent, ask the user for additional information.
   - Sometimes AI models will hallucinate, so this step is critical to ensure accuracy.
4. Return the final answer. If you encountered any challenges, include them in the notes.

Models generally have input file size or media duration limits. You may need to reduce the quality of the file. Alternatively, split the file into multiple parts, analyze each part separately and then combine the results.

FFmpeg is installed on the system.
"""

_USER_PROMPT = "Question: {question}\n\nFile: {file}"

app = MCPApp(name="perception-mcp")


class Analysis(BaseModel):
    answer: str
    notes: str | None = None


async def query(path: str, question: str) -> Analysis:
    """Query the image, audio, or video with the given question.

    Args:
        path: Absolute path or URL to the image, audio, or video file.
        question: Question to ask about the file.

    Returns:
        Analysis of the file.
    """

    if not (path and question):
        raise ValueError("Path and question are required")

    # Ensure file exists
    if path.startswith("http"):
        http = httplib2.Http()
        response, _ = http.request(path, "HEAD")
        if response.status >= 400:
            raise ValueError(f"Failed to fetch file: {response.status}")
    elif not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    async with app.run() as mcp_app:
        agent = Agent(
            name="perception-agent",
            instruction=_SYSTEM_PROMPT,
            server_names=["fal-ai", "perplexity-mcp"],
        )
        async with agent:
            llm = await agent.attach_llm(AnthropicAugmentedLLM)
            result = await llm.generate_structured(
                message=_USER_PROMPT.format(question=question, file=path),
                response_model=Analysis,
                request_params=RequestParams(max_iterations=50),
            )
            if result.notes:
                mcp_app.logger.info(f"Debug notes: {result.notes}")
            return result
