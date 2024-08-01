from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
load_dotenv()

#******************************** Initialize the connection **********************************
# pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT")) # Now not working
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


#******************************** Create a new index **********************************
# pc.create_index(name="test-index", dimension=8, metric="euclidean", spec=ServerlessSpec(
#         cloud="aws",
#         region="us-east-1"
#     ) )

# print(pc.describe_index("test-index"))

#******************************** Insert vectors **********************************
# Create a client instance that  targets the "test-index" index:
index = pc.Index("syllabus")
'''
index.upsert(
    vectors=[
        {"id": "vec1", "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]},
        {"id": "vec2", "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]},
        {"id": "vec3", "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]},
        {"id": "vec4", "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]},
    ],
    namespace = "ns1"
)

index.upsert(
    vectors=[
        {"id": "vec5", "values": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]},
        {"id": "vec6", "values": [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]},
        {"id": "vec7", "values": [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7]},
        {"id": "vec8", "values": [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8]},
    ],
    namespace = "ns2"
)
'''
#******************************** Fetch records **********************************
print(index.fetch(["vec1", "vec2"], "ns1"))

#******************************** Update records **********************************
#Full update
index.upsert([("vec3", [3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3, 3.3])], "ns1")

#Partial update
index.update(id="vec4", values=[4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4, 4.4], namespace="ns1")

index.update(id="vec4", set_metadata={"type": "web", "new": True}, namespace="ns1")


#******************************** Delete records **********************************
# index.delete(ids=["vec1", "vec2"], namespace="ns1")

# index.delete(delete_all=True, namespace="ns2")

#******************************** delete index **********************************
pc.delete_index("test-index")