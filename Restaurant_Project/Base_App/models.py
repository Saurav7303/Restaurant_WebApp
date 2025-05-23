from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_Name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.Category_Name
    
    
class Items(models.Model):
    Item_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')
        
    def __str__(self):
        return self.Item_name
    
    
class AboutUs(models.Model):
    Description = models.TextField(blank=False)
    
class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_Person = models.IntegerField()
    booking_date = models.DateField()