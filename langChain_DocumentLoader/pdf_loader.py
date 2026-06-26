from langchain_community.document_loaders import  PyPDFLoader
#PyPDF loader is mostly used when the pdf has text it doesnt work well with image pdf
loader = PyPDFLoader("Email Writing.pdf")
docs = loader.load()
print(len(docs)) #11
print(docs[0].page_content)
print(docs[1].metadata)