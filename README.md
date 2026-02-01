# Captchacat - Flask Example

A Flask application demonstrating Captchacat integration.

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Edit the values at the top of `app.py`:

```python
CAPTCHACAT_API_KEY = "your-api-key"
CAPTCHACAT_SITE_KEY = "your-site-key"
```

## Usage

```bash
python app.py
```

Visit `http://localhost:5000`

## How It Works

1. **Frontend**: The widget is loaded via `<script src="https://challenge.captchacat.com/ray/widget.js">`. A div with `class="captcha-widget"` and `data-sitekey` attribute renders the CAPTCHA.

2. **Token Submission**: On verification, the widget adds a hidden `captchacat-token` field to the form.

3. **Server Validation**: POST the token to `/validate_token`:

```python
response = requests.post(
    "https://challenge.captchacat.com/validate_token",
    json={"api_key": CAPTCHACAT_API_KEY, "token": token}
)
# 200 OK = valid token
```

## Files

- `app.py` - Flask server with form handling and token validation
- `templates/index.html` - Login form with CAPTCHA widget
- `templates/result.html` - Success page
