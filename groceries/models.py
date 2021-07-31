from django.db import models

# Create your models here.
class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class groceryItems(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    unit=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    image=models.ImageField(upload_to="groceries/images",max_length=255)
    slug=models.SlugField(max_length=200)

    def __str__(self):
        return self.name

    # @staticmethod
    # def get_all_products():
    #     return