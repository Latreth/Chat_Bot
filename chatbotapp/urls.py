from django.urls import path
from django.conf.urls import url, include


from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^prueba/$',views.prueba,name='prueba'),
	url(r'^api/$',views.chat_api,name='chat_api'),
	url(r'^chat/', include('djangoChat.urls')),
]