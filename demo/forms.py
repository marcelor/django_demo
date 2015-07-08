from django import forms


class BigForm(forms.Form):
	field1 = forms.CharField()
	field2 = forms.IntegerField()
	field3 = forms.FileField()