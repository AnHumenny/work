from django import forms

class DateForm(forms.Form):

    start_date = forms.DateField(widget=forms.SelectDateWidget(), label="Начальная дата    ")
    end_date = forms.DateField(widget=forms.SelectDateWidget(), label="Конечная дата     ")

