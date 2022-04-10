from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id',]


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='pictures/', max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.temperature = round(self.temperature, 1)
        super(Measurement, self).save(*args, **kwargs)
