import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key= os.environ.get('SENDGRID_API_KEY'))

from_email = Email("Tarun.kaushik@prepladder.com")
to_email = To("Tarunkaushik.prepladder@gmail.com")
subject = "Sendgrid is fun"
content = Content("text/plain", "Easy to send email through python")
mail = Mail(from_email, to_email, subject, content)

mail_json = mail.get()

response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)

