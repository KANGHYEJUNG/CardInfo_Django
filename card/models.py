from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=30) #카드명
    bank = models.CharField(max_length=20) #카드사명
    af = models.CharField(max_length=10) #연회비(annual_fee) / 우선생략
    benefit = models.TextField() #혜택 나열
    bn = models.CharField(max_length=15) #혜택 코드

    class Meta:
        ordering = ['bank', 'name'] #정렬

    def __str__(self): #문자열화 해주는 함수
        return self.name