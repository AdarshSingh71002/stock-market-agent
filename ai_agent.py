import openai

# Replace 'your_actual_openai_api_key' with your actual OpenAI API key
openai.api_key = 'your_actual_openai_api_key'

def analyze_stock_price(stock_price):
    prompt = f"The current stock price of the company is {stock_price}. Considering the market trends and financial analysis, should I buy, sell, or hold?"
    client = openai.OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a financial advisor."},
            {"role": "user", "content": prompt}
        ]
    )
    recommendation = response.choices[0].message.content.strip()
    return recommendation