from django.shortcuts import render
from .forms import BinarioForm

def convertir(request):
    resultado = None
    error = None

    if request.method == "POST":
        form = BinarioForm(request.POST)
        if form.is_valid():
            binario = form.cleaned_data['numero_binario']

            decimal = int(binario, 2)
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:].upper()

            resultado = {
                "decimal": decimal,
                "octal": octal,
                "hexadecimal": hexadecimal
            }
        else:
            error = "El número ingresado no es binario."
            form = BinarioForm()
    else:
        form = BinarioForm()

    return render(request, "convertir.html", {
        "form": form,
        "resultado": resultado,
        "error": error
    })

