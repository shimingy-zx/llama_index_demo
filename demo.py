import os
os.environ["OPENAI_API_KEY"] = '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'

import logging
import sys
from llama_index import VectorStoreIndex, SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext, load_index_from_storage


# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


documents = SimpleDirectoryReader('data').load_data()


index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist()


query_engine = index.as_query_engine()
response = query_engine.query("陆向谦是谁？")
print(response)


# indexs = GPTVectorStoreIndex(documents, chunk_size_limit=500)
# # 保存索引
# indexs.storage_context('index.json')


# index.save_to_disk('index.json')

# index.build_index_from_nodes('index.json')
