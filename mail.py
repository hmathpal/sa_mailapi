import os
import requests
from dotenv import load_dotenv
from email_template import generate_email_html

# Load environment variables from .env file
load_dotenv()

def send_simple_message():
    content_block = "<p>This is the content block</p><p>It can be customized for each user. We can have sample content here coming from API</p>"
    html_content = generate_email_html("Sara", content_block)

    # Retrieve environment variables
    api_key = os.getenv('MAILGUN_API_KEY')
    domain = os.getenv('MAILGUN_DOMAIN')
    from_email = os.getenv('MAILGUN_FROM')
    to_email = os.getenv('MAILGUN_TO')

    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": from_email,
            "to": to_email,
            "text": "Testing some Mailgun awesomeness!",
            "html": html_content,
            "subject": "Hello"
        }
    )


# Example usage:
# response = send_simple_message()
# print(response.status_code)
# print(response.text)
