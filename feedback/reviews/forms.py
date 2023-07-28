from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', 'review_text'] # selected fields
        fields = '__all__' # all fields will be added in form
        # exclude = ['owner_comment'] # the fields which you do not want to render in form
