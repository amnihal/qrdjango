from django.http import HttpResponse, JsonResponse
from django.shortcuts import render




def scanner(request):

    qr_data = request.POST.get('qr')
    print('Received data:', qr_data)

    return JsonResponse({'status': 'success'})

def home(request):
    
    return render(request,'scanner.html')

def puzzle(request):
    
    return render(request,'puzzle.html')