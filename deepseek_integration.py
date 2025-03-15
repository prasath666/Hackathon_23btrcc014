import requests

# Set your DeepSeek API key
DEEPSEEK_API_KEY = "sk-caf7ef394fe8482a93693135d31dc4cb"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"  # Correct endpoint

def ask_deepseek(query):
    try:
        # Prepare the API request
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",  # Use the correct model name
            "messages": [{"role": "user", "content": query}],
            "max_tokens": 150,
            "temperature": 0.7
        }

        # Send the request to DeepSeek API
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes

        # Print the API response for debugging
        print("DeepSeek API Response:", response.json())

        # Extract the response
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"DeepSeek API Error: {e}")  # Print the full error
        return f"Error in DeepSeek API request: {e}"