from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# GitHub API URL
GITHUB_API_URL = "https://api.github.com/users/{user}/gists"

@app.route('/<username>', methods=['GET'])
def get_user_gists(username):
    """Fetch a user's public gists from GitHub."""
    url = GITHUB_API_URL.format(user=username)
    response = requests.get(url)

    if response.status_code == 200:
        # Return the list of gists
        gists = response.json()
        return jsonify(gists)
    else:
        # Handle error if GitHub API responds with an error
        return jsonify({"error": "Unable to fetch gists for the specified user"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
