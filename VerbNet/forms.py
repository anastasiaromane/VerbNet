from django import forms


# class ContactForm(forms.Form):
#     contact_name = forms.CharField(required=True)
#     contact_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(
#         required=True,
#         widget=forms.Textarea
#     )
#     def __init__(self, *args, **kwargs):
#         super(ContactForm, self).__init__(*args, **kwargs)
#         self.fields['contact_name'].label = "Имя"
#         self.fields['contact_email'].label = "Почта"
#         self.fields['message'].label = ""
#         self.fields['subject'].label = "Тема"


class ContactForm(forms.Form):
    sender = forms.EmailField(
      required=True,
      label='',
      widget=forms.TextInput(
        attrs={'style': 'width:350px', 'placeholder': 'Введите email'}
        )
      )
    name = forms.CharField(
      label='',
      max_length=100,
      widget=forms.TextInput(
        attrs={'style': 'width:350px', 'placeholder': 'Введите имя'}
        )
      )
    message = forms.CharField(
      label='',
      widget=forms.Textarea(
        attrs={'style': 'width:350px','placeholder': 'Введите сообщение'}
        )
      )