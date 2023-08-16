from django.contrib import admin
from .models import Chat, MessageModel, GeneralTaskModel, PersonalTaskModel

# Register your models here.
admin.site.register(Chat)
admin.site.register(MessageModel)
admin.site.register(GeneralTaskModel)
admin.site.register(PersonalTaskModel)
