from datetime import time

from django.db import models

# Create your models here.

class user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    sex = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:  # 设置要存储的数据库名称,默认按照父类的名称创建
        db_table = 'user'

