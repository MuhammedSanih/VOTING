from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'address','register_no','roll_no','department','batch']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

from .models import Candidate

class CandidateForm(forms.ModelForm):
    # Define the choices for position
    POSITION_CHOICES = [
        ('CHAIRMAN', 'CHAIRMAN'),
        ('GENERAL SECRETARY', 'GENERAL SECRETARY'),
        ('VICE CHAIRMAN', 'VICE CHAIRMAN'),
        ('JOINT SECRETARY', 'JOINT SECRETARY'),
        ('UUC 1', 'UUC 1'),
        ('UUC 2', 'UUC 2'),
        ('FINE ARTS SECRETARY', 'FINE ARTS SECRETARY'),
        ('STUDENT EDITOR','STUDENT EDITOR'),
        ('GENERAL CAPTAIN','GENERAL CAPTAIN'),
        ('1ST DC REP','1ST DC REP'),
        ('2ND DC REP','2ND DC REP'),
            
        
    ]
    
    # Use the ChoiceField for position
    position = forms.ChoiceField(choices=POSITION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'department', 'batch', 'image', 'position']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'batch': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
