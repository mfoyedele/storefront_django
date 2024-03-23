from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from tags.models import TaggedItem


# Register your models here.
class TagInLine(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem