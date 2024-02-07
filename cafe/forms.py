from django import forms

class user(forms.Form):
    num1 = forms.CharField(label="value 1",required=True,widget= forms.TextInput(attrs={'class':'form-control'}))
    num2 = forms.CharField(label="value 2",required = True,widget= forms.TextInput(attrs={'class':'form-control'}))
