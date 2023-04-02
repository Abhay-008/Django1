from django import forms
from .models import Employee

class NameForm(forms.Form):
    CHOICES=(
        ("1","+"),
        ("2","-"),
        ("3","*"),
        ("4","/")
    )
    num1 = forms.CharField(label='First Number', max_length=100)
    op=forms.ChoiceField(choices=['+','-','*','/'])
    num2 = forms.CharField(label='Second Number', max_length=100)


class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee 
        fields=['name','age','sal']   