from django import forms
from .models import Post, Category

#choices = [('theses','theses'),('publications','publications'),('conferences','conferences')]
#choice_list = choices
choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','author',
                'category','body','image','attached_file']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
#           'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','category','body','image','attached_file']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title-tag':forms.TextInput(attrs={'class':'form-control'}),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
        
        