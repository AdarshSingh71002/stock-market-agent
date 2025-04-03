# Stock Market Agent

## Description
This project is an AI Agent built using Python, LangChain, and an LLM API to fetch and analyze stock market prices. It provides an API to get the latest stock prices and generate buy/sell/hold recommendations.

## Setup & Execution Process

### Prerequisites
- Python 3.7+
- Virtual environment (recommended)

### Installation
1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd stock-market-agent
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the API
1. Start the Flask API:
    ```sh
    python app.py
    ```

2. The API will be available at `http://127.0.0.1:5000/analyze`

### Usage
- To fetch and analyze stock prices, send a GET request to the `/analyze` endpoint with the `ticker` parameter.

Example:
```sh
curl http://127.0.0.1:5000/analyze?ticker=AAPL
```

### Deployment
- To deploy the project on Heroku:
    ```sh
    heroku create
    git add .
    git commit -m "Deploy initial version"
    git push heroku master
    heroku open
    ```

### License
This project is licensed under the MIT License.

