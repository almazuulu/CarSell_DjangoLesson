from django.db import models
import uuid

class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=False, editable=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False, verbose_name='Second name')
    designation = models.CharField(max_length=255, null=False)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', null=True)
    facebook_link = models.URLField(max_length=255, blank=True, verbose_name='Social Facebook')
    twitter_link = models.URLField(max_length=255, blank=True)
    whatsapp_link = models.URLField(max_length=255, blank=True)
    telegram_link = models.URLField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
    
    
    
    
    


