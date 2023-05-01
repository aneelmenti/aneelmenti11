from.import views
from django.urls import path
app_name='namasapp'
urlpatterns=[path('html',views.htmldisplay),
             path('xml',views.xmldisplay),
             path('excel',views.exceldisplay),
]