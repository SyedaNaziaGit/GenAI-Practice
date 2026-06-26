from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Linux Interview Guide.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ""
)

#result = splitter.split_text(text)
result = splitter.split_documents(docs)
print(result[0].page_content)#first chunk after split - this is also a document  obj having pagecontent and metadata keys in each  chunk 