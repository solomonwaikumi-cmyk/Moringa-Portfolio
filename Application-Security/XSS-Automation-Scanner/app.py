from flask import Flask, request, render_template_string

app = Flask(__name__)

# ---------------------
# Insecure Login Form (used in TL)
# ---------------------
login_template = """
<!doctype html>
<html>
  <head><title>Login</title></head>
  <body>
    <h2>Login</h2>
    <form method="POST" action="/login">
      <input type="text" name="username" placeholder="Username" required /><br/>
      <input type="password" name="password" placeholder="Password" required /><br/>
      <!-- No CSRF token on purpose -->
      <input type="submit" value="Login" />
    </form>
  </body>
</html>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Login attempt received (not secure)", 200
    return render_template_string(login_template)

# ---------------------
# Root path ("/") serves login form
# ---------------------
@app.route("/", methods=["GET"])
def home():
    return render_template_string(login_template)

# ---------------------
# Vulnerable Search Route (used in Lab)
# ---------------------
@app.route("/search")
def search():
    q = request.args.get("q", "")
    return f"<h1>Search Results for: {q}</h1>"

if __name__ == "__main__":
    app.run(port=5000)