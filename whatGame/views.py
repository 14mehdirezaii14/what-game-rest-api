from django.shortcuts import render
from whatGame.models import Ticket
from whatGame.serializers import TicketSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.


@csrf_exempt
def TicketView(request):
    print('log :', request)

    if request.method == 'GET':
        snippets = Ticket.objects.all()
        serializer = TicketSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = request.POST
        print('log <><><><><>', data)
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
