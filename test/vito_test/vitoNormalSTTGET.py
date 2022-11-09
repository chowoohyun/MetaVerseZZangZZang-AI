import requests
from AI import vitoToken
from AI import vitoNormalSTTPOST
import time

def getSTT(filepath):
    transcribe_id = vitoNormalSTTPOST.postSTT(voice_filepath=filepath)
    n_time = time.time()

    while True:
        resp = requests.get(
            'https://openapi.vito.ai/v1/transcribe/'+transcribe_id['id'],
            headers={'Authorization': 'bearer ' + vitoToken.vitoToken()},
        )
        resp.raise_for_status()
        # print(resp.json())
        all_text = []
        try:
            for x in resp.json()['results']['utterances']:
                all_text.append(x['msg'])
        except:
            continue
        if resp.json()['status'] == 'completed':
            break
        time.sleep(0.3)

    # print(' '.join(all_text))
    # print(time.time()-n_time)

    return all_text

# sample
#getSTT("C:\\Users\\HP\\Videos\\EaseUS RecExperts\\20221012_165907.mp3")