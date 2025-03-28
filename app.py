from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv 
import os

load_dotenv() # Load environment variables from .env file

openai.api_key = os.getenv('OPENAI_API_KEY')
print(openai.api_key)
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def get_opinion():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get('prompt', '')
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )
            return jsonify({"response": response.choices[0].message.content}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)

