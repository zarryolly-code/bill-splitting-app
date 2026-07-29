from django import forms
from .models import Expense, Member 


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["description", "amount", "paid_by", "group"]

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["name", "group"]