from django.db import models

# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=50)
    City_of_Residence = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Phone_Number = models.BigIntegerField(null=True, blank=True, default=None)
    Whats_Number = models.BigIntegerField(null=True, blank=True, default=None)
    Travel_Destination = models.CharField(max_length=100)
    Date_of_Travel = models.DateField()
    No_of_People = models.IntegerField()  

    def __self__(self):
        return self.Name

        # contact.html

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    Phone_Number = models.BigIntegerField(null=True, blank=True, default=None)
    message = models.TextField()
    def __str__(self):
        return self.name


    # main.html


class Image(models.Model):
    Image_id=models.IntegerField(null=True, blank=True, default=None)
    img=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100,default="basic")
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    @property
    def imageurl(self):
        try:
            url=self.img.url
        except:
            url=""
        return url
    

class i_Image(models.Model):
    i_Image_id=models.IntegerField(null=True, blank=True, default=None)
    Image=models.ForeignKey(Image,on_delete=models.CASCADE)
    # Image=models.ForeignKey(Image,on_delete=models.CASCADE)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    place=models.CharField(max_length=30)
    place1=models.CharField(max_length=20)
    place2=models.CharField(max_length=20)
    place3=models.CharField(max_length=20)
    place4=models.CharField(max_length=20)
    place5=models.CharField(max_length=20)
    place6=models.CharField(max_length=20)
    place7=models.CharField(max_length=20)
    place8=models.CharField(max_length=20)
    main_img=models.ImageField(upload_to='pic')
    place9=models.CharField(max_length=200)
    place10=models.TextField(default='name')
    place11=models.CharField(max_length=200)
    place12=models.TextField(default='name')
    place13=models.CharField(max_length=200,default='name')
    place14=models.TextField(default='name')
    place15=models.CharField(max_length=200,default='name')
    place16=models.TextField(default='name')
    place9=models.CharField(max_length=200,default='name')
    place10=models.TextField(default='name')
    place11=models.CharField(max_length=200,default='name')
    place12=models.TextField(default='name')
    place13=models.CharField(max_length=200,default='name')
    place14=models.TextField(default='name')
    place15=models.CharField(max_length=200,default='name')
    place16=models.TextField(default='name')
    place17=models.CharField(max_length=200,default='name')
    place18=models.TextField(default='name')
    place19=models.CharField(max_length=200,default='name')
    place20=models.TextField(default='name')
    place21=models.CharField(max_length=200,default='name')
    place22=models.TextField(default='name')
    place23=models.CharField(max_length=200,default='name')


    
    # group.html
    


class G_winder(models.Model):
    im=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def G_winderurl(self):
        try:
            url=self.im.url
        except:
            url=""
        return url
    
class G_summer(models.Model):
    i=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def G_summerurl(self):
        try:
            url=self.i.url
        except:
            url=""
        return url
    
class G_reserved(models.Model):
    re=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def G_reservedurl(self):
        try:
            url=self.re.url
        except:
            url=""
        return url
    
    # india.html


class India(models.Model):
    india=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Indiaurl(self):
        try:
            url=self.india.url
        except:
            url=""
        return url
    

    # north.html


class North(models.Model):
    north=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Northurl(self):
        try:
            url=self.north.url
        except:
            url=""
        return url
    
    # education.html

class Education(models.Model):
    education=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Educationurl(self):
        try:
            url=self.education.url
        except:
            url=""
        return url
    

     # south.html

class South(models.Model):
    south=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Southurl(self):
        try:
            url=self.south.url
        except:
            url=""
        return url
    
    # east.html

class East(models.Model):
    east=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Easturl(self):
        try:
            url=self.east.url
        except:
            url=""
        return url
    
    # europe.html


class Europe(models.Model):
    europe=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Europeurl(self):
        try:
            url=self.europe.url
        except:
            url=""
        return url
    
    # honeymoon.html,goa

