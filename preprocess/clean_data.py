import html2text

def strip_html(html_docs):
    for doc in html_docs:
        doc.page_content = html2text.html2text(doc.page_content)
    return html_docs