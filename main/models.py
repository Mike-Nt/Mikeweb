from django.db import models
from django.utils import timezone

class Category(models.Model):
    cat = models.IntegerField(verbose_name="Категория", default=1)
    cost = models.IntegerField(default=0,
                               blank=True, verbose_name="Цена")
    def __str__(self):
        return str(self.cat)


class Home(models.Model):
    number = models.IntegerField(verbose_name="Номер дома")

    begin_date = models.DateField(verbose_name="Дата заезда" , null=True,
            default=None, blank=True)
    end_date = models.DateField(verbose_name="Дата отъезда", default=None,
            blank=True, null=True)
    sum = models.IntegerField(default=0,
            blank=True, verbose_name="Сумма:")
    name = models.CharField(max_length=50, verbose_name="Заказчик", default=None,
            blank=True)
    Category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, default=1)
    free = models.BooleanField(verbose_name="Cвободно", default=True)
   # def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()

    def __str__(self):
        return str(self.number)
# Create your models here.
