#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import json

# import my_settings

client_id = 'yg1799nptx'
client_secret = 'M8jQcZTp8a8hAUdfT312MxFNelxTAa9a4N9HEkrR'
url = 'https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize'

headers = {
    'Accept': 'application/json;UTF-8',
    'Content-Type': 'application/json;UTF-8',
    'X-NCP-APIGW-API-KEY-ID': client_id,
    'X-NCP-APIGW-API-KEY': client_secret
}

def txt_summary(text, count):
    text_summary_result = None

    data = {
        "document": {
            "content": text
        },
        "option": {
            "language": "ko",
            "model": "general",
            "tone": 0,
            "summaryCount": count
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data).encode('UTF-8'))
    rescode = response.status_code

    if (rescode == 200):
        text_summary_result = response.text
    else:
        print("Error : " + response.text)

    return text_summary_result