def generate_email_html(user_name, content_block):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Template</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}
            .container {{
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .content-block {{
                padding: 20px;
                background-color: #e6f7ff; /* Very light blue */
                border-radius: 5px;
                margin-bottom: 20px;
            }}
            .content-block h2 {{
                color: #333333;
            }}
            .content-block p {{
                color: #555555;
                line-height: 1.6;
            }}
            .thank-you-note {{
                padding: 20px;
                color: #333333;
                text-align: left;
                font-size: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Welcome and Greeting Section -->
            <div class="content-block">
                <h2>Welcome!</h2>
                <p>
                    Dear {user_name},
                </p>
                <p>
                    We are delighted to welcome you to our community! Our team is excited to help you get the most out of our services.
                </p>
               
                <div>
                    {content_block}
                </div>

            </div>

          

           

            <!-- Thank You Note -->
            <div class="thank-you-note">
                <p>Thank you,</p>
                <p>James Smith</p>
                <p>Demo Corp, Inc</p>
                <p>1234 Elm Street, Suite 5678</p>
                <p>Metropolis, NY 10101</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content
