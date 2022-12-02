from django import forms
class FormularioPaciente(forms.Form):

    REGIMEN=(
        (1,'Excepción'),
        (2,'Contributivo'),
        (3,'No asegurado'),
        (4, 'Especial'),
        (5, 'Indetreminado/Pendiente'),
        (6, 'Indetreminado/Pendiente'),
        (7, 'Poliza'),
    )
    TIPOAFILIADO=(
        (1,'Cotizannte'),
        (2, 'Beneficiario')
        
    )
    GRUPOINGRESO=(
        (1,'A'),
        (2,'B'),
        (3,'C')
    )

    nombre=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=15
    ) 
    apellidos=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=35
    )
    cedula=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        max_length=10
    )
    
