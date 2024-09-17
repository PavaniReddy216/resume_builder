from django import forms


class ResumeForm(forms.Form):
  
   education = forms.CharField(widget=forms.Textarea, required=True)
   skills = forms.CharField(widget=forms.Textarea, required=True)
   internships = forms.CharField(widget=forms.Textarea, required=True)
   projects = forms.CharField(widget=forms.Textarea, required=True)
   experience = forms.CharField(widget=forms.Textarea, required=False)
class personaldetails(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100, required=True)
    email = forms.EmailField(label='Email Address', required=True)
    mobile_number = forms.CharField(label='Mobile Number', max_length=15, required=True)
    linkedin_id = forms.URLField(label='LinkedIn ID', required=False)
    github_id = forms.URLField(label='GitHub ID', required=False)
    address = forms.CharField(label='Address', widget=forms.Textarea, required=True)
