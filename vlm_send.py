import requests
import json
import base64
import os

def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def query_vlm(image_path, prompt="この画像に何が見えますか？", model="internvl2.5-1B-ax630c", server_url="http://localhost:8000"):
    if not os.path.exists(image_path):
        return {"error": f"画像ファイル '{image_path}' が見つかりません"}
    
    base64_image = image_to_base64(image_path)
    
    data = {
        "model": model,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
            ]
        }],
        "temperature": 0.2
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
    result = query_vlm("test.jpg", prompt="この画像に何が見えますか？", model="internvl2.5-1B-ax630c", server_url="http://192.168.20.5:8000")
    print(json.dumps(result, indent=2, ensure_ascii=False))