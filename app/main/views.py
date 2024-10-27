import requests
import html

from config import config
from flask import Response, request

from main import app, cache
from main.utils import get_hash_name

@app.route("/monster/<name>")
def get_identicon(name:str):

    name = html.escape(name, quote=True)
    image = cache.get(name)

    if image is None:
        print("Cache miss", flush=True)
        r = requests.get("http://dnmonster:8080/monster/" + name + "?size=80")
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype="image/png")

@app.route("/", methods=["GET", "POST"])
def mainpage():

    name = config["DEFAULT_NAME"]
    if request.method == "POST":
        name = html.escape(request.form["name"], quote=True)

    hash_name = get_hash_name(name, config["SALT"])

    header = "<html><head><title>Identidock</title></head><body>"
    body = """
        <form method='POST'>
            Hello <input type='text' name='name' value='{0}'>
            <input type='submit' value='submit'>
        </form>
        <p>
            You look like a:
            <img src='/monster/{1}'/>
    """.format(name, hash_name)
    footer = "</body></html>"

    return header + body + footer