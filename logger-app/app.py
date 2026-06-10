from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Logger App</title>
<h1>Submit a Message</h1>
<form method=post>
  <input type=text name=message>
  <input type=submit value=Submit>
</form>
<h2>Messages:</h2>
<pre>{{ messages }}</pre>
"""

LOGFILE = "/home/azureuser/messages.log"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form['message']
        with open(LOGFILE, 'a') as f:
            f.write(msg + '\n')

    try:
        with open(LOGFILE, 'r') as f:
            msgs = f.read()
    except FileNotFoundError:
        msgs = ""

    return render_template_string(TEMPLATE, messages=msgs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)