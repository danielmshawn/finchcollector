from django.db import models
# Import the reverse function


from django.urls import reverse

MEALS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

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
    
