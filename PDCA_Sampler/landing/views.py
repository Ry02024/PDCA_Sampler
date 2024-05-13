from django.shortcuts import render, redirect
from .forms import InquiryForm
import logging

def inquiry_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thank_you.html')
    else:
        form = InquiryForm()
    return render(request, 'inquiry_form.html', {'form': form})

# landing/views.py
def contact_button_view(request):
    return render(request, 'contact_button.html')

# ロガーを設定
logger = logging.getLogger('contact_clicks')

def contact_click(request):
    # ログ記録
    logger.debug('Contact Us button clicked')
    # お問い合わせフォームページにリダイレクト
    return redirect('inquire')
