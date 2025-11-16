from django import forms

class BinarioForm(forms.Form):
    numero_binario = forms.CharField(
        label="Número binario",
        max_length=64,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    def clean_numero_binario(self):
        numero = self.cleaned_data['numero_binario']
        if not all(c in '01' for c in numero):
            raise forms.ValidationError("Solo se permiten caracteres 0 y 1")
        return numero
