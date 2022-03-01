from django import forms
from .models import BlogPost


# creating a form
class PostForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = BlogPost

		# specify fields to be used
		fields = [
			"title",
            "description",
        ]
