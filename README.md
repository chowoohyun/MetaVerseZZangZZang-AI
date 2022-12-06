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
- 주목하고 있는 문자색을 바꿔서 눈에 띄도록 설정

![스크린샷_20221130_013322](https://user-images.githubusercontent.com/67001050/205871736-f7af87f8-5a21-4e7a-9496-727a77feff3c.png)


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

![스크린샷_20221201_022349](https://user-images.githubusercontent.com/67001050/205871871-3372ed1c-bb0c-47a3-b22b-af2bd8b770b5.png)

![스크린샷_20221201_022618](https://user-images.githubusercontent.com/67001050/205871932-fc94b001-ddaa-4f3c-8abc-a43e2d152e9f.png)

![스크린샷_20221201_023346](https://user-images.githubusercontent.com/67001050/205871972-b8d0c698-f8aa-4c0f-a7c2-543483e552b3.png)

![스크린샷_20221201_023711](https://user-images.githubusercontent.com/67001050/205872052-c9fb5c57-327c-4406-8c0e-f5a6359356a5.png)

![스크린샷_20221201_023954](https://user-images.githubusercontent.com/67001050/205872072-fe7973fc-ed4e-49a3-b744-f0a9d9a0d148.png)

![스크린샷_20221201_024047](https://user-images.githubusercontent.com/67001050/205872079-4500d0e6-ac47-41e8-b3c1-848673bc1936.png)








