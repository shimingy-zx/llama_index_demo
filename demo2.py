from pathlib import Path
from llama_index import download_loader,VectorStoreIndex
import os


os.environ["OPENAI_API_KEY"] = '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'

AudioTranscriber = download_loader("AudioTranscriber")


p = Path('podcast.mp4')           # 字符串拼接

print(p.exists())                           # 判断文件是否存在
loader = AudioTranscriber()
documents = loader.load_data(file=p)

index = VectorStoreIndex.from_documents(documents)



query_engine = index.as_query_engine()
response = query_engine.query("陆向谦实验室是什么？")
print(response)