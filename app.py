from flask import Flask, request, jsonify, make_response
import json
import requests
app = Flask(__name__)
URL = 'http://numbersapi.com/'

@app.route('/', methods=['GET'])
def home():
    return "hello from prafful"

@app.route('/', methods=['POST'])
def post():
    req = request.get_json(silent = True, force = True) # json object to python dictionary
    intent = req.get('queryResult').get('intent').get('displayName')
    if intent == 'Default Welcome Intent':
        return jsonify({"fulfillmentText": "Welcome to cool number facts. Here's what I, numberBot can do for you.\n1. Tell you trivia about a number\n2. Tell you maths facts about a number\n3. Tell you something interesting about a year\n"})
    elif intent == 'numbers':
        t = req.get('queryResult').get('parameters').get('type')
        num = int(req.get('queryResult').get('parameters').get('number'))
        url = URL + str(num) + "/" + t + "?json"
        response = requests.get(url)
        txt = response.json()["text"]
        return jsonify({"fulfillmentText": txt})


if(__name__ == "__main__"):
    app.run()
