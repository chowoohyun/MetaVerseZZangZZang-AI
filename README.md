# AI

## STT (Speech to Text)

- vito api, google api, clova api
  - 셋중 vito로 사용하기로함, 가성비가 좋으며, 우선적으로 무료이고, 구어체 학습모델이라 회의 내용을 잘 받아준다.
- AI hub에서 회의 데이터 수집
  - https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=132
- Kospeech 패키지를 통해 모델 학습
  - https://github.com/sooftware/kospeech
- 전이학습 진행
  - https://velog.io/@letgodchan0/음성인식-한국어-STT-1

## Data analysis

- 네이버 (블로그, 카페) 크롤링 진행
- 약 1만건의 본문을 스크랩 후 정규화 & 토큰화 진행
- 출현 빈도수에 비례하여 단어가 커지도록 설계

## NLP (Natural Language Processing)

- KoNLP를 활용하여 회의중 나온 문장에서 단어들을 추출해냄
  - https://konlpy-ko.readthedocs.io/ko/v0.4.3/
- word2vec을 계산하여 중요도가 높은 단어를 추출
- 추출된 단어들을 검색하여 다양한 정보를 유저에게 제공

## NLU (Natural Language Understanding)

## make a text

- LSTM 모델을 활용하여 자연스러운 문장을 생성해줌
  - https://soki.tistory.com/46

## Text summarization

- 이미 학습된 패키지를 활용하여 진행
  - https://huggingface.co/lcw99/t5-base-korean-text-summary
- clova api를 활용하여 축약된 정보를 제공하기도 함 ( 하지만 유로임.. )
  - https://www.ncloud.com/product/aiService/clovaSummary


![KakaoTalk_20221129_172612503](https://user-images.githubusercontent.com/67001050/205871364-2640cd7d-c8bd-4928-b513-a0ed5b9e0310.png)
