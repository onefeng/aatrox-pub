# -*- coding: utf-8 -*-

"""
@author: onefeng
@time: 2023/11/17 9:59
"""

# -*- coding: utf-8 -*-

"""
@author: onefeng
@time: 2023/11/15 18:24
"""
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

base_url = 'http://1.15.182.65:20004/'


@app.route("/note", methods=["GET"])
def get_data_by_note():
    note_id = request.args.get('note_id')
    url = base_url + '/api/storage/note'
    data = {
        'note_id': note_id
    }
    r = requests.get(url, params=data)
    # print(r.json())
    return jsonify(r.json())


@app.route("/comment", methods=["GET"])
def get_comment_by_note():
    note_id = request.args.get('note_id')
    url = base_url + 'api/storage/comment'
    data = {
        'note_id': note_id
    }
    r = requests.get(url, params=data)
    # print(r.json())
    return jsonify(r.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
