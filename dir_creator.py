import os

# List of directories to be created
directories = [
    "config",
    "src",
    "src/notion",
    "src/database",
    "src/chatgpt",
    "tests"
]

# List of files to be created
files = [
    "LICENSE",
    "Makefile",
    "README.md",
    "git_operations.log",
    "config/credentials.json",
    "config/settings.json",
    "src/notion/api.py",
    "src/notion/models.py",
    "src/database/db_connector.py",
    "src/database/models.py",
    "src/database/indexer.py",
    "src/chatgpt/plugin.py",
    "src/chatgpt/utils.py",
    "src/main.py",
    "tests/test_notion_api.py",
    "tests/test_database.py",
    "tests/test_chatgpt_plugin.py",
    "requirements.txt",
    ".env"
]

# Create directories
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

# Create files
for file in files:
    if not os.path.exists(file):
        with open(file, 'w') as f:
            pass  # Just create an empty file
        print(f"Created file: {file}")

print("Directory structure and files created!")
