from django.db import models


class Author(models.Model):
    name = models.CharField(
        'autor',
        max_length=50
    )

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name
