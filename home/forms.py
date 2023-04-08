from django import forms
from .models import Medicine, Distributor, Purchase, DetailPurchase, Sell

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'



