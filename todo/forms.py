from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from .models import Todo

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        if commit:
            user.save()
        return user

class ToDoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        } 