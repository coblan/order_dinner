from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
from helpers.director.model_func.cus_fields.jsonable import JsonAbleField
# Create your models here.
class ResourceType(models.Model):
    label = models.CharField('原料名称',max_length=200,)
    amount = models.FloatField('剩余总量',default=0)
    
    def __str__(self):
        return self.label

class Dish(models.Model):
    label = models.CharField('菜名称',max_length=200,)
    cover =  PictureField('封面',max_length = 300,)
    
    def __str__(self):
        return self.label

class DishRes(models.Model):
    dish = models.ForeignKey(Dish)
    res = models.ForeignKey(ResourceType)
    amount = models.FloatField('消耗量',default=0)
 
    
    
    

