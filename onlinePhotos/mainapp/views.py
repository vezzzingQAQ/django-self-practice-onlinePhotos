from django.shortcuts import render
from mainapp.models import Photos

from django.http import HttpResponse

# Create your views here.
def indexUsers(request):
    try:
        ulist=Photos.objects.all()
        uploadContext={"photosList":ulist}
        return(render(request,"mainapp/index.html",uploadContext))#加载模板
    except:
        return(HttpResponse("没有找到信息(○´･д･)ﾉ"))
