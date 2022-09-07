import os
from bas_alignment_preparation import text_preparation
from import_transcript import import_transcript

folder = 'C:\\Users\\moebusd\\sciebo\\Mining LUSIR\\Digital Archive Environment\\transcriptpreparation\\'

for file in os.listdir(folder):
    print(file)
    if file.endswith('.odt') or file.endswith('.doc') or file.endswith('.docx') or file.endswith('.txt'):
        text = import_transcript(folder+file)
        text_processed = text_preparation(folder+file, folder+'\\fertig\\', text)
        #out = open(folder + file.split('.')[0] + '_' + file.split('.')[1] + '_processed.txt', 'w', encoding='UTF-8')
        #out.write(text)
        #out.close()