from openai import OpenAI

from pymongo import MongoClient
import pymongo

OPENAI_API_KEY = "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"
MONGO_URI = "mongodb+srv://macromrit:amma1953@channel-partners-docs.tgvml83.mongodb.net/?retryWrites=true&w=majority&appName=Channel-Partners-Docs"

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return (OpenAI(api_key=OPENAI_API_KEY)
           .embeddings.
           create(input = [text], model=model).data[0].embedding)


uri = MONGO_URI

client = MongoClient(uri, server_api=pymongo.server_api.ServerApi(version="1", strict=False, deprecation_errors=True))

database_name = "Channel-Partner-RAG"
collection_name = "IBD-Data"

db = client.get_database(database_name)
collection = db.get_collection(collection_name)


def vector_search(user_query: str, filter_pdf_name: str, db=db, collection=collection, vector_index="IBD-Index"):
    query_embedding = get_embedding(user_query)
    if query_embedding is None:
        return "Invalid query or embedding generation failed."

    vector_search_stage = {
        "$vectorSearch": {
            "index": vector_index,  # specifies the index to use for the search
            "queryVector": query_embedding,  # the vector representing the query
            "path": "text_embeddings",  # field in the documents containing the vectors to search against
            "numCandidates": 150,  # number of candidate matches to consider
            "limit": 10,  # return top 20 matches
            # "filter": {
            #     "pdf_name": filter_pdf_name
            # },
        }
    }

    pipeline = [vector_search_stage]
    results = collection.aggregate(pipeline)
    
    return list(results)

def getUnBiasedResponses(query):
    all_docs = ["/content/BIO-DOCS/1-s2.0-S216183132400053X-main.pdf", "/content/BIO-DOCS/NUTRITIVE-VALUE-OF-INDIAN-FOODS-ICMR_Optimized.pdf", "/content/BIO-DOCS/PIIS001650852305597X.pdf", "/content/BIO-DOCS/PIIS1542356522011065.pdf", "/content/BIO-DOCS/Patient education_ Type 2 diabetes and diet (Beyond the Basics) - UpToDate.pdf", "/content/BIO-DOCS/dci190014.pdf", "/content/BIO-DOCS/izz268.pdf", "/content/BIO-DOCS/jjab178.pdf", "/content/BIO-DOCS/jjz180.pdf", "/content/BIO-DOCS/otad077.pdf", "/content/BIO-DOCS/s12664-018-0890-5.pdf"]
    
    solution = ""
    
    for doc in all_docs:
        for response in vector_search(query, doc):
            solution = solution + response['text_content'] + "\n"
    
    return solution


if __name__ == "__main__":
    print(getUnBiasedResponses("What to Eat for an Indian Taste"))