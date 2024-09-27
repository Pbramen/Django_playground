from django import forms 

class RegisterForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    user_name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

    def printMessage(self):
        print("form submit success!")
