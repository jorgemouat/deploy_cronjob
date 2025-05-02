import requests
from datetime import datetime

def fetch_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()

    joke = data["value"]
    log = f"{datetime.now()}: {joke}"
    print(log)

    with open("chuck_jokes_log.txt", "a") as f:
        f.write(log + "\n")

if __name__ == "__main__":
    fetch_joke()
