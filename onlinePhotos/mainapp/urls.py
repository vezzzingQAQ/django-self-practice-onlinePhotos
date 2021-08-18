from django.urls import path
from mainapp import views

urlpatterns=[
    path("index/<int:currentPage>",views.indexPhotos,name="indexphotos"),
    path("addPhotoPage",views.addPhotoPage,name="addphotopage"),
    path("addPhoto",views.addPhoto,name="addphoto"),
]