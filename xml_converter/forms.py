from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field


class XmlFileForm(forms.Form):
    file = forms.FileField(
        label="XML file.",
        error_messages={
            "required": "Choose the XML file"
        },
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('file', css_class='form-control'),
                    css_class="input-group mb-3"
                ),
                Div(
                    Submit('submit', 'Submit', css_class='btn btn-primary mt-3'),
                    css_class="d-grid gap-2"
                ),
                css_class='row p-5'
            )
        )
