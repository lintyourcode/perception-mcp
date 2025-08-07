# Perception-MCP

A lightweight **Model Context Protocol (MCP)** server that lets you ask **any question about an image, audio, or video file** and returns an answer powered by state-of-the-art multimodal models served through [fal.ai](https://fal.ai/).

## Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/) ≥ 1.7
- A [fal.ai](https://fal.ai/) account & API key

## Installation

```bash
# Clone and install dependencies
$ git clone https://github.com/lintyourcode/perception-mcp.git
$ cd perception-mcp
$ poetry install --no-root
```

## Usage

Add Perception-MCP to Claude Desktop (v0.3.7+) by adding the following to your `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
    "perception-mcp": {
      "command": "fastmcp",
      "args": ["run", "perception-mcp", "serve"],
      "env": {
        "FAL_KEY": "<your-fal-key>"
      }
    }
  }
}
```
