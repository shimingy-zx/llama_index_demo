import os
os.environ["OPENAI_API_KEY"] = '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'



from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("陆向谦是谁？")
print(response)

