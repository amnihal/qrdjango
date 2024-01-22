from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . models import Scan,Puzzle




def scanner(request):

    if request.method=="POST":

        qr_data = request.POST.get('qr')
        print('Received data:', qr_data)
        matching_puzzle = Puzzle.objects.filter(Name=qr_data).first()

        if matching_puzzle:
            # If a matching puzzle is found, store the code in Scan model
            qr_code = Scan.objects.create(user=request.user, code=qr_data)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No matching puzzle found'})

    return JsonResponse({'status': 'success'})

def home(request):
    
    return render(request,'scanner.html')

def puzzle(request):
    qr = Scan.objects.filter(user=request.user)

    context = {
        "qr":qr
    }
    
    return render(request,'puzzle.html',context)