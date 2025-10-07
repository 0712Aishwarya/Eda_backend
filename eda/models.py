from django.db import models

class SalesData(models.Model):
    market = models.CharField(max_length=255)
    channel = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    variant = models.CharField(max_length=255, blank=True, null=True)
    pack_type = models.CharField(max_length=255, blank=True, null=True)
    ppg = models.CharField(max_length=255, blank=True, null=True)
    pack_size = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField()
    month = models.IntegerField()
    week = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    brcat_id = models.CharField(max_length=255, blank=True, null=True)
    sales_value = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    volume_units = models.FloatField(blank=True, null=True)
    
    # D1-D6
    D1 = models.FloatField(blank=True, null=True)
    D2 = models.FloatField(blank=True, null=True)
    D3 = models.FloatField(blank=True, null=True)
    D4 = models.FloatField(blank=True, null=True)
    D5 = models.FloatField(blank=True, null=True)
    D6 = models.FloatField(blank=True, null=True)

    # AV1-AV6
    AV1 = models.FloatField(blank=True, null=True)
    AV2 = models.FloatField(blank=True, null=True)
    AV3 = models.FloatField(blank=True, null=True)
    AV4 = models.FloatField(blank=True, null=True)
    AV5 = models.FloatField(blank=True, null=True)
    AV6 = models.FloatField(blank=True, null=True)

    # EV1-EV6
    EV1 = models.FloatField(blank=True, null=True)
    EV2 = models.FloatField(blank=True, null=True)
    EV3 = models.FloatField(blank=True, null=True)
    EV4 = models.FloatField(blank=True, null=True)
    EV5 = models.FloatField(blank=True, null=True)
    EV6 = models.FloatField(blank=True, null=True)
    def __str__(self):
        return f"{self.brand} - {self.year}-{self.month}-{self.week}"

