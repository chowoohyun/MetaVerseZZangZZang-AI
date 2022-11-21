import os
import glob
import shutil
#
# wav_list = glob.glob('./audio/*.wav')
#
# for wav in wav_list:
#     folder = '.'.join(wav.split('.')[0:-1])
#     os.mkdir(folder)
#     num = folder.split('\\')[-1]
#     #print('./audio/'+num+'/'+num+'.wav')
#     shutil.move(folder+'.wav', './audio/'+num+'/'+num+'.wav')
#     shutil.move(folder + '.txt', './audio/'+num+'/'+num+'.txt')


wav_list = glob.glob('./audio/*/*.wav')

with open('kospeech/dataset/kspon/train.txt', 'w') as f1:
    for wav in wav_list:
        filename = wav.split('\\')[-1]
        folder = '.'.join(wav.split('.')[0:-1])
        num = folder.split('\\')[-1]
        text = folder + '.txt'
        textfile = './audio/'+num+'/'+num+'.txt'
        audio_file = num+'/'+num+'.wav'
        line = ''
        with open(textfile, 'r', encoding='utf-8') as f2:
            line = f2.read()

        f1.write(audio_file + '\t' + line + '\n')

    f1.close()


