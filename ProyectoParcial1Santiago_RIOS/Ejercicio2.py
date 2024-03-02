import rsa
import PyPDF2
from io import BytesIO

# Generate RSA key pair (adjust key size as needed)
(publickey, privatekey) = rsa.newkeys(2048)

def sign_pdf(pdf_path, private_key):

    with open(pdf_path, 'rb') as file:
        pdf_bytes = file.read()

    with BytesIO(pdf_bytes) as buffer:
        pdf_bytes = buffer.read()
        pdf_reader = PyPDF2.PdfReader(pdf_bytes)


 
    try:
        document_title = pdf_reader.metadata['Title']
        hash_data = bytes(document_title, 'utf-8')
    except KeyError:
        print("Warning: 'Title' key not found in PDF metadata. Using empty hash data.")
        hash_data = b''

    hash = rsa.compute_hash(hash_data, 'SHA-1')  

    signature = rsa.sign_hash(hash, private_key, 'SHA-1')

    # Add the signature to the PDF metadata 
    if hasattr(pdf_reader, 'copy'): 
        pdf_with_sig = pdf_reader.copy()
        pdf_with_sig.addMetadata({'/DocMDP': rsa.pkcs1.encode(signature, 'PEM')})
    else:  
        pdf_reader.addMetadata({'/DocMDP': rsa.pkcs1.encode(signature, 'PEM')})

    
    with open('signed_document.pdf', 'wb') as file:
        if hasattr(pdf_with_sig, 'write'):  
            pdf_with_sig.write(file)
        else:  
            pdf_reader.write(file)

    return pdf_bytes  

if __name__ == '__main__':
    pdf_path = 'C:/Users/Santy/Downloads/NDA.pdf'  
    signed_pdf_content = sign_pdf(pdf_path, privatekey)

    print("Signed PDF saved successfully!")
