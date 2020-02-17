from django.contrib import admin
from .models import Card

admin.site.register(Card)

class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'bank', 'bn') #카드명, 카드사명, 혜택코드 보이기

