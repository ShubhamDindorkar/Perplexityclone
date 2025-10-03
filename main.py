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
