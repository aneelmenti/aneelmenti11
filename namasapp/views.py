from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
data="""<table>
<tr><th>pname</th><th>pid</th><th>cost</th></tr>
<tr><td>BMW</td><td>1111</td><td>50000000</td></tr>
<tr><td>AUDI</td><td>2222</td><td>70000000</td></tr>
<tr><td>BENZ</td><td>3333</td><td>90000000</td></tr>
</table>"""
def htmldisplay(request):
    return HttpResponse(data,content_type="text/html")
def xmldisplay(request):
    return HttpResponse(data,content_type="application/xml")
def exceldisplay(request):
    return HttpResponse(data,content_type="application/vnd.ms-excel")
