Prerequisites:
- VS Code: Make sure you have Visual Studio Code installed on your machine.
- Python: Install Python (version 3.x) if you don't have it already.
- Docker: Ensure Docker is installed on your system to build and run the container.

There are two options on run this
First options: 

Open the Docker panel in VS Code or use the terminal to build the Docker image:
- docker build -t github-api .

After the image is built, run the Docker container:
- docker run -d -p 8080:8080 github-api

Once the Docker container is running, you can test the API again.
- curl http://localhost:8080/octocat


Second options:

In the VS Code terminal, start the Flask server:
- python app.py
The server will run on http://localhost:8080.
Open a browser and navigate to http://localhost:8080/octocat. You should see a list of gists for the GitHub user octocat

In the VS Code terminal, run the tests with:
- python -m unittest test_app.py

