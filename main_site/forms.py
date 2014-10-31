from django import forms

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    name = forms.CharField(label='Imię i Nazwisko')
    phone = forms.CharField(label='Telefon')
    email = forms.CharField(label='Adres email')
    topic = forms.CharField(label='Temat wiadomości')
    message = forms.CharField(widget=forms.Textarea, label='Wiadomość')

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'main_site:contact'
    #
    #     self.helper.add_input(Submit('submit', 'Wyślij'))
