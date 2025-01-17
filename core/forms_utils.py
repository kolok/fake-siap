from django import forms


def address_form_fields():
    return (
        forms.CharField(
            max_length=255,
            min_length=1,
            error_messages={
                "required": "L'adresse est obligatoire",
                "min_length": "L'adresse est obligatoire",
                "max_length": "L'adresse ne doit pas excéder 255 caractères",
            },
        ),
        forms.CharField(
            max_length=255,
            error_messages={
                "required": "Le code postal est obligatoire",
                "max_length": "Le code postal ne doit pas excéder 255 caractères",
            },
        ),
        forms.CharField(
            max_length=255,
            error_messages={
                "required": "La ville est obligatoire",
                "max_length": "La ville ne doit pas excéder 255 caractères",
            },
        ),
    )
