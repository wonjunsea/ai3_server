```cmd
 python -m venv venv
 -먼저 venv 만들어야 됩니다.
```cmd
source venv/bin/activate
```
- 명령어 입력해서 venv 가상환경 접속하시고

```cmd
pip install -r requirements.txt
```
- 필요 라이브러리 설치

```cmd
python3 server.py
```
- 서버 정상 작동합니다

```cmd
CLOVA_API_KEY=your-api-key-here
```

- .env파일 생성하시고 위 내용 추가해주세요
