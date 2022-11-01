# -*- coding: utf-8 -*-
from konlpy.tag import Mecab
from collections import Counter
from gensim.models.word2vec import Word2Vec

doc = '제가 인원을 다 봤는데 임상의사가 1명도 없더라고요.\"\n한국한의학연구원장 최승훈] \"의사는 양방 MD는 없습니다.\"\n박인숙 위원] \"그러니까 임상 현대의학 한 명도 없는데 제가 이것 논문 말씀드릴 것은 참 많은데 여기 책자에 보면 여러 가지 목표를 굉장히 많이 쓰셨는데 한마디로 너무 광범위하고 좀 애매모호하고 현실적ㆍ구체적인 실천 가능성이 너무 낮아 보이는 게 제 의견입니다.  한 예를 들면 하나의 목표에 1페이지에 있지요 ‘유전 요인을 고려한 생애 전 주기 고혈압 예방ㆍ관리 프로그램을 개발한다’ 이것은 사실 상상을 초월하는 엄청난 일이거든요. 전 세계 모든 사이언티스트가 달려서 목매달아도 지금 이게 해결이 안 되는데 이런 걸 목표로 삼으셨어요.  그리고 예산이 굉장히 많거든요 다른 데 예산에 비해서. 450 거의 445억이 되는데 이 기관의 목표가 국민 건강 증진이잖아요?\"\n한국한의학연구원장 최승훈] \"예.\"\n박인숙 위원] \"그런데 국민 건강 증진을 하려면 뭔가 실용적인 파이널 프로덕트가 나와야 되고 그전에 특허가 있어야 되고 그전에 논문이 있어야 되고 그전에 연구를 해야 되잖아요?\"\n한국한의학연구원장 최승훈] \"예 그렇습니다.\"\n박인숙 위원] \"그런데 연구 실적을 보면 SEI 논문 그러니까 논문하고 특허만 제가 말씀드리겠습니다 논문 숫자로 보면 해마다 64에서 77개를 냈는데 448억을 쓰면 연구 논문마다 6억 내지 7억의 비싼 논문인 것이거든요.   그런데 보통 과학계에서 연구비를 보면 논문 하나 내는데 많아야 2000 3000 5000만 원 이 정도가 주로 맥시멈인데 물론 다른 일도 하시지만 그것에 대해서 어떻게 생각하시는지 말씀해 주시지요.'
mecab = Mecab(dicpath=r'C:\mecab\mecab-ko-dic')

stop_words = ['위원장', '위원', '선배', '저', '우리', '위', '가지', '안녕하십니까', '여러', '위해', '못', '것', '사실', '말씀', '이후', '만약', '원장',
              '이전', '마지막', '최소한', '생각', '사이', '그때', '해당', '결정', '장관', '오랫', '최선', '적극', '검토', '사항', '최근', '추구', '나중',
              '그동안', '관련', '당부', '감사', '의견', '자료', '보고', '업무', '요청', '질의', '수고', '응답', '발언', '결국', '이외', '상황', '다음',
              '생각', '이틀', '사장', '대답', '장관']
stop_names = ['강창순', '유기홍', '박성호', '유성엽', '유은혜', '정진후', '박홍근', '박윤원', '이주호', '김상희', '박혜자', '신학용', '이에리사', '최승훈', '박인숙',
              '현영희', '강은희', '민병주', '김균섭', '김태년', '정세균', '서남수', '이동환']

stop_list = stop_words + stop_names

# 네트워크 그래프를 위한 사전 작업
def return_word(text_list, stop_words=None):
    global stop_list

    if stop_words != None:
        stop_list = stop_list + stop_words

    trim_list = []

    for text in text_list:
        doc = text['context']

        word_list = []

        out = mecab.pos(doc)

        for index, word in enumerate(out):
            if word[1] == 'NNG' or word[1] == 'NNP':
                try:
                    if out[index + 1][1] == 'XSN':
                        word_list.append(word[0] + out[index + 1][0])
                    else:
                        word_list.append(word[0])
                except IndexError as e:
                    print(e)
                    word_list.append(word[0])

        trim_list.append(word_list)

    return trim_list

def return_keyword(doc, stop_words=None):
    global stop_list
    out = mecab.pos(doc)

    key_list = {}

    if stop_words != None:
        stop_list = stop_list + stop_words

    noun_list = []

    for index, word in enumerate(out):
        if word[1] == 'NNG' or word[1] == 'NNP':
            try:
                if out[index + 1][1] == 'XSN':
                    noun_list.append(word[0] + out[index + 1][0])
                else:
                    noun_list.append(word[0])
            except IndexError as e:
                print(e)
                noun_list.append(word[0])

    noun_list = [noun for noun in noun_list if len(noun) > 1]

    result = [word for word in noun_list if not word in stop_list]

    # 명사 빈도 카운트
    count = Counter(result)

    common_list = count.most_common(10)

    # 불용어 제거
    tokenized_data = []

     # 불용어 제거
    tokenized_data.append(result)

    # vector_size : 만들어질 워드 벡터의 차원
    # 주로 100~300 사용
    # window : 컨텍스트 윈도우의 크기. 컨텍스트 윈도우는 단어 앞과 뒤에서 몇개 단어를 볼것인지를 정하는 크기이다.
    # min_count = 단어 최소 빈도수의 임계치(이 임계치보다 적은 단어는 훈련시키지 않는다.)
    # 문장내에서 단어 개수가 최소 몇번 나와야만 학습한다는 뜻
    # workers = 학습에 이용하는 프로세스의 갯수
    # sg = 0 일 경우, CBOW, 1 일 경우 Skip-gram
    # seed 고정시 결과 같음

    try:
        model = Word2Vec(sentences = tokenized_data, vector_size = 300, window = 5, min_count = 2, workers = 4, sg = 1)
    except:
        print('word2vec error 에러')
        model = Word2Vec(sentences=tokenized_data, vector_size=300, window=5, min_count=1, workers=4, sg=1)

    model.build_vocab(tokenized_data)

    # 빈도수 높은 2개의 단어에 해당 단어와 유사한 단어를 붙여서 키워드 추출
    try:
        for com in common_list[:2]:
            sim_list = model.wv.most_similar(com[0], topn=20)
            temp_list = []
            for sim in sim_list:
                if (sim[1] > 0):
                    temp_list.append(str(com[0] + ' ' + sim[0]))

            key_list[com[0]] = temp_list
    except KeyError:
        print('키에러')

    return key_list

# key_list = return_keyword(doc, stop_list)
# print(key_list)