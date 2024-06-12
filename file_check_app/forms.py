from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if not file.name.endswith('.py'):
                raise forms.ValidationError('Only .py files are allowed.')
        return file