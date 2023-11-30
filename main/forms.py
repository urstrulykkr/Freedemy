
from django import forms
from .models import Course

# Define a form for editing course details
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        # Specify the fields from the Course model to be included in the form
        fields = ('title', 'description', 'thumbnail', 'featured_video', 'level', 'duration', 'category', 'requirements', 'content', 'lesson_title', 'lesson_video')

# Define a form for searching courses
class CourseSearchForm(forms.Form):
    # Create a text input field for entering search queries with a maximum length of 100 characters
    search_query = forms.CharField(max_length=100, label='Search', required=False)
