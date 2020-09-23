
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='malliksiddharth@gmail.com',
    to_emails='souravmohanty0077@gmail.com',
    subject='Welcome to my world',
    html_content='<strong>Hi,sourav how are you</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    """print(e.message)"""
    print("ERROR: PC LOAD LETTER")



"""
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
from_email = Email("malliksiddharth@gmail.com")
to_email = To("souravmohanty0077@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
"""

"""
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": "souravmohanty0077@gmail.com"
        }
      ],
      "subject": "Sending with SendGrid is Fun"
    }
  ],
  "from": {
    "email": "malliksiddharth@gmail.com"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "and easy to do anywhere, even with Python"
    }
  ]
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)
"""

"""
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
response = sg.client.suppression.bounces.get()
print(response.status_code)
print(response.body)
print(response.headers)
"""

"""
import sendgrid
import os

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('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'))
response = sg.client._("suppression/bounces").get()
print(response.status_code)
print(response.body)
print(response.headers)
"""

"""
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='malliksiddharth@gmail.com',
    to_emails='souravmohanty0077@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='and easy to do anywhere, even with Python')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

"""