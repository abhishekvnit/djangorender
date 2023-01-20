from django.db import models

# Create your models here.

class TalcherDirect(models.Model):
    # id = models.AutoField(db_column='ID', primary_key='True')
    name = models.TextField(db_column='Name', primary_key=True)  # Field name made lowercase.
    activity = models.TextField(db_column='Activity', blank=True, null=True)  # Field name made lowercase.
    pgma = models.TextField(db_column='PGMA', blank=True, null=True)  # Field name made lowercase.
    system = models.TextField(db_column='System', blank=True, null=True)  # Field name made lowercase.
    mu = models.TextField(db_column='MU', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'talcher direct'