from django import forms
from django.forms import ModelForm

from mainapp.models import School, User, SchoolAdmin, Course, EditCourse


class SchoolModelForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(SchoolModelForm, self).__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     # self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'
    #
    #     # self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = School
        fields = '__all__'


from mainapp.models import School
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SchoolModelForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(SchoolModelForm, self).__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     # self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'
    #
    #     # self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = School
        fields = '__all__'


class StaffForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('dob', 'special_care_needed', 'subject_of_interest', 'children_name',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('designation', 'children_name',)


class ParentForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('designation', 'subject_of_interest', 'special_care_needed', 'dob',)


# for edit form

class EditStaffForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('dob', 'special_care_needed', 'subject_of_interest', 'children_name', 'password', 'email',)


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('designation', 'children_name', 'password', 'email',)


class EditParentForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('designation', 'subject_of_interest', 'special_care_needed', 'dob', 'password', 'email',)


class EditSchoolAdminForm(forms.ModelForm):
    class Meta:
        model = SchoolAdmin
        exclude = ('password',)


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = EditCourse
        fields = '__all__'


class MyStyleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyStyleForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


