import fitz

def parse_chase_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return {
        "bankname": "chase",
        "text": text
    }