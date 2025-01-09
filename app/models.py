from django.db import models




class Post(models.Model):
    title = models.CharField(max_length=255)  # String field
    content = models.TextField()  # Text field for large text
    published_date = models.DateTimeField(null=True, blank=True)  # Date/Time
    author = models.CharField(max_length=100)  # Author name
    is_published = models.BooleanField(default=False)  # Boolean field

    def __str__(self):
        return self.title



class Item(models.Model):
    item_name = models.CharField(max_length=255)  # Item name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item
    avl_qty = models.IntegerField()  # Available quantity of the item
    
    def __str__(self):
        return self.item_name  # Return the item name when the object is printed
