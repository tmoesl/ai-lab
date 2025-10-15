# 🤖 Artificial Intelligence Lab

![Status](https://img.shields.io/badge/-Ongoing-F8B84F?style=flat&label=Project&labelColor=23555555)
![Languages](https://img.shields.io/github/languages/count/tmoesl/ai-lab?label=Languages)
![Top Language](https://img.shields.io/github/languages/top/tmoesl/ai-lab?color=white)

A comprehensive workspace for exploring and mastering AI development frameworks with hands-on examples and ready-to-use code snippets.

## Workspace Overview

This is a UV workspace containing multiple AI framework projects. Each project has isolated dependencies but shares a single virtual environment and lockfile for consistency.

### Workspace Structure
```
ai-lab/
├── pyproject.toml              # Workspace configuration
├── .venv/                      # Shared virtual environment
└── langchain_lab/              # LangChain project
    └── pyproject.toml          # LangChain dependencies
```

## Projects

### LangChain Lab
Master LangChain v0.3 with structured learning paths covering chat models, prompts, chains, and RAG systems. Perfect for building LLM applications from basics to advanced implementations.

📁 **[Explore LangChain Lab →](langchain_lab/)**


## Getting Started

> **Prerequisites:** Python 3.12.8+ and [uv](https://docs.astral.sh/uv/) package manager

Each project has complete setup instructions in its README:
- **LangChain Lab:** [Installation Guide →](langchain_lab/README.md)

## Workspace Reference

Common commands for working with the UV workspace:

```bash
# Install specific project
uv sync --package PROJECT_NAME

# Add dependency to specific project  
uv add --package PROJECT_NAME DEPENDENCY_NAME

# Activate environment
source .venv/bin/activate

# Run code (UV auto-detects workspace)
uv run python path/to/your/script.py
```