class Honeymoon(models.Model):
    honeymoon=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Honeymoonurl(self):
        try:
            url=self.honeymoon.url
        except:
            url=""
        return url
    
    # kerala

class Kerala(models.Model):
    kerala=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Keralaurl(self):
        try:
            url=self.kerala.url
        except:
            url=""
        return url
    
        # shimla 

class Shimla(models.Model):
    shimla=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Shimlaurl(self):
        try:
            url=self.shimla.url
        except:
            url=""
        return url
    
        # manali

class Manali(models.Model):
    manali=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Manaliurl(self):
        try:
            url=self.manali.url
        except:
            url=""
        return url
    
    # Andaman

class Andaman(models.Model):
    andaman=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Andamanurl(self):
        try:
            url=self.andaman.url
        except:
            url=""
        return url
    
        # munnar

class Munnar(models.Model):
    munnar=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Munnarurl(self):
        try:
            url=self.munnar.url
        except:
            url=""
        return url
    
            # kodaikanal

class Kodai(models.Model):
    k_img=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Kodaiurl(self):
        try:
            url=self.k_img.url
        except:
            url=""
        return url


            # Ooty

class Ooty(models.Model):
    ooty=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Ootyurl(self):
        try:
            url=self.ooty.url
        except:
            url=""
        return url


            # Paris

class Paris(models.Model):
    paris=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Parisurl(self):
        try:
            url=self.paris.url
        except:
            url=""
        return url

            # Italy

class Italy(models.Model):
    italy=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Italyurl(self):
        try:
            url=self.italy.url
        except:
            url=""
        return url

      # Tailand

class Tailand(models.Model):
    tailand=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)

    
    @property
    def Tailandurl(self):
        try:
            url=self.tailand.url
        except:
            url=""
        return url

      # Australia

class Australia(models.Model):
    australia=models.ImageField(upload_to="pic")
    plan=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.CharField(max_length=20,null=True)
    
    @property
    def Australiaurl(self):
        try:
            url=self.australia.url
        except:
            url=""
        return url

class Details(models.Model):
    place=models.CharField(max_length=30)
    place1=models.CharField(max_length=20)
    place2=models.CharField(max_length=20)
    place3=models.CharField(max_length=20)
    place4=models.CharField(max_length=20)
    place5=models.CharField(max_length=20)
    place6=models.CharField(max_length=20)
    place7=models.CharField(max_length=20)
    place8=models.CharField(max_length=20)
    main_img=models.ImageField(upload_to='pic')
    place9=models.CharField(max_length=200)
    place10=models.TextField(default='name')
    place11=models.CharField(max_length=200)
    place12=models.TextField(default='name')
    place13=models.CharField(max_length=200,default='name')
    place14=models.TextField(default='name')
    place15=models.CharField(max_length=200,default='name')
    place16=models.TextField(default='name')
    place9=models.CharField(max_length=200,default='name')
    place10=models.TextField(default='name')
    place11=models.CharField(max_length=200,default='name')
    place12=models.TextField(default='name')
    place13=models.CharField(max_length=200,default='name')
    place14=models.TextField(default='name')
    place15=models.CharField(max_length=200,default='name')
    place16=models.TextField(default='name')
    place17=models.CharField(max_length=200,default='name')
    place18=models.TextField(default='name')
    place19=models.CharField(max_length=200,default='name')
    place20=models.TextField(default='name')
    place21=models.CharField(max_length=200,default='name')
    place22=models.TextField(default='name')
    place23=models.CharField(max_length=200,default='name')
    place24=models.TextField(default='name')
    place25=models.CharField(max_length=200,default='name')
    place26=models.TextField(default='name')
    place27=models.CharField(max_length=200,default='name')
    place28=models.TextField(default='name')
    place29=models.CharField(max_length=200,default='name')
    place30=models.TextField(default='name')
    place31=models.CharField(max_length=200,default='name')
