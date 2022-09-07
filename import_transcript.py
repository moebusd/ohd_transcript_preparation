### Dateiformat erkennen und Datei importieren


def import_transcript(transcript):
    import win32com.client as win32
    import docx2txt
    from odf.opendocument import load as load_odf
    from odf import text as odf_text, teletype

    if transcript.endswith('.doc'):
        doc = win32.GetObject(transcript)
        text = doc.Range().Text
        return text

    if transcript.endswith('.docx'):
        text = docx2txt.process(transcript)
        return text

    if transcript.endswith('.odt'):
        text = load_odf(transcript)
        #print(text[:99])
        allparas = text.getElementsByType(odf_text.P)
        text = ''
        for i in range(len((allparas))):
            text = text + teletype.extractText(allparas[i]) + '\n'
        return text

    if transcript.endswith('txt'):
        try:
            text = open(transcript, 'r', encoding='UTF-8-sig').read()
            return text

        except UnicodeDecodeError:
            try:
                text = open(transcript, 'r', encoding='UTF-8').read()
                return text

            except UnicodeDecodeError:
                try:
                    text = open(transcript, 'r', encoding='UTF-16-le').read()
                    return text

                except UnicodeDecodeError:
                    try:
                        text = open(transcript, 'r', encoding='UTF-16-be').read()
                        return text

                    except UnicodeDecodeError:
                        text = open(transcript, 'r', encoding='ANSI').read()
                        text = text.encode('UTF-8')
                        text = text.decode('UTF-8', 'ignore')
                        return text

    else:
        return 'Kein kompatibles Dateiformat'