from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8686218205:AAGoy_3zED-NT4bNjsbyJMhWkja5xLTdLyI"
CHAT_ID = "1511371654"

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name")
    email = request.form.get("email")
    problem = request.form.get("problem")
    priority = request.form.get("priority")
    text = request.form.get("message")

    msg = f"""
طلب جديد

الاسم: {name}
البريد: {email}
النوع: {problem}
الأولوية: {priority}

الرسالة:
{text}
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

    return "تم الإرسال بنجاح"

app.run(host="0.0.0.0", port=5000)
