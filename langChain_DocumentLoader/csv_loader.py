from langchain_community.document_loaders import  CSVLoader
loader = CSVLoader(file_path="social_network.csv")
docs = loader.load()
print(len(docs))#400- rows -  each row is a doc


