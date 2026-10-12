try:
    from flask import Flask
except ImportError as exc:
    raise ImportError(
        "Flask is not installed in the active Python environment. "
        "Install it with `python -m pip install Flask`."
    ) from exc

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Flask CI!"


if __name__ == "__main__":
    app.run()
