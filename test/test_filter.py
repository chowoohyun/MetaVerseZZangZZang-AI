from transformers import TextClassificationPipeline, BertForSequenceClassification, AutoTokenizer

model_name = 'smilegate-ai/kor_unsmile'

model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    device=-1,     # cpu: -1, gpu: gpu number
    # return_all_scores=True,
    top_k=10,
    function_to_apply='sigmoid'
)

# 확률 높은 순이므로 처음 나온 게 가장 유력함
# 리스트(dict) 형태


def return_filter(doc):
    result = pipe(doc)[0][:]
    return result


result = return_filter('이놈자식이?')
print(result)
