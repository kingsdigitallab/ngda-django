from django.shortcuts import render_to_response, render
from django.http import JsonResponse
from archives.models import TransationEvents
import json

# Create your views here.


def home(request):
    return render_to_response('base.html')


def fullTransactionRecord(request, t_id):
    id = t_id
    t = TransationEvents.objects.get(pk=id)
    context = {}
    context['transaction'] = t
    return render(request, 'archives/transaction_page.html', context)


def timeGraphRequest(request, gType, gQuery):
    if gType == 'genre':
        return genreJson(gQuery)



def genreJson(q):
    graph = {'data':{'x':'x', 'columns':[['x'],['price']]},\
             'axis':{'x':{'type':'timeseries',\
             'tick':{'format':'%Y-%m-%d'},\
             }}\
             }
    tws = TransationEvents.objects.filter(work__genre__name=q)
    for t in tws:
        if t.sold_date is not None and t.sold_pounds is not None: 
        #try:
            graph['data']['columns'][0].append(t.sold_date.isoformat())
            graph['data']['columns'][1].append(t.sold_pounds)
        #except Exception():
        #    pass
    return JsonResponse(graph)


    
