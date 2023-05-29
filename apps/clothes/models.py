from django.db import models
from django.utils.text import slugify
import uuid


class Cloth(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    article = models.CharField(max_length=20, blank=True, editable=False, unique=True)  # TODO: need to autogenerate it
    cloth_type = models.ForeignKey('ClothType', on_delete=models.CASCADE)
    suit = models.ForeignKey('Suit', on_delete=models.CASCADE)
    size = models.CharField(max_length=40)  # TODO: how to make it multichoice
    fabric_width = models.CharField(max_length=40)
    textile = models.CharField(max_length=100)
    dublerin_usage = models.CharField(max_length=100)
    flazelin_usage = models.CharField(max_length=100)
    actual_fabric_usage = models.CharField(max_length=100)
    lining = models.CharField(max_length=50)
    twist = models.CharField(max_length=20)
    technical_description = models.TextField()
    processing = models.TextField()
    furniture = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.article = self.generate_article()
        super(Cloth, self).save(*args, **kwargs)

    def generate_article(self):
        name_slug = slugify(self.name)
        id = str(self.id)[:5]
        return f'{name_slug}-{id}'
    
    
class ClothModelImage(models.Model):
    """Photo of model in cloth"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE, related_name='model_images')
    image = models.ImageField(upload_to='clothes_images/') #TODO: need to change folder to upload
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
                                        
                                        
class ClothSampleImage(models.Model):
    """Photo of sample of cloth"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE, related_name='sample_images')
    image = models.ImageField(upload_to='clothes_images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

class ClothType(models.Model):
    """Type of cloth"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class Suit(models.Model):
    """Suit of cloth"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)