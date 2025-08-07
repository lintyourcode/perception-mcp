import pytest
import perception_mcp as pm
from fastmcp import FastMCP


def test_serve_returns_server():
    server = pm.serve()
    assert isinstance(server, FastMCP)


@pytest.mark.asyncio
async def test_tools_registered():
    server = pm.serve()
    tool_dict = await server.get_tools()
    tool_names = set(tool_dict.keys())
    expected = {"query_image", "query_audio", "query_video"}
    assert expected.issubset(tool_names)


@pytest.mark.parametrize(
    "stub_fn",
    [pm.query_image, pm.query_audio, pm.query_video],
)
@pytest.mark.asyncio
async def test_tool_stubs_raise_not_implemented(stub_fn):
    with pytest.raises(NotImplementedError):
        await stub_fn.fn("/dev/null", "dummy question") 