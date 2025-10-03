# 🔍 Perplexity Clone - AI-Powered Research Assistant

A powerful research tool that combines web search with AI analysis to provide comprehensive insights on any topic. Built with Exa (web search) and Cerebras (ultra-fast LLM inference).

## ✨ Features

### Three Research Modes

1. **Basic Research** (`research_topic`)
   - Single-layer web search and AI synthesis
   - Fast and straightforward
   - Perfect for quick insights

2. **Deep Research** (`deeper_research_topic`)
   - Two-layer sequential research
   - AI-driven follow-up questions
   - Provides more comprehensive coverage

3. **Multi-Agent Research** (`anthropic_multiagent_research`) ⭐
   - Anthropic-inspired multi-agent orchestration
   - Parallel specialized subagents
   - Most comprehensive and intelligent approach
   - Automatically decomposes complex queries

## 🚀 Quick Start

### Prerequisites

- Python 3.13+ (or Python 3.8+)
- API Keys:
  - [Exa API Key](https://exa.ai) - For web search
  - [Cerebras API Key](https://cloud.cerebras.ai) - For AI analysis

### Installation

1. **Clone or download this repository**

2. **Install dependencies**
   ```bash
   pip install exa-py cerebras-cloud-sdk
   ```

3. **Add your API keys**
   
   Open `main.py` and add your keys on lines 5-6:
   ```python
   EXA_API_KEY = "your-exa-api-key-here"
   CEREBRAS_API_KEY = "your-cerebras-api-key-here"
   ```

4. **Run the demo**
   ```bash
   python main.py
   ```

## 📖 Usage

### Running the Default Demo

The script will automatically run a multi-agent research on "current climate change solutions" and display the results.

### Custom Research Queries

Open a Python REPL or modify `main.py`:

```python
# Basic research
result = research_topic("quantum computing applications")
print(result['response'])

# Deep research with follow-up
result = deeper_research_topic("space exploration news")
print(result['response'])

# Multi-agent research (recommended)
result = anthropic_multiagent_research("artificial intelligence safety")
print(result['synthesis'])
```

## 🏗️ How It Works

### Multi-Agent System Architecture

```
┌─────────────────────────────────────────┐
│         Lead Agent                       │
│  • Analyzes query                        │
│  • Decomposes into subtasks              │
│  • Delegates to specialized agents       │
└──────────────┬──────────────────────────┘
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
┌────────┐ ┌────────┐ ┌────────┐
│Agent 1 │ │Agent 2 │ │Agent 3 │
│Core/   │ │Recent  │ │Apps/   │
│Basics  │ │Trends  │ │Impact  │
└───┬────┘ └───┬────┘ └───┬────┘
    │          │          │
    └──────────┼──────────┘
               ▼
┌─────────────────────────────────────────┐
│         Lead Agent                       │
│  • Synthesizes parallel findings         │
│  • Identifies cross-cutting insights     │
│  • Produces final report                 │
└─────────────────────────────────────────┘
```

### Research Flow

1. **Search**: Exa API finds relevant sources using semantic search
2. **Extract**: Content is extracted and filtered (>200 characters)
3. **Analyze**: Cerebras Llama 4 Scout analyzes and synthesizes
4. **Present**: Structured insights with summary and key findings

## 🎯 Example Queries

Try these topics with the multi-agent system:

- `anthropic_multiagent_research('quantum computing commercial applications')`
- `anthropic_multiagent_research('artificial intelligence safety frameworks')`
- `anthropic_multiagent_research('renewable energy policy implementation')`
- `anthropic_multiagent_research('latest breakthroughs in cancer treatment')`
- `anthropic_multiagent_research('future of autonomous vehicles')`

## 🛠️ Configuration

### Adjust Research Parameters

**Number of sources:**
```python
results = search_web(query, num=10)  # Default is 5
```

**Content length:**
```python
text={"max_characters": 2000}  # Default is 1000
```

**AI Temperature:**
```python
temperature = 0.2  # Lower = more focused, Higher = more creative
```

**Max tokens:**
```python
max_tokens = 1000  # Default is 600
```

## 📊 Output Format

### Multi-Agent Research Output

```
🤖 Anthropic Multi-Agent Research: [query]
--------------------------------------------------
👨‍💼 LEAD AGENT: Planning and delegating...
  ✓ Subtasks defined and delegated

🔍 SUBAGENTS: Working in parallel...
  🤖 Subagent 1: Researching [topic] fundamentals principles
  🤖 Subagent 2: Researching [topic] latest developments
  🤖 Subagent 3: Researching [topic] applications real world
  📊 Combined: X sources from 3 agents

👨‍💼 LEAD AGENT: Synthesizing parallel findings...

==================================================
🎯 MULTI-AGENT RESEARCH COMPLETE
==================================================
EXECUTIVE SUMMARY:
[Comprehensive overview]

INTEGRATED FINDINGS:
• [Finding from fundamentals]
• [Finding from recent developments]
• [Finding from applications]
• [Cross-cutting insight]

RESEARCH QUALITY:
- Sources analyzed: X across 3 specialized agents
- Coverage: [Assessment]
```

## 🔑 API Keys

### Getting Your Keys

1. **Exa API**
   - Visit [exa.ai](https://exa.ai)
   - Sign up for an account
   - Generate API key from dashboard

2. **Cerebras Cloud SDK**
   - Visit [cloud.cerebras.ai](https://cloud.cerebras.ai)
   - Create account
   - Get API key from settings

### Security Note

⚠️ **Never commit API keys to version control!** 

Consider using environment variables:
```python
import os
EXA_API_KEY = os.getenv("EXA_API_KEY")
CEREBRAS_API_KEY = os.getenv("CEREBRAS_API_KEY")
```

## 🎓 Inspiration

This project implements concepts from:
- **Anthropic's Multi-Agent Research System** - Parallel agent orchestration
- **Perplexity.ai** - Combining search with AI synthesis
- **Modern AI Research Workflows** - Iterative deepening and specialization

## 🤝 Contributing

Feel free to:
- Add new research strategies
- Improve prompt engineering
- Enhance output formatting
- Add error handling and retry logic

## 📝 License

This is a demo project for educational purposes.

## 🐛 Troubleshooting

### Import errors
If you see `Import "cerebras.cloud.sdk" could not be resolved`:
1. Ensure packages are installed: `pip install exa-py cerebras-cloud-sdk`
2. Select the correct Python interpreter in your IDE
3. Restart your IDE or Python language server

### API errors
- Check that your API keys are valid and have credits
- Verify no extra spaces in the API key strings
- Check your internet connection

### No sources found
- Try broader search terms
- Check if Exa API is accessible in your region
- Increase the `num` parameter in `search_web()`

## 📚 Learn More

- [Exa API Documentation](https://docs.exa.ai)
- [Cerebras Cloud SDK](https://inference-docs.cerebras.ai/)
- [Anthropic Research Blog](https://www.anthropic.com/engineering)

---

**Happy Researching! 🚀**
