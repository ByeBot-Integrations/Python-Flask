import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuration - update these values for your setup
CAPTCHACAT_API_KEY = ""
CAPTCHACAT_SITE_KEY = "bd1cc81c04564d3f899e" # Just an example sitekey so the widget shows up


def validate_captcha_token(token: str) -> dict:
    """Validate the CAPTCHA token with the server."""
    try:
        response = requests.post(
            "https://challenge.captchacat.com/validate_token",
            json={"api_key": CAPTCHACAT_API_KEY, "token": token},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        if response.ok:
            return {"valid": True}
        return {"valid": False, "message": f"Server error: {response.status_code}"}
    except requests.RequestException as e:
        return {"valid": False, "message": str(e)}


@app.route("/")
def index():
    return render_template("index.html", site_key=CAPTCHACAT_SITE_KEY)


@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    token = request.form.get("captchacat-token", "")

    if not token:
        return render_template(
            "index.html",
            site_key=CAPTCHACAT_SITE_KEY,
            error="Please complete the CAPTCHA",
        )

    result = validate_captcha_token(token)

    if result["valid"]:
        return render_template(
            "result.html",
            success=True,
            username=username,
            message="Form submitted successfully!",
        )
    else:
        return render_template(
            "index.html",
            site_key=CAPTCHACAT_SITE_KEY,
            error=f"CAPTCHA validation failed: {result.get('message', 'Unknown error')}",
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
