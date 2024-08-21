from django.db import models
from django.utils.text import slugify
import uuid
# Create your models here.

class Catagory(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Enter a Catagory    ")
    slug = models.SlugField(unique=True, null=True, blank=True)
    is_active = models.BooleanField()
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = "Inventory Catagory"
        verbose_name_plural = "Catagories"
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, *kwargs)


class SeasonalEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length= 100)


class Product(models.Model):

    IN_STOCK = "IS"
    OUT_OF_STOCK = "OOS"
    BACKORDER = "BO"
    STOCK_STATUS = {
        IN_STOCK : "In stock",
        OUT_OF_STOCK : "Out of stock",
        BACKORDER : "Back order"
    }
    pid = models.CharField(max_length=250, null=False, blank=False)
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True, help_text="you can skip", null=True, blank= True)
    description = models.TextField(null=True)
    is_digital = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField()
    updates_at = models.DateTimeField(auto_now=True, editable=False)
    stoch_status = models.CharField(max_length=3, choices= STOCK_STATUS, default= OUT_OF_STOCK)
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, null=True)
    seasonal_event = models.ForeignKey(SeasonalEvents, on_delete=models.SET_NULL,null=True, blank= True)
    product_type = models.ManyToManyField('ProductType', related_name="product_type",null=True, blank= True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
class AttributeValue(models.Model):
    atttribute_value = models.CharField(max_length=100)
    attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=3)
    sku = models.UUIDField(default=uuid.uuid4)
    stock_qty = models.IntegerField()
    is_active = models.BooleanField(default=False)
    order = models.IntegerField()
    weight = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    attribute_value = models.ManyToManyField("AttributeValue", related_name="attribute_value")


class ProductImage(models.Model):
    name = models.CharField(max_length= 100)
    alternative_text = models.CharField(max_length= 100)
    url = models.ImageField()
    order = models.IntegerField()
    product_line = models.ForeignKey(ProductLine, on_delete= models.CASCADE)


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class ProductLine_AttributeValue(models.Model):
    attribute_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)


class Product_ProductType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)


class StockControl(models.Model):
    stock_qty = models.IntegerField()
    name = models.CharField(max_length=100)
    stock_product = models.OneToOneField(Product, on_delete=models.CASCADE)