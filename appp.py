from flask import Flask, render_template, request
import requests

BOT_TOKEN = "8686218205:AAGoy_3zED-NT4bNjsbyJMhWkja5xLTdLyI"
CHAT_ID = "1511371654"
app = Flask(__name__)
orders = []
ADMIN_PASSWORD = "soft23000"
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/cyber")
def cyber():
    return render_template("cyber.html")

@app.route("/websites")
def websites():
    return render_template("websites.html")

@app.route("/bots")
def bots():
    return render_template("bots.html")

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/consulting")
def consulting():
    return render_template("consulting.html")


@app.route("/order", methods=["POST"])
def order():

    name = request.form.get("name")
    service = request.form.get("service")
    details = request.form.get("details")

    msg = f"""
📩 طلب جديد

👤 الاسم: {name}
🛠 الخدمة: {service}
📝 التفاصيل: {details}
"""

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

    orders.append({
        "name": name,
        "service": service,
        "details": details
    })

    return """
    <h1 style='text-align:center;margin-top:50px'>
    ✅ تم ارسال الطلب بنجاح
    </h1>

    <center>
    <a href='/'>العودة للرئيسية</a>
    </center>
    """


@app.route("/admin")
def admin():

    password = request.args.get("password")

    if password != ADMIN_PASSWORD:
        return """
        <h2>🔒 صفحة محمية</h2>

        <form>
            <input type="password" name="password" placeholder="كلمة السر">
            <button type="submit">دخول</button>
        </form>
        """

    return render_template("admin.html", orders=orders)
@app.route("/about")
@app.route("/achievements")
@app.route("/contact")
def contact():
    return render_template("contact.html")
def achievements():
    return render_template("achievements.html")

@app.route("/login")
def login():
    return render_template("login.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
