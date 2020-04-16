from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
from helpers.director.model_func.cus_fields.jsonable import JsonAbleField
# Create your models here.
class ResourceType(models.Model):
    label = models.CharField('原料名称',max_length=200,)
    amount = models.FloatField('剩余总量',default=0)
    unit = models.CharField('单位',max_length=50,blank=True)
    
    def __str__(self):
        return self.label

DISH_KIND = (
    (0,'未分类'),
    (1,'热菜'),
    (2,'冷菜'),
    (3,'汤'),
    (4,'酒水'),
    (5,'小吃'),
)

class Dish(models.Model):
    label = models.CharField('菜名称',max_length=200,)
    cover =  PictureField('封面',max_length = 300,)
    title = models.CharField('标题',max_length=300,blank=True)
    dsp = models.TextField('描述',blank=True)
    price = models.DecimalField('价格',max_digits=10,decimal_places=2,default=0)
    kind = models.IntegerField('种类',default=0,choices=DISH_KIND)
    key_word = models.CharField('关键字',max_length=300,blank=True)
    
    def __str__(self):
        return self.label

class DishRes(models.Model):
    dish = models.ForeignKey(Dish)
    res = models.ForeignKey(ResourceType)
    amount = models.FloatField('消耗量',default=0)
    
class KeyWord(models.Model):
    content = models.CharField('关键字',max_length=50)
    
 
    
    
    

