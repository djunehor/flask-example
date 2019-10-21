# Introduction
This is a very simple Flask RESTful API app that fetches genes from Ensembl public database.

# Running
* Clone this repo `git clone https://github.com/djunehor/flask-example.git`
* cd into the folder i.e `cd flask-example`
* Ensure you have at least Python 3.6
* Run `pip install -r requirements.txt`
* copy `.env.example` to `.env` and fill in the DB details
* Then run `python app/main.py`

# Testing
*First run `pip install pytest`
* Then run `pytest app/tests.py`

# Docker container
Run the following command to build the Docker image

```bash
docker build -t pw_api:0.1 .
```

Initialize a instance of the image 

```bash
docker run -d -p 80:80 pw_api:0.1
```

Access the container in a browser on port 80: http://127.0.0.1/
