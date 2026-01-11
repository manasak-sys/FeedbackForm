from django import forms

RATING_CHOICES = [
    (1, '1 - Very Poor'),
    (2, '2 - Poor'),
    (3, '3 - Average'),
    (4, '4 - Good'),
    (5, '5 - Excellent'),
]

class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    rating = forms.ChoiceField(
        label="Rating",
        choices=RATING_CHOICES
    )
    comments = forms.CharField(
        label="Comments",
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your feedback...'})
    )
    attachment = forms.FileField(
        label="Attachment (optional)",
        required=False
    )