# Django Imports
from django.shortcuts import render

# Project Imports
from .forms import ValidationForm
from .utils import is_vendor_available

# Homepage
def home(request):
    form = ValidationForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            vendor_id = form.cleaned_data.get('vendor_id')
            date = form.cleaned_data.get('date')
            if is_vendor_available(vendor_id, date):
                context['availability'] = 'Vendor is available'
            else:
                context['availability'] = 'Vendor is not available'
        else:
            context['error'] = 'Form Not Valid'

    return render(request, 'base.html', context)
