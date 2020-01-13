from flask import Flask, render_template
import requests
from random import randint
import os

app = Flask(__name__)

try:
  api_key =os.environ["api_key"]
except:
  api_key = open("api_key.txt").read().strip()

# url = f"https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID={api_key}"

@app.route("/", methods=["GET"])
def index_get():
  ime_mesta = ["Ljubljana", "London", "Paris"][randint(0,2)]
  url = f"https://api.openweathermap.org/data/2.5/weather?q={ime_mesta}&units=metric&APPID={api_key}"
  result = requests.get(url).json()
  return render_template("index.html", data = result)

if __name__ == "__main__":
  app.run()
  