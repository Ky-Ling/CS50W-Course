from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # Related_name: it is going to be a way of me accessing a relationship in the reverse order:
    #   If we have an airport, how can I get all of the flights that have that airport as an origin?
    #   Now, if i get access all the departures, which gets me all of the flights.
    
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # This function will return a string representation of the object.
    def __str__(self) -> str:
        return f"{self.id}: {self.origin} to {self.destination}"

