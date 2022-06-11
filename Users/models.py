# Create your models here.
from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


# 擴充 django User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    # 模型類中設定:blank=True,表示程式碼中建立資料庫記錄時該欄位可傳空白(空串,空字串)
    address = models.CharField('地址', max_length=100, blank=True)
    phone = models.IntegerField('電話', max_length=10, blank=True)
    tax_id = models.IntegerField('統一編號', validators=[MaxValueValidator(99999999)], default=0)
    estimate_tester = models.IntegerField('預計測試人員數量', default=1)
    actual_tester = models.IntegerField('實際測試人員數量', default=1)
    estimate_viewer = models.IntegerField('預計閱覽人員數量', default=0)
    actual_viewer = models.IntegerField('實際閱覽人員數量', default=1)
    allow_project  = models.IntegerField('allow_project', default=1)
    allow_group = models.IntegerField('allow_group', default=1)
    allow_case_per_group = models.IntegerField('allow_case_per_group', default=50)
    allow_run = models.IntegerField('allow_run', default=1)
    account_type = models.IntegerField('1 組織； 0, 個人', default=1)


    class Meta:
        verbose_name = 'User profile'

    def __str__(self):
        return "{}".format(self.user.__str__())

class ProjectTable(models.Model):
    account_id = models.BigIntegerField('id')
    project_name = models.CharField('project_name', max_length=50, default="default")
    description = models.TextField('description', blank=True)
    color = models.TextField('project_name', blank=True)
    create_datetime = models.DateTimeField('create_datetime', default=datetime.now)
    creator = models.CharField('creator', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Project table'

    def __str__(self):
        return "{}".format(self.account_id.__str__())
