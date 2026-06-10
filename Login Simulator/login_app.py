from flask import Flask, request, render_template_string
import logging


app = Flask(__name__)

# Log file dedicated to login activity
logging.basicConfig(
    filename='login.log',
    level=logging.INFO,
    format='%(asctime)s %(message)s'
)

HTML = """
<h2>Login Simulator</h2>
<form method="POST">
  Username: <input name="user"><br><br>
  Password: <input name="pass" type="password"><br><br>
  <button type="submit">Login</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        pwd = request.form.get("pass")

        # Simple fake auth logic (for lab purposes)
        if pwd == "admin123":
            logging.info(f"SUCCESS login user={user} ip={request.>
            return "<h3>Login Success</h3>"
        else:
            logging.warning(f"FAILED login user={user} ip={reques>

            return "<h3>Login Failed</h3>"

    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
