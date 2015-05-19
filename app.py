import os
import requests
import xmltodict
import json
from flask import Flask, request, Response, redirect

app = Flask(__name__)


@app.route('/', methods=['get'])
def ipl():
    """ converts xml to json
    """
    data = requests.get('http://synd.cricbuzz.com/j2me/1.0/livematches.xml').content
    a = xmltodict.parse(data)
    return json.dumps(xmltodict.parse(data), indent=4)


@app.route('/abc')
def hello():
    return redirect('https://github.com/shashisp/slack-ipl')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)