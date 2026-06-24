from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/v1/chat/completions', methods=['POST'])
def intercept_completions():
    data = request.get_json()
    
    if not data or 'messages' not in data:
        return jsonify({"error": "Invalid OpenAI payload format"}), 400

    messages = data.get('messages', [])
    system_prompt = ""
    
    for message in messages:
        if message.get('role') == 'system':
            system_prompt = message.get('content', '')
            break
            
    if system_prompt:
        print("\n=== CAPTURED CHARACTER DEFINITION ===")
        print(system_prompt)
        print("=====================================\n")
        
        with open("captured_character.txt", "w", encoding="utf-8") as f:
            f.write(system_prompt)
    else:
        print("System prompt not found in this request batch.")

    dummy_response = {
        "id": "chatcmpl-mock12345",
        "object": "chat.completion",
        "created": 1677652288,
        "model": data.get("model", "mock-model"),
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "[System Note: Character definition successfully captured by your local proxy server.]"
            },
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
    }
    
    return jsonify(dummy_response)

if __name__ == '__main__':
    PORT = 5000
    
    # Authenticate ngrok if you haven't set it via the CLI
    # ngrok_auth_token = os.environ.get("NGROK_AUTHTOKEN") or "YOUR_NGROK_AUTH_TOKEN"
    # ngrok.set_auth_token(ngrok_auth_token)

    try:
        public_url = ngrok.connect(PORT)
        print("\n" + "="*60)
        print(f" NGROK TUNNEL ACTIVE ")
        print(f" Public URL: {public_url.public_url}")
        print(f" Quick URL: {public_url.public_url}/v1/chat/completions")
        print(f" Use this base URL for your external client requests.")
        print("="*60 + "\n")
    except Exception as e:
        print(f"Failed to start ngrok tunnel: {e}")
        print("Continuing with local server execution only...")

    app.run(port=PORT, debug=True, use_reloader=False)
