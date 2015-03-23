from django import forms

from students.models import Child_detail, Child_family_detail


class Child_detailform(forms.ModelForm):
    """Upload files with this form"""
    dob = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
    sibling_name = forms.CharField(max_length=50)
    sibling_relationship = forms.CharField(max_length=20)
    sibling_age = forms.PositiveIntegerField(blank=True, null=True)
    sibling_status = forms.CharField(max_length=50, blank=True, null=True)
    sibling_studying = forms.CharField(max_length=50)
    sibling_studying_same_school = forms.CharField(max_length=3, blank=True, null=True)
    staff_id = forms.CharField(max_length=30)
    pin_code = CharField(widget=TextInput(attrs={'type':'number'}),
                    validators=[RegexValidator(regex='^(6)([0-9]){5}$',message='Pincode can have 6 digits'),],
                    required=False, min_length=6)


    phone_number = CharField(widget=TextInput(attrs={'type':'number'}),
                    validators=[RegexValidator(regex='/^([7-9])([0-9]){9}$/',message='Mobile Number can have 10 digits'),],
                    required=False, min_length=6)
    class Meta:
        model = Child_detail
       