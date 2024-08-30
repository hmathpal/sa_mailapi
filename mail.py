import os
import requests
from dotenv import load_dotenv
from email_template import generate_email_html

# Load environment variables from .env file
load_dotenv()

def send_template_message(reciever_name,reciever_email, email_subject):

    # Retrieve environment variables
    api_key = os.getenv('MAILGUN_API_KEY')
    domain = os.getenv('MAILGUN_DOMAIN')
    from_email = os.getenv('MAILGUN_FROM')
    to_email = reciever_email
    content_block = "<h1>This is a test email</h1><p>Thanks for reading this email</p>"

    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
                "from": from_email,
                "to": to_email,
                "template": "template v1",
                "h:X-Mailgun-Variables": f'{{"reciever_name": "{reciever_name}","content_block" : "{content_block}"}}',
                "subject": email_subject
            }
    )


def send_simple_message(reciever_name,img_url, reciever_email, email_subject, content_block_1, content_block_2, content_block_3, attachment=None):


    print("We are here")
    html_content = generate_email_html(reciever_name, img_url,content_block_1,content_block_2,content_block_3)
   
    print("We are here after email")
     
  
    # Retrieve environment variables
    api_key = os.getenv('MAILGUN_API_KEY')
    domain = os.getenv('MAILGUN_DOMAIN')
    from_email = os.getenv('MAILGUN_FROM')
    to_email = reciever_email
   
    print("We are here after email api_key", api_key)

    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": from_email,
            "to": to_email,
            "text": "Testing some Mailgun awesomeness!",
            "html": html_content,
            "subject":email_subject
        }
    )


# Example usage:
# response = send_simple_message()
# print(response.status_code)
# print(response.text)
