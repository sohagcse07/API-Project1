from django.db import models

# এখানে আপনার models তৈরি করা হয়েছে

# Company model তৈরি করা হয়েছে
class Company(models.Model):
    # প্রাইমারি কী হিসাবে AutoField
    company_id = models.AutoField(primary_key=True)
    # কোম্পানির নাম
    name = models.CharField(max_length=100)
    # কোম্পানির অবস্থান (লোকেশন)
    location = models.CharField(max_length=100)
    # কোম্পানি সম্পর্কে বিস্তারিত তথ্য
    about = models.TextField()
    # কোম্পানির ধরণ (কোন ফিল্ডে কাজ করে)
    type = models.CharField(
        max_length=100,
        choices=(
            ('IT', 'IT'),
            ('Non IT', 'Non IT'),
            ('Mobiles Phones', 'Mobiles Phones')
        )
    )
    # কখন ডাটা যোগ হয়েছে তা সংরক্ষণ করবে
    add_data = models.DateTimeField(auto_now=True)
    # কোম্পানি সক্রিয় কি না
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Employe ( models.Model):

    name = models.CharField(max_length= 220)
    email = models.EmailField()
    phone = models.CharField(max_length= 15)
    address = models.TextField()
    about = models.TextField()

    position = models.CharField( max_length=100 , choices= (
        ("manager" , "manager") , 
        ("Pl" , "Productledear") , 
        ("product_manager" , "PM"),
        ("MD" , 'MD')))
    
    company = models.ForeignKey( Company , on_delete= models.CASCADE)

# IceCream model তৈরি করা হয়েছে
class IceCream(models.Model):
    # আইসক্রিমের নাম
    name = models.CharField(max_length=100)
    # ফ্লেভার বা স্বাদ
    flavor = models.CharField(max_length=100)
    # দাম (decimal format)
    price = models.DecimalField(max_digits=5, decimal_places=2)
