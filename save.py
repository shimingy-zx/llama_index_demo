import os
os.environ["OPENAI_API_KEY"] = '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'

from llama_index import VectorStoreIndex, SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext, load_index_from_storage
import sys
import logging



logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


documents = SimpleDirectoryReader('data').load_data()


index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist()


# query_engine = index.as_query_engine()
# response = query_engine.query("陆向谦是谁？")
# print(response)


# index.save_to_disk('index.json')

# index.build_index_from_nodes('index.json')
