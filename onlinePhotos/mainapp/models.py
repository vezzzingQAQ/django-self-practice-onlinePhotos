from django.db import models
from datetime import datetime
# Create your models here.
class Photos(models.Model):
    #主键id可以省略不写
    title=models.CharField(max_length=20)
    about=models.CharField(max_length=255)#默认值
    fileName=models.CharField(max_length=100)
    time=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table="photoslist"
