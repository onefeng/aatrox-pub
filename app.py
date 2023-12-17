# -*- coding: utf-8 -*-


"""
@author: onefeng
@time: 2023/11/15 18:24
"""
import json
import os
from flask import Flask, request, jsonify, abort
import requests

app = Flask(__name__)

base_url = 'http://1.15.182.65:20005/'

token = os.getenv('token')
headers = {
    'Authorization': f'bearer {token}'
}


def api_jsonify(code, message, data=None):
    if data is None:
        return jsonify({
            'code': code,
            'message': message
        })
    return jsonify({
        'code': code,
        'message': message,
        'data': data
    })


def get_token():
    authorization = request.headers.get('Authorization')
    if authorization:
        try:
            token_type, _token = authorization.split(None, 1)
            if token_type.lower() != 'bearer':
                # if error, exit and return error msg
                abort(api_jsonify(400, 'token must be bearer'))
            if _token != token:
                abort(api_jsonify(400, 'token err'))
            return token_type, token
        except ValueError:
            # if error, exit and return error msg
            abort(api_jsonify(400, 'authorization format error'))
    else:
        # if error, exit and return error msg
        abort(api_jsonify(400, 'can not find token in request head'))


@app.route("/note", methods=["GET"])
def get_data_by_note():
    # get_token()
    note_id = request.args.get('note_id')
    url = base_url + '/api/storage/note'
    data = {
        'note_id': note_id
    }
    r = requests.get(url, params=data, headers=headers)
    return jsonify(r.json())


@app.route("/comment", methods=["GET"])
def get_comment_by_note():
    # get_token()
    note_id = request.args.get('note_id')
    url = base_url + 'api/storage/comment'
    data = {
        'note_id': note_id
    }
    r = requests.get(url, params=data, headers=headers)
    return jsonify(r.json())


@app.route("/keywords", methods=["GET"])
def get_comment_by_keywords():
    # get_token()
    keywords = request.args.get('keywords')
    limit = request.args.get('limit')
    url = base_url + 'api/storage/keywords'
    data = {
        'keywords': keywords,
        'limit': limit
    }
    r = requests.get(url, params=data, headers=headers)
    return jsonify(r.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
