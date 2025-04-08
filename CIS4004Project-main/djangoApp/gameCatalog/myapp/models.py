from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Item(models.Model):
    CATEGORY_CHOICES = [
        (1, 'Game Copy'),
        (2, 'Console'),
        (3, 'Peripheral')
    ]
    
    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('LIKE_NEW', 'Like New'),
        ('VERY_GOOD', 'Very Good'),
        ('GOOD', 'Good'),
        ('FAIR', 'Fair'),
        ('POOR', 'Poor')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    pubmanu = models.CharField(max_length=100)  # Publisher/Manufacturer
    year = models.IntegerField()
    quantity = models.IntegerField(default=1)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    class Meta:
        ordering = ['-created_at']
