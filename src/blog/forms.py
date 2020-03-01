from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance  # get the Object from BlogPost which we are working on
        title = self.cleaned_data.get('title')

        qs = BlogPost.objects.filter(title=title)
        if instance is not None:
            # To exclude the instace from the querryset qs
            qs = qs.exclude(pk=instance.pk)  # id = instance.id
        if qs.exists():
            print("Exist")
            raise forms.ValidationError(
                "This title has already been used. Please try again.")
        return title
