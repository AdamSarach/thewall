from django.db import models


# Create your models here.


class FetchedData(models.Model):
    SITES = (
        ('wnp', 'wnp'),
        ('bankier', 'bankier'),
        ('money', 'money'),
    )

    data_id = models.AutoField(primary_key=True)
    data_name = models.CharField(max_length=8, choices=SITES)
    data_time = models.DateTimeField(auto_now_add=True)
    data_content = models.CharField(max_length=10000)

    def __str__(self):
        return "%s on %s" % (self.data_name, self.data_time)
