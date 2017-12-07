from django.shortcuts import render_to_response, render
from archives.models import TransationEvents

# Create your views here.


def home(request):
    return render_to_response('base.html')


def fullTransactionRecord(request, t_id):
    id = t_id
    t = TransationEvents.objects.get(pk=id)
    context = {}
    context['transaction'] = t
    return render(request, 'archives/transaction_page.html', context)
