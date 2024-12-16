import json
from scrapegraphai.graphs import SmartScraperGraph

OPENAI_API_KEY = "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"
GOOGLE_API_KEY = "AIzaSyDm4_MxyCOzycokC2LHuqE9fUeIn-3fL6E"

graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "openai/gpt-4o-mini",
    },
    "verbose": True,
    "headless": False,
}

def get_content_frm_link(link):

    #Chagne the prompt
    smart_scraper_graph = SmartScraperGraph(
    prompt="Inflammatory Bowel Disease (IBD) overview: Causes, symptoms, diagnosis, and treatment options for Crohn's disease and ulcerative colitis. Latest research and developments in managing IBD, including dietary recommendations, medication, and lifestyle changes. Explore the impact of IBD on daily life, potential complications, and advancements in medical therapies or surgeries.",
    source=link,
    config=graph_config,
    )

    result = smart_scraper_graph.run()
    return json.dumps(result, indent=4)