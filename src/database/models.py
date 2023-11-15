# models.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.logger import get_logger

# Initialize logger
logger = get_logger(__name__)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

# Database setup
def setup_database(engine_url):
    engine = create_engine(engine_url)
    Base.metadata.create_all(engine)
    return engine

# Example usage
if __name__ == "__main__":
    engine_url = 'postgresql://user:password@localhost/dbname'
    engine = setup_database(engine_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Perform database operations...
    session.close()
