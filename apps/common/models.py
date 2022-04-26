from django.db import models
from django.urls import reverse
from .choices import *


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    passport = models.CharField(max_length=128)
    stir = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    birth_day = models.DateField()
    gender = models.CharField(choices=GenderChoices.choices, max_length=16, default=GenderChoices.NULL)

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.middle_name)

    class Meta:
        verbose_name = 'Fuqoro'
        verbose_name_plural = verbose_name


class Family(models.Model):
    """Oila"""
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='common.FamilyMember')
    status = models.CharField(choices=FamilyStatusChoices.choices, max_length=128, default=FamilyStatusChoices.SIMPLE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Oila'
        verbose_name_plural = verbose_name


class FamilyMember(models.Model):
    """Oila a`zolar"""
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Oila a`zolari'
        verbose_name_plural = verbose_name


class House(models.Model):
    """Xonadon"""
    families = models.ManyToManyField(Family, blank=True)
    number = models.CharField(max_length=128)
    level = models.IntegerField(default=1)
    street = models.ForeignKey('common.Street', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.number


    class Meta:
        verbose_name = 'Xonadon'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('house-detail', kwargs={'pk': self.id, 'street_pk': self.street.id})


class Street(models.Model):
    """Ko'cha"""
    name = models.CharField(max_length=128)
    mahalla = models.ForeignKey('common.Mahalla', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Ko`cha'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('street-detail', kwargs={'pk': self.id, 'mahalla_pk': self.mahalla.id})



class Mahalla(models.Model):
    """Mahalla"""
    name = models.CharField(max_length=128)
    district = models.ForeignKey('common.District', on_delete=models.CASCADE)
    section = models.CharField(
        max_length=128, choices=MahallaSectionChoices.choices, default=MahallaSectionChoices.I
        )

    def __str__(self) -> str:
        return self.name
    
 
    def houses(self):
        return House.objects.filter(
            street_id__in=self.street_set.all().values_list('id', flat=True)
        )
    
    def houses_level1(self):
        return self.houses().filter(level=1)
    
    def houses_level2(self):
        return self.houses().filter(
            ~models.Q(level=1)  # query
        )
    
    def get_absolute_url(self):
        return reverse('mahalla-detail', kwargs={'pk': self.id, 'district_pk': self.district.id})

    class Meta:
        verbose_name = 'Mahalla'
        verbose_name_plural = verbose_name


class District(models.Model):
    """Tuman"""
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    def streets(self):
        return Street.objects.filter(
            mahalla_id__in=self.mahalla_set.all().values_list('id', flat=True)
        )
    
    def houses(self):
        return House.objects.filter(
            street_id__in=self.streets().values_list('id', flat=True)
        )
    
    def houses_level1(self):
        return self.houses().filter(level=1)
    
    def houses_level2(self):
        return self.houses().filter(
            ~models.Q(level=1)  # query
        )

    def get_absolute_url(self):
        return reverse('district-detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Tuman'
        verbose_name_plural = verbose_name