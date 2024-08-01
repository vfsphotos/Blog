from django.db import models

from author.models import Author


class Publication(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    date_pub = models.DateField(
        'publication date',
        auto_now_add=True
    )
    pub_title = models.CharField(
        'publication title',
        max_length=100
    )
    pub_text = models.TextField(
        'publications',
        max_length=255
    )

    class Meta:
        db_table = 'pubblications'
