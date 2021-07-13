from django.contrib import admin
from .models import Question, Answer, Game
# Register your models here.


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'numberOfAnswers', 'points',)
    list_display_links = ( 'id',)
    list_editable = ('title','numberOfAnswers', 'points',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id','title','correct')
    list_display_links = ('id',)
    list_editable = ('title', 'correct',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id',)
    list_editable = ('title', )


admin.site.register(Question,QuestionsAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Game, GameAdmin)
