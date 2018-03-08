# Django imports
from django import forms
# Crispy form imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField, Submit
# App imports
from .models import ScrapedJob


class JobSearchForm(forms.Form):
    collector_name = forms.ModelChoiceField(
        queryset=ScrapedJob.objects.values_list('collector_name', flat=True),
        empty_label="Choose a Collector"
    )

    def __init__(self, *args, **kwargs):
        super(BrandSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            'collector_name',
            Submit('Search', 'search', css_class='btn-default'),
        )
        self.helper.form_method = 'get'
