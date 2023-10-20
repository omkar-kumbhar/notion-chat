# Notion-ChatGPT Integration

## Author 
Omkar Kumbhar

This project integrates Notion with ChatGPT, allowing users to search for relevant content in Notion using ChatGPT and refine the search using FAISS.

## Current Features

- **Notion API Integration**: Fetch and process data from Notion.
- **Logging Utility**: A centralized logger for consistent logging across modules.
- **Unit Tests**: Basic tests for the Notion API interactions.

## Requirements

- Python 3.8+
- Notion API Key
- ChatGPT API Key
- FAISS

## Setup

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Set up your `.env` file with the necessary credentials and configurations.
4. Run the main application using `python src/main.py`.

## Testing

- notion api testing
    - Run the unit tests using: `python -m unittest tests/test_notion_api.py`


## Future Scope / TODOs

- **Database Integration**: Store the fetched Notion data in a structured database.
- **FAISS Integration**: Use FAISS to refine the search results from ChatGPT.
- **ChatGPT Plugin**: Develop a ChatGPT plugin to retrieve and display information.
- **Error Handling**: Enhance error handling, especially for external API interactions.
- **Logging Enhancements**: Improve logging by adding more granularity and potentially integrating with external logging platforms.
- **Performance Optimization**: As the data grows, optimize the search and retrieval mechanisms.
- **Security**: Ensure that sensitive data, especially API keys, are securely stored and accessed.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

This README provides a clear overview of the current state of the project and outlines the future scope. Adjustments can be made based on the project's evolution and specific requirements.