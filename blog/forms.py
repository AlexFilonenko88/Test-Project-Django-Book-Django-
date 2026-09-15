from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Email адрес")
    subject = forms.CharField(max_length=200, label="Тема сообщения")
    message = forms.CharField(widget=forms.Textarea, label="Текст сообщение")
    send_copy = forms.BooleanField(required=False, label="Отправить копию")

    def clean_emal(self):
        email = self.cleaned_data.get("email")
        if email.endswith("@spam.com"):
            raise forms.ValidationError("Не принимает письма сэтого домена")

        return email
