import os
from tavily import TavilyClient
from crewai.tools import tool

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

@tool("Web Search Tool")
def web_search_tool(query: str) -> str:
    """Searches the web for current information on a given query and returns results with sources."""
    results = tavily_client.search(query, max_results=5)
    formatted = "\n\n".join([
        f"Source: {r['url']}\n{r['content'][:500]}"
        for r in results['results']
    ])
    return formatted