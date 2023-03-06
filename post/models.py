from django.db import models
from base import models as BaseModels

class Post(BaseModels.BaseModel):
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return f'{ self.id } { self.title }'
