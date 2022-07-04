from django.db import models


class Airport(models.Model):
    code = models.CharField("Airport Code", unique=True, db_index=True, max_length=20)
    name = models.CharField("Airport Name", max_length=150)


class Flight(models.Model):
    flight_number = models.CharField("Flight Number", max_length=20)
    take_off = models.DateTimeField("Take Off Time")
    landing = models.DateTimeField("Landing Time")
    to_airport = models.ForeignKey(Airport, on_delete=models.ProtectedError,
                                   related_name="to_airport")
    from_airport = models.ForeignKey(Airport, on_delete=models.ProtectedError,
                                     related_name="from_airport")
