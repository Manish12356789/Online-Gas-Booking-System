from django import forms
from django.forms import widgets
from .models import FeedbackComplaint



class FeedbackComplaintForm(forms.ModelForm):
    class Meta:
        types=[('feedback','Feedback'),
         ('complaint','Complaint')]

        model = FeedbackComplaint
        fields = '__all__'
        exclude = ['user',]
        widgets = {
            'type': widgets.RadioSelect(choices=types, attrs={'class': 'radio-inline'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Product related, delivery related, etc... '}),
            'message': widgets.Textarea({'class': 'form-control', 'rows':'3' , 'placeholder': 'Write messages less than 1000 words...'}),
            # 'user':widgets.ChoiceWidget({'type': 'hidden', 'value': '{{request.user.id}}'})
        }
