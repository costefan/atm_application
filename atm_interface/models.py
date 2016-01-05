from django.db import models
from django.core.validators import MinLengthValidator

PERSON_SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Person(models.Model):
    """
    Store user data name, age, sex, city
    """

    name = models.CharField(max_length=20, null=False)
    sex = models.CharField(max_length=1, choices=PERSON_SEX_CHOICES)
    age = models.IntegerField()
    city = models.CharField(max_length=20)

    def __str__(self):
        return 'Person {}'.format(self.name)


class Card(models.Model):
    """
    Store card data with number, pin, cvv, cash

    Related to Person model
    """

    number = models.CharField(max_length=16, validators=[MinLengthValidator(16)], null=False)
    pin = models.CharField(max_length=4, validators=[MinLengthValidator(4)], null=False)
    cvv = models.CharField(max_length=3, validators=[MinLengthValidator(3)], null=False)
    blocked = models.BooleanField(default=False)
    cash = models.IntegerField(default=0, null=False)
    person_id = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return 'Card {}'.format(self.number)

    class Meta:
        ordering = ['id']


class Operation(models.Model):
    card_id = models.ForeignKey(Card)
    time = models.TimeField(null=False)
    code = models.IntegerField(null=False)
    cash = models.IntegerField(default=0)

    def __str__(self):
        return 'Operation {} {}'.format(self.id, self.time)


