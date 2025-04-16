import requests
import json

def query_llm(message="Hello!", model="qwen2.5-0.5B-p256-ax630c", temperature=0.7, server_url="http://localhost:8000"):
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": message}],
        "temperature": temperature
    }
    
    response = requests.post(
        f"{server_url}/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_KEY"
        },
        json=data
    )
    
    return response.json()

if __name__ == "__main__":
    result = query_llm(message="Hello!", model="qwen2.5-0.5B-p256-ax630c", server_url="http://192.168.20.5:8000")
    print(json.dumps(result, indent=2, ensure_ascii=False))

