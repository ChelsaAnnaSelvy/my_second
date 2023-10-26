from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Define a custom validator to check for spaces in user_name
   
    no_spaces_validator = RegexValidator(
        regex=r'^\S+$',  # Only non-space characters are allowed
        message="Username cannot contain spaces.",
        code="no_spaces"
    )
    user_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(8),
            no_spaces_validator,  # Apply the custom validator
        ],
        unique=True,  # Ensure usernames are unique
    )
    phone = models.CharField(max_length=13, validators=[MinLengthValidator(13)],unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()      
    LANGUAGE_CHOICES=[('ENGLISH','EN'),
                      ('MALAYALAM','ML'),                     
                    ]
    language = models.CharField(max_length=100,choices=LANGUAGE_CHOICES,default='')    
    profile_id = models.AutoField(primary_key=True, unique=True)  # Use AutoField as primary key
    
    def save(self, *args, **kwargs):
        # Auto-generate an 8-digit ID for the profile
        if not self.profile_id:
            last_profile = Profile.objects.order_by('profile_id').last()
            if not last_profile:
                self.profile_id = 10000000  # Start with the first 8-digit ID
            else:
                self.profile_id = last_profile.profile_id + 1  # Increment by 1
        super(Profile, self).save(*args, **kwargs)
    def __str__(self):
        return self.user_name

class Product(models.Model):
    product_name = models.CharField(max_length = 100)
    rate = models.DecimalField(max_digits = 10,decimal_places = 2)
    stock = models.DecimalField(max_digits = 4,decimal_places = 2)
    product_image = models.ImageField(upload_to = 'products')
    CATEGORY_CHOICES = [('MEN',"MEN'S FASHION" ),
                      ('WOMEN',"WOMEN'S FASHION" ),
                      ('KIDS',"KID'S FASHION" )]
    category = models.CharField(max_length = 10, choices = CATEGORY_CHOICES)
    category_id = models.AutoField(primary_key = True,unique = True)
    def save(self, *args, **kwargs):
        # Auto-generate an 8-digit ID for the profile
        if not self.product_id:
            last_product  =  Product.objects.order_by('product_id').last()
            if not last_product:
                self.product_id  =  10000000  # Start with the first 8-digit ID
            else:
                self.product_id  =  last_product.product_id + 1  # Increment by 1
        super(Profile, self).save(*args, **kwargs)
    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key = True,unique = True)
    product_id =  models.ForeignKey(Product, on_delete = models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
    quantity = models.DecimalField(max_digits = 4,decimal_places = 2)
    amount = models.DecimalField(max_digits = 10,decimal_places = 2)

    def save(self, *args, **kwargs):
        # Auto-generate an 8-digit ID for the profile
        if not self.order_id:
            last_order  =  Order.objects.order_by('order_id').last()
            if not last_order:
                self.order_id  =  10000000  # Start with the first 8-digit ID
            else:
                self.order_id  =  last_order.order_id + 1  # Increment by 1
        super(Profile, self).save(*args, **kwargs)
    def __str__(self):
        return self.product_name

class Cart(models.Model):
    product_id =  models.ForeignKey(Product, on_delete = models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
    quantity = models.DecimalField(max_digits = 4,decimal_places = 2)
    timestamp = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits = 10,decimal_places = 2)
    
