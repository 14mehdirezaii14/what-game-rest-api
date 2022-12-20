from django.shortcuts import render
from whatGame.models import Ticket
from whatGame.serializers import TicketSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# Create your views here.



@csrf_exempt
def TicketView(request):
    print('log :', request)

    if request.method == 'GET':
        snippets = Ticket.objects.all()
        serializer = TicketSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        dataa = request.POST
        print('log <><><><><>', dataa)
        serializer = TicketSerializer(data=dataa)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"data": "ok"}, status=201)
        return JsonResponse(serializer.errors, status=400)


# class TicketView(APIView):
#     def get(selfself, request):
#         snippets = Ticket.objects.all()
#         serializer = TicketSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request, format=None):
#         serializer = TicketSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({"data": "ok"}, status=201)
#         return JsonResponse(serializer.errors, status=400)
