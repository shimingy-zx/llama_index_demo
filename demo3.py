from llama_index import VectorStoreIndex,download_loader

BilibiliTranscriptReader= download_loader("BilibiliTranscriptReader")
loader = BilibiliTranscriptReader()
documents = loader.load_data(video_urls=['https://www.bilibili.com/video/BV1ob4y147ZP/?share_source=copy_web&vd_source=032e10172d816c9446bcf2784824074d'])


index = VectorStoreIndex.from_documents(documents)


query_engine = index.as_query_engine()
response = query_engine.query("陆向谦实验室是什么？")
print(response)