# Perception-MCP

A lightweight **Model Context Protocol (MCP)** server that lets you ask **any question about an image, audio, or video file** and returns an answer powered by state-of-the-art multimodal models served through [fal.ai](https://fal.ai/).

## Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/) ≥ 1.7
- A [fal.ai](https://fal.ai/) account & API key
- A [Perplexity](https://www.perplexity.ai/) account & API key

## Installation

```bash
git clone --recurse-submodules https://github.com/lintyourcode/perception-mcp.git
cd perception-mcp
cp mcp_agent.secrets_template.yaml mcp_agent.secrets.yaml
$EDITOR mcp_agent.secrets.yaml
```

## Usage

Add Perception-MCP to Claude Desktop (v0.3.7+) by adding the following to your `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
    "perception-mcp": {
      "command": "fastmcp",
      "args": ["run", "perception-mcp", "serve"]
    }
  }
}
```

## Tools

Perception-MCP provides the following tools:

- `query_image`: Answer a question about an image's contents
- `query_audio`: Answer a question about an audio file's contents
- `query_video`: Answer a question about a video's contents

## Development

### Running tests

```bash
uv run pytest -q
```
