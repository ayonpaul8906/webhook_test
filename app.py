import os
from app import create_app
from flask import jsonify

app = create_app()
OPENAI_API_KEY= process.env.OPENAI_API_KEY_0
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

if __name__ == "__main__":
    app.run(port=5000)
