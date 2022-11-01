# -*- coding: utf-8 -*-
import re
import requests
import lxml
from bs4 import BeautifulSoup as bs
from datetime import datetime
from google_images_download import google_images_download
from AI import keys

def return_tour(search):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
    cookie = {'CONSENT' : 'YES'}
    url = 'https://www.google.com/search?'
    params = {'q' : search , 'hl' : 'ko', 'source' : 'hp'}

    res = requests.get(url, params = params, headers = header, cookies = cookie)
    soup = bs(res.text, 'lxml')

    div_origin = soup.find('div', id='rso')
    div_list = div_origin.find_all('div', recursive=False)

    all_list = []

    for div in div_list:
        temp_dict = {}
        title = ''
        url = ''
        context = ''

        title_h3 = div.find('h3')
        url_tag = div.find('a', href=True)
        span_tag = div.find_all('span')

        if title_h3 != None:
            title = title_h3.text
        if url_tag != None:
            url = url_tag['href']
        for span in span_tag:
            context += span.text

        # 제목, 내용, 주소
        temp_dict['title'] = title
        temp_dict['context'] = context
        temp_dict['url'] = url

        # 구글 사이트 설명이라 스킵함
        if title == '' or title == '설명':
            pass
        else:
            all_list.append(temp_dict)

    return all_list

def googleImageCrawling(keyword, limit):
    response = google_images_download.googleimagesdownload()
    # 검색어와 제한개수, url을 출력할지, 무슨 형식으로 저장할지
    arguments = {'keywords':keyword, 'limit':limit, 'format':'jpg', 'no_download':True, 'silent_mode':True}
    paths = response.download(arguments)
    return paths

# 구글에서 이미지 검색 후 리스트로 url 반환
def getGoogleImages(keyword, limit):
    result = googleImageCrawling(keyword, limit)
    img_url_list = []
    if len(result) > 0:
        img_url_list = result[0][keyword]

    return img_url_list

doc = """
제가 인원을 다 봤는데 임상의사가 1명도 없더라고요.\"\n한국한의학연구원장 최승훈] \"의사는 양방 MD는 없습니다.\"\n박인숙 위원] \"그러니까 임상 현대의학 한 명도 없는데 제가 이것 논문 말씀드릴 것은 참 많은데 여기 책자에 보면 여러 가지 목표를 굉장히 많이 쓰셨는데 한마디로 너무 광범위하고 좀 애매모호하고 현실적ㆍ구체적인 실천 가능성이 너무 낮아 보이는 게 제 의견입니다.  한 예를 들면 하나의 목표에 1페이지에 있지요 ‘유전 요인을 고려한 생애 전 주기 고혈압 예방ㆍ관리 프로그램을 개발한다’ 이것은 사실 상상을 초월하는 엄청난 일이거든요. 전 세계 모든 사이언티스트가 달려서 목매달아도 지금 이게 해결이 안 되는데 이런 걸 목표로 삼으셨어요.  그리고 예산이 굉장히 많거든요 다른 데 예산에 비해서. 450 거의 445억이 되는데 이 기관의 목표가 국민 건강 증진이잖아요?\"\n한국한의학연구원장 최승훈] \"예.\"\n박인숙 위원] \"그런데 국민 건강 증진을 하려면 뭔가 실용적인 파이널 프로덕트가 나와야 되고 그전에 특허가 있어야 되고 그전에 논문이 있어야 되고 그전에 연구를 해야 되잖아요?\"\n한국한의학연구원장 최승훈] \"예 그렇습니다.\"\n박인숙 위원] \"그런데 연구 실적을 보면 SEI 논문 그러니까 논문하고 특허만 제가 말씀드리겠습니다 논문 숫자로 보면 해마다 64에서 77개를 냈는데 448억을 쓰면 연구 논문마다 6억 내지 7억의 비싼 논문인 것이거든요.   그런데 보통 과학계에서 연구비를 보면 논문 하나 내는데 많아야 2000 3000 5000만 원 이 정도가 주로 맥시멈인데 물론 다른 일도 하시지만 그것에 대해서 어떻게 생각하시는지 말씀해 주시지요.
"""

def return_final(keyword_list):
    if (keyword_list == None):
        return ''

    final_search = {}

    key_list = keyword_list.keys()

    for key in key_list:
        word_list = keyword_list[key]
        search = word_list[0]
        search_list = return_tour(search)
        img_list = getGoogleImages(search, 10)
        temp_dict = {}
        temp_dict['info'] = search_list
        temp_dict['img'] = img_list
        final_search[search] = temp_dict

    return final_search

# # 사용 예시
# search = '부산 관광지'
#
# search_list = return_tour(search)
# img_list = getGoogleImages(search, 10)

# print(search_list)
# print(img_list)

# keyword_list = keys.return_keyword(doc, keys.stop_list)
# key_list = keyword_list.keys()


