from django.db import models
from django.urls import reverse

# Create your models here.

class District(models.Model):
    name = models.CharField("乡镇",max_length=20)
    schools = models.IntegerField(verbose_name="学校数")
    geo_l = models.FloatField(verbose_name="经度")
    geo_d = models.FloatField(verbose_name="维度")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_school',kwargs={"pk":self.pk})

class School(models.Model):
    name = models.CharField("学校名称",max_length=50)
    district = models.ForeignKey(District,verbose_name="所属乡镇",on_delete=None)
    students = models.IntegerField(verbose_name="学生人数")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_school',kwargs={"pk":self.pk})


class Food_Struct(models.Model):
    name = models.ForeignKey(School,verbose_name="学校名称",null=True,on_delete=None)
    rice = models.FloatField("大米",default=0,null=True)
    ganhuo = models.FloatField("干货",default=0,null=True)
    cake = models.FloatField("糕点",default=0,null=True)
    egg = models.FloatField("蛋类",default=0,null=True)
    chicken = models.FloatField("鸡鸭肉",default=0,null=True)
    ricenoodle = models.FloatField("米粉",default=0,null=True)
    milk = models.FloatField("奶制品",default=0,null=True)
    beef = models.FloatField("牛肉",default=0,null=True)
    oil = models.FloatField("食用油",default=0,null=True)
    vegitable = models.FloatField("蔬菜",default=0,null=True)
    flavor = models.FloatField("调味品",default=0,null=True)
    pock = models.FloatField("猪肉",default=0,null=True)
    total = models.FloatField("总计",default=0,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myechart',kwargs={"pk":self.pk})

class Nutri_of_Food(models.Model):
    school = models.ForeignKey(School,on_delete=None,verbose_name="学校名称",null=True)
    xuqin = models.FloatField(verbose_name="畜禽肉",null=True)
    fish = models.FloatField(verbose_name="鱼虾",null=True)
    soilbean = models.FloatField(verbose_name="大豆坚果",null=True)
    egg = models.FloatField(verbose_name="蛋类",null=True)
    gushu = models.FloatField(verbose_name="谷薯类", null=True)
    milk = models.FloatField(verbose_name="奶制品",null=True)
    sault = models.FloatField(verbose_name="盐",null=True)
    vigetable = models.FloatField(verbose_name="蔬菜类",null=True)
    fruit = models.FloatField(verbose_name="水果类",null=True)
    oil = models.FloatField(verbose_name="食用油",null=True)
    total = models.FloatField(verbose_name="合计",null=True)

    def get_absolute_url(self):
        return reverse('myechart', kwargs={"pk": self.pk})

