import os
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
OPENAI_API_KEY= process.env.OPENAI_API_KEY_0

if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=False)
