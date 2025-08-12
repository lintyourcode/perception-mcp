from fastmcp import FastMCP

from perception_mcp.analysis import query

mcp = FastMCP("Perception-MCP")


@mcp.tool
async def query_image(path: str, question: str) -> str:
    """Answer a question about an image's contents using state-of-the-art generative AI models.

    Args:
        path: Absolute local file path or URL pointing to an image.
        question: The question to ask about the contents of the image.

    Returns:
        The answer to the question.
    """
    analysis = await query(path, question)
    return analysis.answer


@mcp.tool
async def query_audio(path: str, question: str) -> str:
    """Answer a question about an audio file's contents using state-of-the-art generative AI models.

    Args:
        path: Absolute local file path or URL pointing to an audio file.
        question: The question to ask about the contents of the audio.

    Returns:
        The answer to the question.

    """
    analysis = await query(path, question)
    return analysis.answer


@mcp.tool
async def query_video(path: str, question: str) -> str:
    """Answer a question about a video's contents using state-of-the-art generative AI models.

    Args:
        path: Absolute local file path or URL pointing to a video.
        question: The question to ask about the contents of the video.

    Returns:
        The answer to the question.
    """
    analysis = await query(path, question)
    return analysis.answer


def serve() -> FastMCP:
    """Return the FastMCP server instance.

    This function is used by the `fastmcp run perception-mcp serve` command
    referenced in the README.
    """
    return mcp


__all__ = [
    "mcp",
    "serve",
]
