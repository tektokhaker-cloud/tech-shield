from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BOT_TOKEN = "ضع_التوكن_هنا"
CHAT_ID = "ضع_الايدي_هنا"

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html")

# الخدمات
@app.route("/services")
def services():
    return render_template("services.html")

# الإنجازات
@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

# من نحن
@app.route("/about")
def about():
    return render_template("about.html")

# التواصل
@app.route("/contact")
def contact():
    return render_template("contact.html")

# إرسال الطلب
@app.route("/send", methods=["POST"])
def send():

    name = request.form.get("name")
    email = request.form.get("email")
    problem = request.form.get("problem")
    priority = request.form.get("priority")
    message = request.form.get("message")

    text = f"""
🛡️ طلب جديد

👤 الاسم:
{name}

📧 البريد:
{email}

📂 النوع:
{problem}

⚡ الأولوية:
{priority}

📝 الرسالة:
{message}
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

    return render_template("success.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
