# indexer.py
from db_connector import PostgresConnector
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class Indexer:
    def __init__(self, connector: PostgresConnector):
        self.connector = connector

    def index_data(self, data):
        # Assuming 'data' is a dictionary that contains the data to be indexed
        conn = self.connector.get_connection()
        cursor = conn.cursor()
        try:
            # Assuming a table 'documents' with columns 'id' and 'content'
            cursor.execute(
                "INSERT INTO documents (id, content) VALUES (%s, %s)",
                (data['id'], data['content'])
            )
            conn.commit()
            logger.info(f"Data indexed successfully: {data['id']}")
        except Exception as e:
            conn.rollback()
            logger.error(f"Error indexing data: {e}")
        finally:
            cursor.close()
            self.connector.release_connection(conn)

# Example usage
if __name__ == "__main__":
    connector = PostgresConnector()
    indexer = Indexer(connector)
    # Example data to index
    data_to_index = {'id': '123', 'content': 'This is a sample document.'}
    indexer.index_data(data_to_index)
    connector.close_connection_pool()
