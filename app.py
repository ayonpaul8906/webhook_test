import os
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

if __name__ == "__main__":
    app.run(port=5000, debug=True, use_reloader=False)
