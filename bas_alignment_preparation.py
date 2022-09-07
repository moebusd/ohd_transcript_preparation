def text_preparation(source, destination, text):
    import re
    import os
    from odf.opendocument import OpenDocumentText
    from odf.text import P
    ### Tabstops entfernen und Carriage Returns durch Line Feeds ersetzen
    text_1 = text.replace('\t', ' ').replace('\r', '\n')

    ### Überschüssige Zeilenumbrüche entfernen
    while ' \n' in text_1:
        text_1 = text_1.replace(' \n', '\n')
    while '\n\n' in text_1:
        text_1 = text_1.replace('\n\n', '\n')
    while '!!' in text_1:
        text_1 = text_1.replace('!!', '!')
    while '??' in text_1:
        text_1 = text_1.replace('??', '?')

    replace_list = [
        ('(', ' <'),
        (')', '> '),
        ('{[', ' <'),
        (']}', '> '),
        ('{', ' <'),
        ('}', '> '),
        ('[', ' <'),
        (']', '> '),
        (':\n', ' <:> .\n'),
        (',\n', ' <...> .\n'),
        ('<...>', '#***#'),
        ('...', '#***#'),
        ('..', '#***#'),
        ('. .', '#***#'),
        ('#***#', ' <...>')
    ]

    for repl in replace_list:
        text_1 = text_1.replace(repl[0],repl[1])

    while '  ' in text_1:
        text_1 = text_1.replace('  ', ' ')

    text_1 = text_1.replace(' \n', '\n')

    text_processed_final = ''

    for line in text_1.splitlines():
        if line.endswith('>') or line.endswith('>.'):
            text_processed_final = text_processed_final + line + ' .\n'
            continue
        if line.endswith('.') or line.endswith('!') or line.endswith('?'):
            text_processed_final = text_processed_final + line + '\n'
            continue
        else:
            text_processed_final = text_processed_final + line + '.\n'


    #text_processed = text_1
    #text_processed_1 = text_processed.replace('(', ' <').replace(')', '> ').replace('{[', '<').replace(']}', '>').replace('{', '<').replace('}', '>').replace('[', '<').replace(']', '>').replace('\n', '.\n').replace(':\n', '<:>.\n')
    #text_processed_2 = text_processed_1.replace('<...>', '#***#').replace('...', '#***#').replace('..', '#***#').replace('. .', '#***#')
    #text_processed_3 = text_processed_2.replace('#***#', '<...>')
    #print(text[:99])

    #text_processed_final = text_processed_3

    #odt schreiben
    doc_out = OpenDocumentText()
    #text_out = ''
    for line in text_processed_final.splitlines():
        doc_out.text.addElement(P(text=line))
    #doc_out.text.addElement(text_out)
    doc_out.save(destination+source.split('\\')[-1].split('.')[0] + '_' + source.split('.')[1] + '_processed.odt')
