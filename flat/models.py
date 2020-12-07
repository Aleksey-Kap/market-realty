from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип Страны'
        verbose_name = 'Тип Страна'


class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    pid = models.ForeignKey('self', null=True, blank=True, related_name='parent', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип Регионы (для выборки)'
        verbose_name = 'Тип Регион (для выборки)'


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    pid = models.ForeignKey('self', null=True, blank=True, related_name='parent', on_delete=models.RESTRICT)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип Города (для выборки)'
        verbose_name = 'Тип Город (для выборки)'



class Roomtypes(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип Количество комнат в квартире (для выборки)'
        verbose_name = 'Тип Количество комнат в квартире (для выборки)'



class District(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип Районы города (для выборки)'
        verbose_name = 'Тип Район города (для выборки)'


class Repairtype(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип Ремонт (для выборки)'
        verbose_name = 'Тип Ремонт (для выборки)'


class Windowsview(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип Вид из окна (для выборки)'
        verbose_name = 'Тип Вид из окна (для выборки)'


class Housetype(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип дома (для выборки)'
        verbose_name = 'Тип дома (для выборки)'



class Lifttype(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип лифта (для выборки)'
        verbose_name = 'Тип лифта (для выборки)'


class Parkingtype(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип парковка(для выборки)'
        verbose_name = 'Тип парковка(для выборки)'


class Saletype(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип продажи(для выборки)'
        verbose_name = 'Тип продажи(для выборки)'


class Sallertype(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип продавца(для выборки)'
        verbose_name = 'Тип продавца(для выборки)'


class Mertoline(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип линия метро (для выборки)'
        verbose_name = 'Тип линия метро (для выборки)'


class Metro(models.Model):
    name = models.CharField(max_length=100)
    metroline = models.ForeignKey(Mertoline, on_delete=models.RESTRICT)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип метро (для выборки)'
        verbose_name = 'Тип метро (для выборки)'


class Freeplan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Тип Планировки (для выборки)'
        verbose_name = 'Тип Планировка (для выборки)'


class Flat(models.Model):
    roomtype = models.ForeignKey(Roomtypes, on_delete=models.RESTRICT, verbose_name='Сколько комнат')
    freeplan = models.ForeignKey(Freeplan, on_delete=models.RESTRICT, null=True, verbose_name='Планировка')
    isnew = models.BooleanField(verbose_name='Новостройка')
    city = models.ForeignKey(City, on_delete=models.RESTRICT, verbose_name='Город')
    floor = models.IntegerField(verbose_name='Этаж')
    floortotal = models.IntegerField(null=True, verbose_name='Количество этажей в доме')
    sqkitchen = models.IntegerField(null=True, verbose_name='Площадь кухни')
    sqtotal = models.IntegerField(verbose_name='Общая площадь')
    sqtotaldesc = models.IntegerField(verbose_name='Площадь с расшифровкой')
    height = models.IntegerField(null=True, verbose_name='Высота потолков')
    wctype = models.CharField(max_length=100, null=True, verbose_name='Тип санузла')
    repairtype = models.ForeignKey(Repairtype, on_delete=models.RESTRICT, null=True, verbose_name='Ремонт')
    windowsview = models.ForeignKey(Windowsview, on_delete=models.RESTRICT, null=True, verbose_name='Вид из окна')
    year = models.IntegerField(null=True, verbose_name='Год постройки')
    housetype = models.ForeignKey(Housetype, on_delete=models.RESTRICT, null=True, verbose_name='Тип дома')
    housetudestrou = models.BooleanField(verbose_name='Дом под снос')
    lifttype = models.ForeignKey(Lifttype, on_delete=models.RESTRICT, null=True, verbose_name='Тип лифта')
    parkingtype = models.ForeignKey(Parkingtype, on_delete=models.RESTRICT, null=True, verbose_name='Паркинг')
    saletype = models.ForeignKey(Saletype, on_delete=models.RESTRICT, verbose_name='Тип продаж')
    isapartaments = models.BooleanField(null=True, verbose_name='Апартаменты')
    createdat = models.DateTimeField(verbose_name='дата регистрации')
    phone = models.CharField(max_length=100, verbose_name='Телефон клиента')
    sallertype = models.ForeignKey(Sallertype, on_delete=models.RESTRICT, verbose_name='Тип продавца')
    text = models.TextField(verbose_name='Текст объявления')
    price = models.IntegerField(verbose_name='Цена')
    address = models.CharField(max_length=200, verbose_name='адрес')
    coord_lat = models.CharField(max_length=100, verbose_name='широта')
    coord_long = models.CharField(max_length=100, verbose_name='долгота')



    class Meta:
        verbose_name_plural = 'Квартиры'
        verbose_name = 'Квартира'
        ordering = ['-createdat']


class Flatmetro(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.RESTRICT)
    metro = models.ForeignKey(Metro, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип метро-квартиры (для выборки)'
        verbose_name = 'Тип метро-квартиры (для выборки)'


def flat_upload_path(instance, filename):
    return 'flats/flat_{0}'.format(instance.id)


class Flatimges (models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.RESTRICT)
    pik = models.FileField(upload_to=flat_upload_path)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'Тип фото (для выборки)'
        verbose_name = 'Тип фото (для выборки)'
















