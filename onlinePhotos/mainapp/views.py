from django.shortcuts import render
from mainapp.models import Photos

from django.http import HttpResponse

from PIL import Image

import time,os

from django.core.paginator import Paginator

# Create your views here.
def indexPhotos(request,currentPage=1):
    try:
        ulist=Photos.objects.filter()
        p=Paginator(ulist,5)#5条数据一页
        #判断页码值是否有效
        if currentPage<1:
            currentPage=1
        if currentPage>p.num_pages:
            currentPage=p.num_pages
        #重新返回表格
        currentlist=p.page(currentPage)

        uploadContext={"photosList":currentlist,"currentPage":currentPage,"pagesList":p.page_range}
        return(render(request,"mainapp/index.html",uploadContext))#加载模板
    except:
        return(HttpResponse("没有找到信息(○´･д･)ﾉ"))

#添加照片页面
def addPhotoPage(request):
    return(render(request,"mainapp/add.html"))

#执行添加
#<form action="{% url 'insertphoto' %}" method="POST">
def addPhoto(request):
    try:
        ob=Photos()
        #从表单获取要添加的信息
        ob.title=request.POST['title']
        ob.about=request.POST['about']

        #图片操作*****************************************************
        myfile=request.FILES.get("pic",None)#上传的图片
        if not myfile:
            return(HttpResponse("没有上传的文件信息"))

        print(myfile)
        filename=str(time.time())+"."+myfile.name.split(".").pop()#随机时间戳+原来的后缀名
        destination=open("static/mainapp/pics/"+filename,"wb+")

        for chunk in myfile.chunks():#分块读取上传文件内容并写入目标文件
            destination.write(chunk)
        destination.close()

        #用Pillow实现图片自动缩放成75*75,也可以用来加水印
        im=Image.open("static/mainapp/pics/"+filename)
        im.thumbnail((75,75))
        im.save("static/mainapp/pics_sized/"+filename,None)

        #os.remove(...+filename)删除原图
        #图片操作*****************************************************

        ob.fileName=filename
        ob.save()
        uploadContext={"info":"添加成功"}
    except:
        uploadContext={"info":"添加失败"}
    return(render(request,"mainapp/info.html",uploadContext))
