from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings                                                                                                                                                      
from django.http import HttpResponse
from .utils import send_mailjet_email
from django.http import JsonResponse

def broadcast_sms(request):
    message_to_broadcast = ("Thanks for using hopeline. We are glad to have you.")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        print(recipient)
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!" + message_to_broadcast, 200)

def send_email_view(request):
    subject = "Emergency!"
    html_content = "<h1>We are from Hopeline</h1><p>We are here for your convenience.</p>"
    to_email = "sanchitamahajan11@gmail.com"
    response = send_mailjet_email(subject, html_content, to_email)

    if response.status_code == 200:
        return JsonResponse({"message": "Email sent successfully"}, safe=False)
    else:
        return JsonResponse({"error": response.text}, safe=False)

    return JsonResponse(response, safe=False)


