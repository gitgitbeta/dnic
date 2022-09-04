from django.contrib import admin

# Register your models here.
from .models import Korisnik, Lectures, Question, Tests


class KorisnikAdmin(admin.ModelAdmin):
    pass
admin.site.register(Korisnik,KorisnikAdmin)

class LecturesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Lectures,LecturesAdmin)

class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question,QuestionAdmin)

class TestsAdmin(admin.ModelAdmin):
    list_display = ("title",)
admin.site.register(Tests,TestsAdmin)


