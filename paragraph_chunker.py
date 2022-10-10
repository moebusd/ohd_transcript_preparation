def paragraph_chunker(text, nr_sentences):

    from odf.opendocument import OpenDocumentText
    from odf.text import P

    # odt schreiben
    doc_out = OpenDocumentText()
    # text_out = ''
    for line in text_processed_final.splitlines():
        doc_out.text.addElement(P(text=line))
    # doc_out.text.addElement(text_out)
        doc_out.save(destination + source.split('\\')[-1].split('.')[0] + '_' + source.split('.')[1] + '_processed.odt')