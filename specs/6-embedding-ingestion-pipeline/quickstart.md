# Quickstart: Embedding Ingestion Pipeline

This guide provides the steps to set up and run the embedding ingestion pipeline.

## Prerequisites

-   Python 3.8+
-   `uv` installed (`pip install uv`)
-   A Cohere API key
-   A Qdrant Cloud URL and API key

## Setup

1.  **Create the project directory**:

    ```bash
    mkdir backend
    cd backend
    ```

2.  **Initialize the environment**:

    ```bash
    uv venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```

3.  **Install dependencies**:

    ```bash
    uv pip install cohere qdrant-client requests beautifulsoup4
    ```

4.  **Set environment variables**:

    Create a `.env` file in the `backend` directory with the following content:

    ```
    COHERE_API_KEY="your_cohere_api_key"
    QDRANT_URL="your_qdrant_cloud_url"
    QDRANT_API_KEY="your_qdrant_api_key"
    ```

## Running the Pipeline

The pipeline is run from a single script.

1.  **Create `main.py`**:

    Create a `main.py` file in the `backend` directory with the Python code for the pipeline.

2.  **Execute the script**:

    ```bash
    python main.py
    ```

The script will then crawl the specified website, process the content, and store the embeddings in your Qdrant collection.
