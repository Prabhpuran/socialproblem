from django.urls import path                                                                                                                                                        
from . import views

urlpatterns = [
   path('broadcast/', views.broadcast_sms, name="broadcast"),
   path('send-email/', views.send_email_view, name="send_email"),
   path('post-tweet/', views.tweet_view, name="post_tweet"),
]