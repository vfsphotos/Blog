from django.db import models

from author.models import Author


class Publication(models.Model):
    autor = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    date_pub = models.DateField(
        'publication date',
        auto_now_add=True
    )
    pub_title = models.CharField(
        'Título da publicação',
        max_length=100
    )
    pub_text = models.TextField(
        'Texto da publicação',
        max_length=255
    )

    class Meta:
        db_table = 'publications'

    def __str__(self):
        return self.name
