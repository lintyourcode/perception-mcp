from fastmcp import FastMCP

mcp = FastMCP("Perception-MCP")


@mcp.tool
async def query_image(path: str, question: str) -> str:
    """Answer a question about an image.

    Args:
        path: A local file path or URL pointing to an image.
        question: The question to ask about the contents of the image.

    Returns:
        The answer to the question.

    Note:
        The implementation will be added in a future commit.
    """
    raise NotImplementedError("query_image tool not implemented yet.")


@mcp.tool
async def query_audio(path: str, question: str) -> str:
    """Answer a question about an audio clip.

    Args:
        path: A local file path or URL pointing to an audio file.
        question: The question to ask about the contents of the audio.

    Returns:
        The answer to the question.

    Note:
        The implementation will be added in a future commit.
    """
    raise NotImplementedError("query_audio tool not implemented yet.")


@mcp.tool
async def query_video(path: str, question: str) -> str:
    """Answer a question about a video.

    Args:
        path: A local file path or URL pointing to a video.
        question: The question to ask about the contents of the video.

    Returns:
        The answer to the question.

    Note:
        The implementation will be added in a future commit.
    """
    raise NotImplementedError("query_video tool not implemented yet.")


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
