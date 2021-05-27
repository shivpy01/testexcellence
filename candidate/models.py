from django.db import models

# Create your models here.

class  candidate(models.Model):
    name = models.CharField(max_length= 50)
    email = models.CharField(max_length= 50)

class test_score(models.Model):
    name = models.CharField(max_length= 50)
    first_round = models.IntegerField()
    second_round = models.IntegerField()
    third_round = models.IntegerField()
    
    def total(self):
        return self.first_round+self.second_round+self.third_round, self.total()/3
