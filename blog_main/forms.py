from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']

    
    def clean_username(self):
        uname = self.cleaned_data['username']
        errors = []
        if len(uname) < 4:
            errors.append("Username must be at least 4 characters long.")
        if len(uname) > 10:
            errors.append("username can't be greater than 10 characters")
        if bool(re.match(r'^\d', uname)):
            errors.append("username can't be started with a digit")
        regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
        if regex.search(uname) != None:
            errors.append("Username cannot contain special characters.")
        if errors:
            raise forms.ValidationError(errors)
        return uname
    
    '''
    Email Validation Rules
    A valid email must follow these conditions 

    Format must be username@company.domain

    Username can contain letters, numbers, dashes, and underscores and a dot

    Company name can contain letters and numbers only

    Domain can contain lowercase letters only

    Domain extension length must be 1-3 character
    '''
    

    def clean_email(self):
        errors_email = []
        
        email = self.cleaned_data['email']
        if '@' not in email or email.count('@') != 1:
            errors_email.append("Must contain exactly one @ symbol")
        
        username, domain_part = email.split('@')
        
        if '.' not in domain_part or domain_part.count('.') != 1:
            errors_email.append("Domain must contain exactly one dot")
        
        company, domain = domain_part.split('.')
        
        # Validate username
        if not re.match("^[a-zA-Z0-9-_.]+$", username):
            errors_email.append("Username contains invalid characters")
        
        # Validate company
        if not re.match("^[a-zA-Z0-9]+$", company):
            errors_email.append("Company name contains invalid characters")
        
        # Validate domain
        if not re.match("^[a-z]{1,3}$", domain):
            errors_email.append("Domain must be 1-3 lowercase letters")
        if errors_email:
            raise forms.ValidationError(errors_email)
        return email
     
    ''' passqord validation rule

        Have at least one number
        Have at least one uppercase letter
        Have at least one lowercase letter
        Have at least one special character ($, @, #, %)
        Be between 6 and 20 characters in length
        password and confirm password should be same.

    '''

    def clean_password1(self):
        
        pswd1 = self.cleaned_data['password1']
        #pswd2 = self.cleaned_data['password2']
        SpecialSym = ['$', '@', '#', '%']
        error_pswd = []
        if len(pswd1) < 6:
            error_pswd.append('Length should be at least 6')
        if len(pswd1) > 20:
            error_pswd.append('Length should not be greater than 20')
        if not any(char.isdigit() for char in pswd1):
            error_pswd.append('Password should have at least one numeral')
        if not any(char.isupper() for char in pswd1):
            error_pswd.append('Password should have at least one uppercase letter')
        if not any(char.islower() for char in pswd1):
            error_pswd.append('Password should have at least one lowercase letter')
           
        if not any(char in SpecialSym for char in pswd1):
            error_pswd.append('Password should have at least one of the symbols $@#%')
        if  error_pswd:
            raise forms.ValidationError(error_pswd)  
        return pswd1

    def clean_password2(self):
        pswd1 = self.cleaned_data.get("password1")
        pswd2 = self.cleaned_data.get("password2")

        if pswd1 and pswd2 and pswd1 != pswd2:
            raise forms.ValidationError("Passwords do not match.")

        return pswd2