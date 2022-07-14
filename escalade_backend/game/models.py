from django.db import models
# from .models import Team

# Create your models here.

class Question(models.Model):
    level = models.IntegerField()
    body = models.TextField()
    hint = models.TextField(null=True, default=None)
    ans = models.CharField(max_length=500)
    link1 = models.CharField(max_length=200, null=True, blank=True, default=None)
    link2 = models.CharField(max_length=200, null=True, blank=True, default=None)
    img = models.URLField(null=True, blank=True, default=None)
    def __str__(self):
        return str(self.id)

class Opposer(models.Model):
    boardNo = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()

class Booster(models.Model):
    boardNo = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()

# class board(models.Model):
#     boardNo=models.IntegerField()
#     snake=models.ForeignKey(boardSnake, on_delete=models.CASCADE, blank=True)
#     ladder=models.ForeignKey(boardLadder, on_delete=models.CASCADE, blank=True)

# class unsolvedQues(models.Model):
#     level1=models.CharField(max_length=50,default="01,02,03,04,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20") #remember to delete where snake head or ladder bottom is present
#     level2=models.CharField(max_length=50,default="21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40") #remember to delete where snake head or ladder bottom is present
#     level3=models.CharField(max_length=50,default="41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60") #remember to delete where snake head or ladder bottom is present
#     level4=models.CharField(max_length=50,default="61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80") #remember to delete where snake head or ladder bottom is present
#     team=models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)