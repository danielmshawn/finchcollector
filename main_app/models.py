from django.db import models
# Import the reverse function
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

MEALS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)

# Create your models here.
class Accessory(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # create a M:M relationdhip with Accessory
    # accessories is the Related Manager
    accessories = models.ManyToManyField(Accessory)
    # add user_id FK column
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # adding the 'choices' field option
        choices=MEALS,
        # setting the default value to 'M' Morning
        default=MEALS[0][0]
        )
    
    # This creates a finch_id FK, and ensures it's deleted if Finch is deleted
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
    def __str__(self):
        # Nice django method that creates access to human friendly description
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
