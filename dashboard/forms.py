from django import forms


class FileUploadForm(forms.Form):
    file_upload = forms.FileField()
    
    class Meta:
        fields = ['file_upload']
        
    