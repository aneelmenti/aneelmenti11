from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
data="""<table>
<tr><th>pname</th><th>pid</th><th>pcost</th></tr>
<tr><th>DUKE</th><th>9999</th><th>250000</th></tr>
<tr><th>PULSAR</th><th>8888</th><th>200000</th></tr>
<tr><th>ROYALENFIELD</th><th>0009</th><th>350000</th></tr>
</table>"""
def htmldisplay(request):
    return HttpResponse(data,content_type="text/html")
def xmldisplay(request):
    return HttpResponse(data,content_type="application/xml")
def exceldisplay(request):
    return HttpResponse(data,content_type="application/vnd.ms-excel")
