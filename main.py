from exa_py import Exa
from cerebras.cloud.sdk import Cerebras

# Add your API keys here
EXA_API_KEY = ""
CEREBRAS_API_KEY = ""

client = Cerebras(api_key = CEREBRAS_API_KEY)
exa = Exa(api_key = EXA_API_KEY)

print("✅ Setup complete")

def search_web(query, num=5):
    """Search the web using Exa's auto search"""
    result = exa.search_and_contents(
      query,
      type = "auto",
      num_results = num,
      text={"max_characters": 1000}
    )
    return result.results

print("✅ Search function ready")

def ask_ai(prompt):
    """Get AI response from Cerebras"""
    chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="llama-4-scout-17b-16e-instruct",
      max_tokens = 600,
      temperature = 0.2
    )
    return chat_completion.choices[0].message.content

print("✅ AI function ready")

def research_topic(query):
    """Main research function that orchestrates the entire process"""
    print(f"🔍 Researching: {query}")

    # Search for sources
    results = search_web(query, 5)
    print(f"📊 Found {len(results)} sources")

    # Get content from sources
    sources = []
    for result in results:
        content = result.text
        title = result.title
        if content and len(content) > 200:
            sources.append({
                "title": title,
                "content": content
            })

    print(f"📄 Scraped {len(sources)} sources")

    if not sources:
        return {"summary": "No sources found", "insights": []}

    # Create context for AI analysis
    context = f"Research query: {query}\n\nSources:\n"
    for i, source in enumerate(sources[:4], 1):
        context += f"{i}. {source['title']}: {source['content'][:400]}...\n\n"
        # ^^ get rid of this to use API params!
        # best practices - https://www.anthropic.com/engineering/built-multi-agent-research-system

    # Ask AI to analyze and synthesize
    prompt = f"""{context}

Based on these sources, provide:
1. A comprehensive summary (2-3 sentences)
2. Three key insights as bullet points

Format your response exactly like this:
SUMMARY: [your summary here]

INSIGHTS:
- [insight 1]
- [insight 2]
- [insight 3]"""

    response = ask_ai(prompt)
    print("🧠 Analysis complete")

    return {"query": query, "sources": len(sources), "response": response}

print("✅ Research function ready")
