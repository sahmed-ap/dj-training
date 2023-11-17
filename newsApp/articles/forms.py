from django import forms


class ArticlePostForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    is_published = forms.BooleanField(required=False)

    # def clean_title(self):
    #     """method to check data is valid or not"""
    #     _article_title = self.cleaned_data['title']
    #     if _article_title != "abc":
    #         raise forms.ValidationError("Title is not correct")


class SigunupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    
    