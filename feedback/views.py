from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            # Here you could save to database or send an email
            # For now we just send data to success template
            cleaned_data = form.cleaned_data
            return render(request, 'feedback/feedback_success.html', {
                'data': cleaned_data
            })
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})