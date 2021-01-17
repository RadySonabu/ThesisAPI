from django import forms

GENDER_CHOICES = (
    ('Male','Male'),
    ('Female', 'Female'),
)

LESION_LOCALIZATION = (
    ('Head', 'Head'),
    ('Body', 'Body'),
    ('Arms', 'Arms'),
    ('Lower Extremities', 'Lower Extremities')
)
class FileUploadForm(forms.Form):
    file_upload = forms.FileField()
    patient_name = forms.CharField(max_length=250)
    patient_gender = forms.ChoiceField(choices=GENDER_CHOICES)
    patient_age = forms.IntegerField()
    lesion_location = forms.ChoiceField(choices=LESION_LOCALIZATION)

    class Meta:
        fields = ['file_upload']
        
    