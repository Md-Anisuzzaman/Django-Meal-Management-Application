# from django import forms
# from .models import DailyExpenses

# class ExpensesForm(forms.ModelForm):
   

#     class Meta:
#         model = DailyExpenses
#         fields = ['date', 'item_name', 'quantity', 'price']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Customize widgets with Bootstrap classes
#         # self.fields['date'].widget.attrs.update({'class': 'form-control'})
#         self.fields['date'].widget=forms.DateInput(attrs={'type': 'date'})

