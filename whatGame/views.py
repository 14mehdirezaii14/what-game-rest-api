from django.shortcuts import render
from whatGame.models import Ticket
from whatGame.models import EscapeRoom
from whatGame.models import disableDate
from whatGame.serializers import TicketSerializer
from whatGame.serializers import EscapeRoomSerializer
from whatGame.serializers import disableDateSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json


@csrf_exempt
def EscapeRoomView(request):
    if request.method == 'GET':
        snippets = EscapeRoom.objects.all()
        serializer = EscapeRoomSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


def getDisableDate(request):
    if request.method == 'GET':
        print("<><><><><><><>", request.GET.get('idGame'))
        snippets = disableDate.objects.filter(idGame=request.GET.get('idGame'))
        serializer = disableDateSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def TicketView(request):
    if request.method == 'GET':
        print(request)
        snippets = Ticket.objects.filter(date=request.GET.get(
            'date'), idGame=request.GET.get('idGame'))
        print('<><><><><><>', snippets)
        print('<><><><><><>', request.GET.get('date'))
        print('<><><><><><>', request.GET.get('idGame'))
        serializer = TicketSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        dataa = request.POST
        serializer = TicketSerializer(data=dataa)
        #
        print("<><><><><><><><>", Ticket.objects.filter(
            date=dataa["date"]).__len__())
        if Ticket.objects.filter(date=dataa["date"]).__len__() >= 7:
            return JsonResponse({"err": "در این تاریخ تمامی سانس ها رزرو شده"}, status=400)
        if Ticket.objects.filter(date=dataa["date"]).__len__() >= 6:
            instanceEscapeRoom = EscapeRoom.objects.get(
                id=dataa["idGame"])
            disableDate.objects.create(
                idGame=instanceEscapeRoom, date=dataa["date"])
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({'data': 'ok'}, status=201)

        #
        elif serializer.is_valid():
            serializer.save()
            print('log <><><><><>', request)
            return JsonResponse({'data': 'ok'}, status=201)
        else:
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


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify/'


def send_request(request):
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    print('log <><><><><>', req.json())
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(
            req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                return HttpResponse('Transaction success.\nRefID: ' + str(
                    req.json()['data']['ref_id']
                ))
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return HttpResponse('Transaction failed or canceled by user')
