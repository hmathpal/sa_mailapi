def generate_email_html(user_name, img_url, content_block_1, content_block_2, content_block_3):
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
                max-width: 700px;  /* Increased width */
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background-color: #003366; /* Navy Blue */
                padding: 10px 0;
                text-align: center;
                color: white;
                font-size: 24px;
                border-radius: 5px 5px 0 0;
            }}
            .content-block {{
                padding: 20px;
                background-color: #f1f3f5; /* Very Very Light Slate */
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
            .cta-button {{
                display: block;
                width: 150px;
                margin: 20px auto;
                padding: 10px;
                background-color: #003366; /* Navy Blue */
                color: white;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
            }}
            .thank-you-note {{
                padding: 20px;
                color: #333333;
                text-align: left;
                font-size: 16px;
            }}
            .footer {{
                background-color: #333333; /* Dark Gray */
                padding: 10px 0;
                text-align: center;
                color: white;
                font-size: 14px;
                border-radius: 0 0 5px 5px;
            }}
            .image-block {{
                text-align: center;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header Section -->
            <div class="header">
                OmniBrief Assistant
            </div>

            <!-- Content Section -->
            <div class="content-block">
               <!-- Image Section -->
                <div class="image-block">
                    <img src="{img_url}" alt="Descriptive Alt Text"  width="660" style="display:block;"> <!-- Adjusted image width -->
                 
                    

                </div>

                <p>
                    Hi {user_name},
                </p>
                <div>
                    {content_block_1}
                </div>
                
                

              
                <div>
                    {content_block_2}
                </div>

                <div>
                    {content_block_3}
                </div>


                 <!-- Thank You Note -->
            <div class="thank-you-note">
                <p><b>Thank you</b>,</p>
                <p>Omnibrief Assistant | Sales Consultant</p>
                <p>DemoPharma, Inc</p>
                <p>Phone: +1 416-908-9876</p>
            </div>
            </div>

          

           

            <!-- Footer Section -->
            <div class="footer">
                &copy; 2024 DemoPharma, Inc. All rights reserved.
                <br>
                1234 Elm Street, Suite 5678, Metropolis, NY 10101
            </div>
        </div>
    </body>
    </html>
    """
    return html_content
