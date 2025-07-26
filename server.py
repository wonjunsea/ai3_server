# server.py
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os
import time

# .env 파일 로드
load_dotenv()

app = Flask(__name__)
CORS(app)

CLOVA_API_KEY = os.getenv("CLOVA_API_KEY")
print(f"Loaded CLOVA_API_KEY: {CLOVA_API_KEY}")


@app.route("/api/clova-summary", methods=["POST"])
def clova_summary():
    try:
        # 요청 데이터
        data = request.json

        # Clova API 요청
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
        response.raise_for_status()  # HTTP 에러 발생 시 예외

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
    app.run(port=4000, debug=True)
