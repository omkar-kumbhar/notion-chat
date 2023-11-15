# vector_search.py
import faiss
import numpy as np
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class VectorSearch:
    def __init__(self, dimension, index_file_path=None):
        self.dimension = dimension
        self.index = None
        if index_file_path:
            self.load_index(index_file_path)
        else:
            self.create_index()

    def create_index(self, index_description='Flat'):
        try:
            self.index = faiss.index_factory(self.dimension, index_description)
            logger.info("New FAISS index created.")
        except Exception as e:
            logger.error(f"Error creating FAISS index: {e}")
            raise

    def load_index(self, index_file_path):
        try:
            self.index = faiss.read_index(index_file_path)
            logger.info("FAISS index loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading FAISS index: {e}")
            raise

    def update_index(self, vectors):
        if not self.index.is_trained:
            logger.info("Training the index.")
            self.index.train(vectors)
        logger.info("Adding vectors to the index.")
        self.index.add(vectors)
        logger.info("Vectors added to the index.")

    def save_index(self, index_file_path):
        try:
            faiss.write_index(self.index, index_file_path)
            logger.info(f"FAISS index saved to {index_file_path}.")
        except Exception as e:
            logger.error(f"Error saving FAISS index: {e}")

    def search(self, query_vector, top_k):
        if not self.index:
            logger.error("Index is not created or loaded.")
            return None
        query_vector = np.array(query_vector).astype('float32').reshape(1, -1)
        distances, indices = self.index.search(query_vector, top_k)
        return distances, indices

# Example usage
if __name__ == "__main__":
    dimension = 128  # Example dimension
    search_engine = VectorSearch(dimension)
    
    # Example vectors for training and adding to the index
    vectors_to_add = np.random.rand(1000, dimension).astype('float32')
    search_engine.update_index(vectors_to_add)
    
    # Save the index to a file
    index_file_path = 'path_to_your_faiss_index.index'
    search_engine.save_index(index_file_path)
    
    # Load the index from a file
    search_engine.load_index(index_file_path)
    
    # Example query vector
    query_vector = np.random.rand(dimension).astype('float32')
    distances, indices = search_engine.search(query_vector, top_k=5)
    print("Distances:", distances)
    print("Indices:", indices)
