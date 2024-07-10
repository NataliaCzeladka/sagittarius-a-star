from django import forms


class ContactRequestForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, required=True)
    email = forms.EmailField(label='Your Email', max_length=50, required=True)
    phone_number = forms.CharField(label='Your Phone Number', max_length=20, required=False)
    message = forms.CharField(
        label='Your Message', widget=forms.Textarea, max_length=1000, required=True
    )
