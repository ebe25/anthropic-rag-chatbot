import voyageai
##RAG retriver file
from dotenv import load_dotenv
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
import voyageai
load_dotenv()

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")



REVIEWS_CSV_PATH = "data/reviews.csv"
REVIEWS_CHROMA_PATH = "chroma_data" #datasopurce of ther db in local env

loader = CSVLoader(file_path=REVIEWS_CSV_PATH, source_column="review")
reviews = loader.load()

# split it into chunks
text_splitter = CharacterTextSplitter(chunk_size=128, chunk_overlap=0)
docs = text_splitter.split_documents(reviews)


#creating embeddings with Voage api
vo = voyageai.Client()

# page_content = []
# selected_chunks = []
# batch_size = 128

# for review in reviews:
#     page_content.append(review.page_content)
    
# def embeddingFunc():
#     for i in range(0, len(page_content), batch_size):
#         batch = page_content[i:i + batch_size]
#         response=vo.embed(texts=batch, model="voyage-large-2", input_type="document")
#     return response.embeddings



embedding_fuc = vo.embed(texts=docs, model="voyage-large-2", input_type="document")
#making a vector db with embeddings 
reviews_vector_db = Chroma.from_documents(docs,embedding_fuc , persist_directory=REVIEWS_CHROMA_PATH)
print(reviews_vector_db)


