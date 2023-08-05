from django.core.exceptions import ValidationError

def validate_anio_mes(value):
    partes = value.split('-')

    if len(partes) != 2:
        raise ValidationError("El formato debe ser YYYY-MM.")

    anio, mes = partes

    if not anio.isdigit() or not mes.isdigit():
        raise ValidationError("El año y mes deben ser números enteros.")

    if len(anio) != 4 or not (1 <= int(mes) <= 12):
        raise ValidationError("El año debe tener 4 dígitos y el mes debe estar entre 1 y 12.")

# Validacion de idioma aplicado solo por tema de práctica    
def validate_idioma_permitido(value):
    idiomas = ['Español', 'Quechua', 'Inglés']

    if value not in idiomas:
        raise ValidationError(f"El idioma debe ser uno de los siguientes: {', '.join(idiomas)}.")