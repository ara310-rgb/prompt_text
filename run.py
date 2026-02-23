import http.server
import socketserver
import webbrowser
import threading
import os

# HTML 파일이 있는 폴더로 이동 (run.py와 같은 폴더에 있으면 그대로)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000
URL  = f"http://localhost:{PORT}/prompt-guide.html"

def open_browser():
    webbrowser.open(URL)

# 서버 시작 후 브라우저 자동 실행
threading.Timer(1.0, open_browser).start()

print(f"✅ 서버 시작: {URL}")
print("🛑 종료하려면 Ctrl + C 를 누르세요")

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()

# 완료