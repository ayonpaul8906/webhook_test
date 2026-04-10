from app import create_app
from flask import jsonify

app = create_app()
OPENAI_API_KEY= "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"

if __name__ == "__main__":
    app.run(port=5000)
