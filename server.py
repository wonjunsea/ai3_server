from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = Flask(__name__)
CORS(app)

CLOVA_API_KEY = os.getenv("CLOVA_API_KEY")
# print(f"Loaded CLOVA_API_KEY: {CLOVA_API_KEY}") 무서워요..

@app.route("/api/clova-summary", methods=["POST"])
def clova_summary():
    try:
        data = request.json
        response = requests.post(
            "https://clovastudio.stream.ntruss.com/v3/chat-completions/HCX-005",
            json=data,
            headers={
                "Authorization": f"Bearer {CLOVA_API_KEY}",
                "X-NCP-CLOVASTUDIO-REQUEST-ID": f"demo-{int(time.time())}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
        )
        response.raise_for_status()
        result = response.json()
        print("요약 결과:", result.get("result", {}).get("message", {}).get("content"))
        return jsonify(result)
    except requests.RequestException as e:
        return (
            jsonify(
                {"error": str(e), "detail": e.response.json() if e.response else None}
            ),
            500,
        )
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host="0.0.0.0", port=port)