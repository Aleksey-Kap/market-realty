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

class Wctype(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Тип Санузла (для выборки)'
        verbose_name = 'Тип Санузла (для выборки)'



class Balcony(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Тип Балкона(для выборки)'
        verbose_name = 'Тип Балкона(для выборки)'



class Loggia(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Тип Лоджии(для выборки)'
        verbose_name = 'Тип Лоджии(для выборки)'


class Floortype(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Тип перекрытий(для выборки)'
        verbose_name = 'Тип перекрытий(для выборки)'


class Heating(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Тип отопления(для выборки)'
        verbose_name = 'Тип отопления(для выборки)'


class Flat(models.Model):
    isdayly = models.BooleanField(default=False, verbose_name='Посуточно аренда')
    isrent = models.BooleanField(default=False, verbose_name='Аренда')
    issale = models.BooleanField(default=False, verbose_name='Продажа')
    roomtype = models.ForeignKey(Roomtypes, on_delete=models.RESTRICT, verbose_name='Сколько комнат')
    freeplan = models.ForeignKey(Freeplan, on_delete=models.RESTRICT, null=True, verbose_name='Планировка')
    isnew = models.BooleanField(verbose_name='Новостройка')
    city = models.ForeignKey(City, on_delete=models.RESTRICT, verbose_name='Город')
    floor = models.IntegerField(verbose_name='Этаж')
    floortotal = models.IntegerField(null=True, verbose_name='Количество этажей в доме')
    sqkitchen = models.IntegerField(null=True, verbose_name='Площадь кухни')
    sqtotal = models.IntegerField(verbose_name='Общая площадь')
    sqtotaldesc = models.CharField(max_length=100, verbose_name='Площадь с расшифровкой')
    height = models.FloatField(null=True, blank=True, verbose_name='Высота потолков')
    wctype = models.ForeignKey(Wctype, null=True, on_delete=models.RESTRICT, verbose_name='Тип санузла')
    repairtype = models.ForeignKey(Repairtype, on_delete=models.RESTRICT, null=True, verbose_name='Ремонт')
    windowsview = models.ForeignKey(Windowsview, on_delete=models.RESTRICT, null=True, verbose_name='Вид из окна')
    balcony = models.ForeignKey(Balcony, on_delete=models.RESTRICT, blank=True, null=True, verbose_name='Балкон')
    loggia = models.ForeignKey(Loggia, on_delete=models.RESTRICT, blank=True, null=True, verbose_name='Лоджия')
    year = models.IntegerField(null=True, verbose_name='Год постройки')
    housetype = models.ForeignKey(Housetype, on_delete=models.RESTRICT, null=True, verbose_name='Тип дома')
    floortype = models.ForeignKey(Floortype, on_delete=models.RESTRICT, blank=True, null=True, verbose_name='Тип перекрытий')
    entrances = models.IntegerField(blank=True, null=True, verbose_name='Подъезды')
    heating = models.ForeignKey(Heating, on_delete=models.RESTRICT, blank=True, null=True, verbose_name='Тип отопления')
    accidentrate = models.BooleanField(blank=True, null=True, verbose_name='Аварийность')
    garbagechute = models.BooleanField(blank=True, null=True, verbose_name='Мусоропровод')
    housetudestrou = models.BooleanField(verbose_name='Дом под снос')
    lifttype = models.ForeignKey(Lifttype, on_delete=models.RESTRICT, null=True, verbose_name='Тип лифта')
    parkingtype = models.ForeignKey(Parkingtype, on_delete=models.RESTRICT, null=True, verbose_name='Паркинг')
    saletype = models.ForeignKey(Saletype, on_delete=models.RESTRICT, blank=True, null=True, verbose_name='Тип продаж')
    metro = models.ForeignKey(Metro, on_delete=models.RESTRICT, null=True, verbose_name='Метро')
    isapartaments = models.BooleanField(null=True, verbose_name='Апартаменты')

    # аренда
    withanimals = models.BooleanField(blank=True, null=True, verbose_name='Можно с животными')
    withchildren = models.BooleanField(blank=True, null=True, verbose_name='Можно с детьми')
    furnitureintherooms = models.BooleanField(blank=True, null=True, verbose_name='Мебель в комнатах')
    thefurnitureinthekitchen = models.BooleanField(blank=True, null=True, verbose_name='Мебель на кухне')
    fridge = models.BooleanField(blank=True, null=True, verbose_name='Холодильник')
    dishwasher = models.BooleanField(blank=True, null=True, verbose_name='Посудомоечная машина')
    washingmachine = models.BooleanField(blank=True, null=True, verbose_name='Стиральная машина')
    tv = models.BooleanField(blank=True, null=True, verbose_name='Телевизор')
    telephone = models.BooleanField(blank=True, null=True, verbose_name='Телефон')
    bath = models.BooleanField(blank=True, null=True, verbose_name='Ванна')
    showercabin = models.BooleanField(blank=True, null=True, verbose_name='Душевая кабина')
    conditioner = models.BooleanField(blank=True, null=True, verbose_name='Кондиционер')
    internet = models.BooleanField(blank=True, null=True, verbose_name='Интернет')
    # //аренда

    createdat = models.DateTimeField(verbose_name='дата регистрации')
    phone = models.CharField(max_length=100, verbose_name='Телефон клиента')
    sallertype = models.ForeignKey(Sallertype, on_delete=models.RESTRICT, verbose_name='Тип продавца')
    text = models.TextField(verbose_name='Текст объявления')
    price = models.IntegerField(verbose_name='Цена')
    address = models.CharField(max_length=200, verbose_name='адрес')
    coord_lat = models.CharField(max_length=100, blank=True, null=True, verbose_name='широта')
    coord_long = models.CharField(max_length=100, blank=True, null=True, verbose_name='долгота')


    def __str__(self):
        return f'# {self.pk} {self.address[:20]} {self.price}'


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
    return 'static/uploads/flats/flat_{0}/{1}'.format(instance.flat_id, filename)


class Flatimges(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.RESTRICT, related_name='images')
    # pik = models.FileField(upload_to='static/uploads/flats/')
    pik = models.FileField(upload_to=flat_upload_path,)

    # def __str__(self):
    #     return self.name


    class Meta:
        verbose_name_plural = 'Тип фото (для выборки)'
        verbose_name = 'Тип фото (для выборки)'
















