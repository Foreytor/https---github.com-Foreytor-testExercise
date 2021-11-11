from django import forms
import re


class SearcherDNKForm(forms.Form):
    codon = forms.CharField(label='Введите кодон', max_length=3)

    def clean_codon(self):
        data = self.cleaned_data['codon']

        tpl = '[ACGT]{3}'
        if re.match(tpl, str(data).upper()) is None:
            raise forms.ValidationError('Неверный формат кодона, кодон может седержать только символы (A,C,G,T)')
        return data