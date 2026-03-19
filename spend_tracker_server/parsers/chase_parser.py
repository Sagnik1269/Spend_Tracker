import fitz
import re

def parse_chase_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    

    doc.close()

    text_list = text.split("ACCOUNT ACTIVITY")

    print(text_list)

    transactions = text_list[1].split("Date of\nTransaction\nMerchant  Name or Transaction Description\n$ Amount\n")

    transactions_list = transactions[1].split("\n")

    transactions_list = [item.strip() for item in transactions_list]

    transactions_array = []
    
    i=0

    while (i < len(transactions_list)):
        
        if bool(re.match(r'^\d{2}/\d{2}$', (transactions_list[i]))):
            transactions_array.append([transactions_list[i], transactions_list[i+1], transactions_list[i+2]])
            i+=3
        else:
            i+=1
    
    print(len(transactions_array))

    return {
        "bankname": "chase",
        "text": transactions_array
    }