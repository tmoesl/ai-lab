# ⛓️‍💥 LangChain Lab

![Status](https://img.shields.io/badge/-Ongoing-F8B84F?style=flat&label=Project&labelColor=23555555)

LangChain Lab is part of the AI Lab workspace for exploring and mastering LangChain, an open-source development framework for building LLM applications. It's based on LangChain v0.3 and covers:

- ✅ Chat Models and LLM integrations (20+ providers)
- ✅ Message types and structured communication
- ✅ Prompt templates and dynamic prompting
- ✅ Chains for complex workflows and composition
- ✅ Retrieval-Augmented Generation (RAG) systems (in-progress)
- ✅ Agents and Custom Tools (in-progress)

## Getting Started

**Prerequisites:** Python 3.12.8+ and [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
# 1. Clone Repository
git clone https://github.com/tmoesl/ai-lab
cd ai-lab

# 2. Install Dependencies
uv sync --package langchain-lab

# 3. Create Environment File
cp .env.example .env
```

### Configuration

Add your API keys to `.env`:

```env
# OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic (Claude)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Google (Gemini)
GOOGLE_API_KEY=your_google_api_key_here
```

### Run Examples

```bash
uv run python 1_chat_models/1_chat_model_basic.py
```


## Learning Path

Follow this sequence for optimal learning progression:

### 1. Chat Models
Learn LLM integration and provider setup with hands-on examples covering chat model basics, provider configurations, conversation handling, and history management across multiple LLM providers.

📁 Folder: [1_chat_models](1_chat_models)

### 2. Messages  
Understand structured communication patterns with LangChain's BaseMessage classes including SystemMessage, HumanMessage, AIMessage, and ToolMessage for cross-provider compatibility.

📁 Folder: [2_messages](2_messages)

### 3. Prompt Templates
Master dynamic prompt creation with few-shot learning examples and template composition techniques for building robust prompting strategies.

📁 Folder: [3_prompt_templates](3_prompt_templates)

### 4. Chains [LCEL]
Build complex workflows and applications combining prompts, LLMs, and output parsing. Includes basic chains, parallel execution, and branching logic.

📁 Folder: [4_chains](4_chains)


## Project Structure
```
langchain_lab/
├── 1_chat_models/          # Chat model implementations
├── 2_messages/             # Message types and utilities
├── 3_prompt_templates/     # Prompt template examples
├── 4_chains/               # Chain workflows and composition
├── 5_rag/                  # Retrieval augmented generation systems
├── 6_agents/               # Agents and custom tools
```

## Sources
- [LangChain Documentation](https://docs.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangSmith](https://smith.langchain.com/)
- [LangChain Crash Course](https://github.com/bhancockio/langchain-crash-course/tree/main)


## Disclaimer

This repository is provided solely for educational purposes. It does not claim ownership of, nor is it officially affiliated with, the original LangChain framework or its documentation. Content and structure are inspired by Brandon Hancock’s LangChain course.
