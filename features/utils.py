from django.conf import settings
from mailjet_rest import Client

def send_mailjet_email(subject, html_content, to_email):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_API_SECRET))
    data = {
        'FromEmail': 'prabhpuran@gmail.com',
        'FromName': 'Hopeline',
        'Subject': subject,
        'Html-part': html_content,
        'Recipients': [{'Email': to_email}],
    }
    result = mailjet.send.create(data=data)
    return result
