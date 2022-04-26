from django.db import models


class GenderChoices(models.TextChoices):
    NULL = 'null', "----"
    MAN = 'man', "Erkak"
    WOMAN = 'woman', "Ayol"


class FamilyStatusChoices(models.TextChoices):
    POOR = 'poor', "Kam tamillangan"
    SIMPLE = 'simple', "Oddiy"


class MahallaSectionChoices(models.TextChoices):
    I = 'I', '1-sektor'
    II = 'II', '2-sektor'
    III = 'III', '3-sektor'
    IV = 'IV', '4-sektor'