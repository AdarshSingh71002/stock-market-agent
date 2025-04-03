from flask import Flask, request, jsonify
from fetch_stock_price import fetch_stock_price
from ai_agent import analyze_stock_price

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze():
    ticker = request.args.get('ticker')
    stock_price = fetch_stock_price(ticker)
    recommendation = analyze_stock_price(stock_price)
    return jsonify({'ticker': ticker, 'stock_price': stock_price, 'recommendation': recommendation})

if __name__ == '__main__':
    app.run(debug=True)