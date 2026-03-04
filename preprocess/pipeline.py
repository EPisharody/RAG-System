from ingest.load_data import load_documents
from preprocess.chunk_data import split_documents
from preprocess.clean_data import strip_html

def ingest():
    pdfs, textFiles, htmlFiles = load_documents() # load documents
    cleaned_html = strip_html(htmlFiles) # clean HTML files

    docs = []
    docs.extend(pdfs)
    docs.extend(textFiles)
    docs.extend(cleaned_html)

    docs = split_documents(docs)
    
    return docs