from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
data="""<table>
<tr><th>pname</th><th>pid</th><th>pcost</th></tr>
<tr><td>shirts</td><td>012></td><td>999</td></tr>
<tr><td>jeans</td><td>55</td><td>2500</td></tr>
<tr><td>shooes</td><td>66</td><td>1500</td></tr>
</table>"""
def htmldisplay(request):
    return HttpResponse(data,content_type="text/html")
def xmldisplay(request):
    return HttpResponse(data,content_type="application/xml")
def exceldisplay(request):
    return HttpResponse(data,content_type="application/vnd.ms-excel")

