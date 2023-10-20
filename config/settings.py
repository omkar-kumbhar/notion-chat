import os
from dotenv import load_dotenv
from pathlib import Path

# Locate the root directory
project_root = Path(__file__).parent.parent

# Load environment variables
dotenv_path = project_root / '.env'
load_dotenv(dotenv_path)

NOTION_KEY = os.getenv('NOTION_KEY')
NOTION_PAGE_ID = os.getenv('NOTION_PAGE_ID')
LOG_PATH = os.getenv('LOG_PATH', project_root / 'default_logs.log')  # Default to 'default_logs.log' in the project root if LOG_PATH is not set
