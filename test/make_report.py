#import pyaudio
import threading
import time
from threading import Event
from flask import Flask
import wave
from AI import vitoNormalSTTGET
from AI import google_new
from AI import keys
from AI import textSummary
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
import datetime
import pandas as pd
from apyori import apriori
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
from fpdf import FPDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib.pagesizes import A4
from urllib import request
import time
import os
from PIL import Image as pilImage
from io import BytesIO

client = pymongo.MongoClient(
    "mongodb+srv://metaverse123:hongil123@accidentlyunity.ts7ta4j.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.zzang

talkDB = db.talk
keywordDB = db.keyword
searchDB = db.search
imageDB = db.image
summaryDB = db.summary
graphDB = db.graph

audio_list = {}
events = {}
num = 0
ai_events = {}
ai_num_list = {}
room_list = {}
sound_num_list = {}
sid_nickname_list = {}
sid = 1


def make_minutes(sid):
    sid = str(sid)
    sid = 1

    paper_width = 400

    pdf_path = './export_pdf/'
    summaryName = SimpleDocTemplate(pdf_path + str(sid) + '.pdf', pagesize=A4)

    FONT_FILE = '%s/Fonts/%s' % (os.environ['WINDIR'], 'BATANG.TTC')
    FONT_NAME = '바탕'
    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_FILE))
    h_center_style = ParagraphStyle(
        name='Normal', fontName=FONT_NAME, fontSize=16, alignment=TA_CENTER, leading=24)
    h_left_style = ParagraphStyle(
        name='Normal', fontName=FONT_NAME, fontSize=16, alignment=TA_LEFT, leading=24)
    h_right_style = ParagraphStyle(
        name='Normal', fontName=FONT_NAME, fontSize=16, alignment=TA_RIGHT, leading=24)

    c_left_style = ParagraphStyle(
        name='Normal', fontName=FONT_NAME, fontSize=12, alignment=TA_LEFT, leading=16)
    c_right_style = ParagraphStyle(
        name='Normal', fontName=FONT_NAME, fontSize=12, alignment=TA_RIGHT, leading=16)
    c_center_style = ParagraphStyle(
        name='Normal', fontName=FONT_NAME, fontSize=12, alignment=TA_CENTER, leading=16)

    line_draw = Drawing(paper_width, 1)
    line_draw.add(Line(0, 0, paper_width, 0))

    parts = []

    talk_list = list(talkDB.find({'id': sid}).sort('_id', 1))
    # 나중에 gt:0으로 변경하기
    key_list = list(keywordDB.find(
        {'id': sid, 'favorite': {'$gt': -1}}).sort('_id', 1))
    search_list = list(searchDB.find(
        {'id': sid, 'favorite': {'$gt': -1}}).sort('_id', 1))
    image_list = list(imageDB.find(
        {'id': sid, 'favorite': {'$gt': -1}}).sort('_id', 1))
    graph_list = list(graphDB.find(
        {'id': sid, 'favorite': {'$gt': -1}}).sort('_id', 1))

    summary_list = list(summaryDB.find({'id': sid}).sort('_id', 1))

    time_list = []
    type_list = ['talk', 'summary', 'keyword', 'search', 'image', 'graph']

    for idx, talk in enumerate(talk_list):
        temp_dict = {}
        temp_dict['id'] = talk['_id']
        temp_dict['time'] = talk['start']
        temp_dict['type'] = 0
        temp_dict['index'] = idx

        time_list.append(temp_dict)

    for idx, summary in enumerate(summary_list):
        temp_dict = {}
        temp_dict['id'] = summary['_id']
        temp_dict['time'] = summary['time']
        temp_dict['type'] = 1
        temp_dict['index'] = idx

        time_list.append(temp_dict)

    for idx, key in enumerate(key_list):
        temp_dict = {}
        temp_dict['id'] = key['_id']
        temp_dict['time'] = key['time']
        temp_dict['type'] = 2
        temp_dict['index'] = idx

        time_list.append(temp_dict)

    for idx, search in enumerate(search_list):
        temp_dict = {}
        temp_dict['id'] = search['_id']
        temp_dict['time'] = search['time']
        temp_dict['type'] = 3
        temp_dict['index'] = idx

        time_list.append(temp_dict)

    for idx, image in enumerate(image_list):
        temp_dict = {}
        temp_dict['id'] = image['_id']
        temp_dict['time'] = image['time']
        temp_dict['type'] = 4
        temp_dict['index'] = idx

        time_list.append(temp_dict)

    for idx, graph in enumerate(graph_list):
        temp_dict = {}
        temp_dict['id'] = graph['_id']
        temp_dict['time'] = graph['time']
        temp_dict['type'] = 5
        temp_dict['index'] = idx

        time_list.append(temp_dict)

    # 텍스트, 요약, 키워드, 검색결과, 그래프 순
    time_list = sorted(time_list, key=lambda k: (k['time'], k['type'], k['id']))

    temp_str = ''
    temp_type = ''
    temp_key = ''
    temp_key_list = ''
    temp_img_list = []
    temp_img_name = []
    base_dir = './temp_image/'
    img_cnt = 0

    for temp in time_list:
        if temp_type is not temp['type']:
            if temp_type == 2:
                parts.append(Paragraph(temp_key_list, style=c_left_style))
                temp_key_list = ''

            if temp_type == 4 and len(temp_img_list) > 0:
                file_name = str(temp['id']) + '.jpg'
                real_file_name = base_dir + file_name
                tmp = np.hstack(temp_img_list[:len(temp_img_list)])
                img = pilImage.fromarray(tmp)
                img.save(real_file_name)
                temp_img_name.append(real_file_name)
                parts.append(Image(filename=real_file_name, width=500, height=100))
                img_cnt = 0
                temp_img_list = []

            parts.append(line_draw)
            parts.append(Paragraph(type_list[temp['type']], style=h_left_style))
            parts.append(Paragraph(' '))
            temp_type = temp['type']

        # 채팅 내용
        if temp['type'] == 0:
            talk = talk_list[temp['index']]
            parts.append(Paragraph(' '))
            temp_str = talk['context']
            parts.append(Paragraph(temp_str, style=c_left_style))
            parts.append(Paragraph(' '))

        # 요약본
        if temp['type'] == 1:
            parts.append(line_draw)
            summary = summary_list[temp['index']]
            parts.append(Paragraph(' '))
            temp_str = summary['context']
            parts.append(Paragraph(temp_str, style=c_left_style))
            parts.append(Paragraph(' '))

        # 키워드
        if temp['type'] == 2:
            key = key_list[temp['index']]
            parts.append(Paragraph(' '))
            if key['main_key'] != temp_key:
                temp_key = key['main_key']
                parts.append(Paragraph(temp_key_list, style=c_left_style))
                parts.append(Paragraph(temp_key, style=h_left_style))
                parts.append(Paragraph(' '))
                temp_key_list = ''
            else:
                temp_key_list += key['real_key'] + ', '

        # 구글 검색 결과
        if temp['type'] == 3:
            search = search_list[temp['index']]
            parts.append(Paragraph(' '))
            parts.append(
                Paragraph('제목 : ' + search['title'], style=c_left_style))
            parts.append(
                Paragraph('내용 : ' + search['context'], style=c_left_style))
            parts.append(
                Paragraph('링크 : ' + search['url'], style=c_left_style))
            parts.append(Paragraph(' '))

        if temp['type'] == 5:
            graph = graph_list[temp['index']]
            parts.append(Paragraph(' '))
            file_name = graph['file']
            img = Image(file_name, width=600, height=300)
            parts.append(img)

    summaryName.build(parts)

    print('끝')


make_minutes(1)
