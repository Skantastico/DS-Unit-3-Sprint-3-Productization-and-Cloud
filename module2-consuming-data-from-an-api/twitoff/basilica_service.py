
import os
import basilica
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")

sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]

connection = basilica.Connection(BASILICA_API_KEY)

embeddings = list(connection.embed_sentences(sentences))

print(embeddings)

for emb in embeddings:
    print(type(emb))
    print(emb)
    print("------------")
