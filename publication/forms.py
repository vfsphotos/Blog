from django import forms

from .models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('autor', 'pub_title', 'pub_text')
        widgets = {
            'pub_text': forms.Textarea(attrs={'rows': 10, 'cols': 50})
        }


