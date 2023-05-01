from.import views
from django.urls import path
app_name='app2'
urlpatterns=[path('html',views.htmldisplay),
             path('xml',views.xmldisplay),
             path('excel',views.exceldisplay),

]