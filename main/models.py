from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 200)
    imgsrc = models.ImageField(default = 'https://placehold.it/500x500')

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
    blank = True, null = True)
    name = models.CharField(max_length = 200)
    imgsrc = models.ImageField(default = 'https://placehold.it/500x500')

    def __str__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length = 200)

class Attributeitem(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE,
    blank = True, null = True)
    name = models.CharField(max_length = 200)

class Product(models.Model):
    created = models.DateTimeField(editable=False, default = timezone.now())
    modified = models.DateTimeField(default = timezone.now())

    category = models.ForeignKey(Category, on_delete= models.CASCADE,
    blank = True, null = True)
    subcategory = models.ForeignKey(Subcategory, on_delete= models.CASCADE,
    blank = True, null = True)

    attributeitem = models.ManyToManyField(Attributeitem)

    name = models.CharField(max_length = 200)
    price = models.FloatField(default = None,
    blank = True, null = True)
    sale_price = models.FloatField(default = None,
    blank = True, null = True)
    imgsrc = models.ImageField(default = 'https://placehold.it/500x500')
    description = models.TextField()
    code = models.CharField(max_length = 200)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    def has_sale(self):
        if self.sale_price:
            return True
        else:
            return False
    def discount_perc(self):
            return int(((self.price - self.sale_price) / self.price) * 100)
    def discount_val(self):
        return int(self.price - self.sale_price)

def delall():
    p = Product.objects.all()
    attr = Attribute.objects.all()
    attr_item = Attributeitem.objects.all()
    cat = Category.objects.all()
    subcat = Subcategory.objects.all()

    p.delete()
    attr.delete()
    attr_item.delete()
    cat.delete()
    subcat.delete()
    print('All is deleted')