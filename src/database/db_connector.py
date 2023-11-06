# db_connector.py
import os
import psycopg2
from psycopg2 import pool
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

class PostgresConnector:
    def __init__(self):
        self.db_name = os.getenv('POSTGRES_DB')
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('POSTGRES_HOST', 'localhost')
        self.port = os.getenv('POSTGRES_PORT', 5432)
        self.connection_pool = None
        self.setup_connection_pool()

    def setup_connection_pool(self):
        try:
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.db_name
            )
            if self.connection_pool:
                logger.info("Connection pool created successfully.")
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(f"Error while creating connection pool: {error}")
            raise

    def get_connection(self):
        try:
            connection = self.connection_pool.getconn()
            logger.debug("Successfully retrieved a connection from the pool.")
            return connection
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(f"Error while getting connection: {error}")
            raise

    def release_connection(self, connection):
        try:
            self.connection_pool.putconn(connection)
            logger.debug("Connection returned to the pool.")
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(f"Error while returning connection: {error}")
            raise

    def close_connection_pool(self):
        try:
            self.connection_pool.closeall()
            logger.info("Connection pool has been closed.")
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(f"Error while closing connection pool: {error}")
            raise

# Example usage
if __name__ == "__main__":
    connector = PostgresConnector()
    # Perform database operations...
    connector.close_connection_pool()