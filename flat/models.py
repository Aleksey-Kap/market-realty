from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)


class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    #parent = models.ForeignKey(self)


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)


class Roomtypes(models.Model):
    name = models.CharField(max_length=100)


class District(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)


class Repairtype(models.Model):
    name = models.CharField(max_length=100)


class Windowsview(models.Model):
    name = models.CharField(max_length=100)


class Lifttype(models.Model):
    name = models.CharField(max_length=100)


class Parkingtype(models.Model):
    name = models.CharField(max_length=100)


class Saletype(models.Model):
    name = models.CharField(max_length=100)


class Sallertype(models.Model):
    name = models.CharField(max_length=100)


class Mertoline(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)


class Metro(models.Model):
    name = models.CharField(max_length=100)
    metroline = models.ForeignKey(Mertoline, on_delete=models.RESTRICT)


class Freeplan(models.Model):
    name = models.CharField(max_length=100)


class Flat(models.Model):
    roomtype = models.ForeignKey(Roomtypes, on_delete=models.RESTRICT)
    freeplan = models.ForeignKey(Freeplan, on_delete=models.RESTRICT, null=True)
    isnew = models.BooleanField()
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    floor = models.IntegerField()
    floortotal = models.IntegerField()
    sqkitchen = models.IntegerField()
    sqtotal = models.IntegerField()
    sqtotaldesc = models.IntegerField()
    height = models.IntegerField(null=True)
    wctype = models.CharField(max_length=100)
    repairtype = models.ForeignKey(Repairtype, on_delete=models.RESTRICT)
    windowsview = models.ForeignKey(Windowsview, on_delete=models.RESTRICT)
    year = models.IntegerField(null=True)
    housetype = models.CharField(max_length=100)
    housetudestrou = models.BooleanField()
    lifttype = models.ForeignKey(Lifttype, on_delete=models.RESTRICT)
    parkingtype = models.ForeignKey(Parkingtype, on_delete=models.RESTRICT)
    saletype = models.ForeignKey(Saletype, on_delete=models.RESTRICT)
    isapartaments = models.BooleanField()
    createdat = models.DateTimeField()
    phone = models.CharField(max_length=100)
    sallertype = models.ForeignKey(Sallertype, on_delete=models.RESTRICT)
    text = models.CharField(max_length=1000)
    price = models.IntegerField()


class Flatmetro(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.RESTRICT)
    metro = models.ForeignKey(Metro, on_delete=models.RESTRICT)

















