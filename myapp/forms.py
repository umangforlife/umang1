from .models import *
from django import forms      
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.http import HttpResponse

# Create your forms here.

class reg_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput())    
    semail=forms.CharField(widget=forms.EmailInput())
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password':
            if self.cleaned_data['password']!=self.cleaned_data['confirm_password']:
                raise forms.ValidaionError("the two password fields did not match")
            return self.cleaned_data
    
    
    class Meta:
        model=User
        fields=['username','semail','password','confirm_password']






'''
    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            print('dvcccccccccccccccccccc')
            return HttpResponse( "<html> <script> window.alert('dfavbhj') </script> </html>")



'''
'''       
    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',)
        return password2
'''

    
   
'''
    def clean_confirm_password(self):
        p=self.cleaned_data['password']
        cp=self.cleaned_data['confirm_password']

        if(p!=cp):
            print('okkkkkkkkkkkkkkkkkkkkk kkkkkkkkkkkkkkkkkkk kkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    
            
            raise forms.ValidationError("Confirm Password and Password Must be Same")
        else:
            if(len(p)<8):
                raise forms.ValidationError("Password must be atleast 8 Character")
            if(p.isdigit()):
                raise forms.ValidationError("Password must contains aleast a character")        
'''

class subscribe(forms.ModelForm):
    class Meta:
        model=Email
        fields='__all__'

class feed_form(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'

class con_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'


class Comment_form(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']


class Nested_Comment_form(forms.ModelForm):
    class Meta:
        model=Nested_Comment
        fields=['text']

class donate_form(forms.ModelForm):
    class Meta:
        model=donate
        fields='__all__'
     

        
