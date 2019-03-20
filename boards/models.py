from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.


def board_image_path(instance,filename):
    return f'boards/{instance.pk}/images/{filename}'
    
    
class Board(models.Model):
    title = models.CharField(max_length = 30)
    content =models.TextField()
    
    image = ProcessedImageField(
        upload_to = board_image_path,
        processors = [ResizeToFill(200,300)],
        format = 'JPEG', 
        options = {'quality':90},
        )
        
        
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f"{self.id}: {self.title}"
        
        
class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.content
        