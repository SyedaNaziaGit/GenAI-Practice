#used to load multiple pdfs present inside any folder we use Directory loader
from langchain_community.document_loaders import  DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

for eachdoc in docs:
    print(eachdoc.metadata)
    
#using lazyload method - it creates a generator and loads one docs at one time
docs1 = loader.lazy_load()
for document in docs1:
    print(document.metadata)