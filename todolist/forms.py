from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(
        max_length = 45,
        widget = forms.TextInput(
            attrs={'class': 'form-input', 'placeholder': 'Enter a task', 'type':'text'}
        )
    )