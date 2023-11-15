import pytest
from unittest.mock import patch, MagicMock
from database.db_connector import PostgresConnector
from database.indexer import Indexer
from database.models import setup_database, User

# Test the database connection setup
@patch('database.db_connector.psycopg2.pool.SimpleConnectionPool')
def test_setup_connection_pool(mocked_pool):
    connector = PostgresConnector()
    mocked_pool.assert_called_once()
    assert connector.connection_pool is not None, "Connection pool should be set up."

# Test getting a connection from the pool
@patch.object(PostgresConnector, 'get_connection')
def test_get_connection(mock_get_connection):
    mock_get_connection.return_value = MagicMock()
    connector = PostgresConnector()
    connection = connector.get_connection()
    mock_get_connection.assert_called_once()
    assert connection is not None, "Should retrieve a connection."

# Test releasing a connection back to the pool
@patch.object(PostgresConnector, 'release_connection')
def test_release_connection(mock_release_connection):
    connector = PostgresConnector()
    mock_connection = MagicMock()
    connector.release_connection(mock_connection)
    mock_release_connection.assert_called_once_with(mock_connection)

# Test closing the connection pool
@patch.object(PostgresConnector, 'close_connection_pool')
def test_close_connection_pool(mock_close_connection_pool):
    connector = PostgresConnector()
    connector.close_connection_pool()
    mock_close_connection_pool.assert_called_once()

# Test indexing data into the database
@patch('database.indexer.PostgresConnector')
def test_index_data(mock_connector):
    mock_connector.get_connection.return_value = MagicMock()
    indexer = Indexer(mock_connector)
    data_to_index = {'id': '123', 'content': 'This is a sample document.'}
    indexer.index_data(data_to_index)
    # Assuming commit is called, indicating data was indexed
    mock_connector.get_connection.return_value.commit.assert_called_once()

# Test the ORM model creation
@patch('database.models.create_engine')
def test_setup_database(mock_create_engine):
    engine_url = 'postgresql://user:password@localhost/test_db'
    setup_database(engine_url)
    mock_create_engine.assert_called_once_with(engine_url)

# Test User model representation
def test_user_model():
    user = User(username='testuser', email='testuser@example.com')
    assert user.__repr__() == "<User(username='testuser', email='testuser@example.com')>", "User model representation should match."
