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

def deeper_research_topic(query):
    """Two-layer research for better depth"""
    print(f"🔍 Researching: {query}")

    # Layer 1: Initial search
    results = search_web(query, 6)
    sources = []
    for result in results:
        if result.text and len(result.text) > 200:
            sources.append({"title": result.title, "content": result.text})

    print(f"Layer 1: Found {len(sources)} sources")

    if not sources:
        return {"summary": "No sources found", "insights": []}

    # Get initial analysis and identify follow-up topic
    context1 = f"Research query: {query}\n\nSources:\n"
    for i, source in enumerate(sources[:4], 1):
        context1 += f"{i}. {source['title']}: {source['content'][:300]}...\n\n"

    follow_up_prompt = f"""{context1}

Based on these sources, what's the most important follow-up question that would deepen our understanding of "{query}"?

Respond with just a specific search query (no explanation):"""

    follow_up_query = ask_ai(follow_up_prompt).strip().strip('"')

    # Layer 2: Follow-up search
    print(f"Layer 2: Investigating '{follow_up_query}'")
    follow_results = search_web(follow_up_query, 4)

    for result in follow_results:
        if result.text and len(result.text) > 200:
            sources.append({"title": f"[Follow-up] {result.title}", "content": result.text})

    print(f"Total sources: {len(sources)}")

    # Final synthesis
    all_context = f"Research query: {query}\nFollow-up: {follow_up_query}\n\nAll Sources:\n"
    for i, source in enumerate(sources[:7], 1):
        all_context += f"{i}. {source['title']}: {source['content'][:300]}...\n\n"

    final_prompt = f"""{all_context}

Provide a comprehensive analysis:

SUMMARY: [3-4 sentences covering key findings from both research layers]

INSIGHTS:
- [insight 1]
- [insight 2]
- [insight 3]
- [insight 4]

DEPTH GAINED: [1 sentence on how the follow-up search enhanced understanding]"""

    response = ask_ai(final_prompt)
    return {"query": query, "sources": len(sources), "response": response}

print("✅ Enhanced research function ready")

# Test the enhanced research system
result = deeper_research_topic("climate change solutions 2025")

# Display results
print("\n" + "="*50)
print("ENHANCED RESEARCH RESULTS")
print("="*50)
print(f"Query: {result['query']}")
print(f"Sources analyzed: {result['sources']}")
print(f"\n{result['response']}")
print("="*50)

# Try more topics
print("\nTry these:")
print("deeper_research_topic('quantum computing advances')")
print("deeper_research_topic('space exploration news')")
