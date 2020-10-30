from django.db import models


class Drink_type(models.Model):
    programmatic_name = models.CharField(max_length=255)
    friendly_name = models.CharField(
        max_length=255, null=True, blank=True)

    def __str__(self):
        return self.programmatic_name

    def get_friendly_name(self):
        return self.friendly_name


class Drink(models.Model):
    image = models.ImageField()
    drink_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    millilitres = models.IntegerField()
    drink_type = models.ForeignKey(
        "Drink_type", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.drink_name


class About_us_section(models.Model):
    programmatic_name = models.CharField(max_length=255)
    friendly_name = models.CharField(
        max_length=255, null=True, blank=True)

    def __str__(self):
        return self.programmatic_name

    def get_friendly_name(self):
        return self.friendly_name


class About_us(models.Model):
    class Meta:
        verbose_name_plural = "About us"

    image = models.ImageField(null=True, blank=True)
    image_description = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    paragraph = models.TextField()
    section = models.ForeignKey(
        "About_us_section", null=True, blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
