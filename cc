curl "http://127.0.0.1:5000/analyze?ticker=AAPL"

python3 -m venv venv
sudo apt install python3.10-venv
source venv/bin/activate
pip install langchain requests Flask openai
pip install -r requirements.txt
python app.py
