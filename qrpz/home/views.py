from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import Puzzle, Scan

# def scan(request):

#     if request.method == "POST":

#         qr_data = request.POST.get('qr')
#         matching_puzzle = Puzzle.objects.filter(Name=qr_data).first()

#         if matching_puzzle:
#             existing_scan = Scan.objects.filter(user=request.user, code=qr_data).first()

#             if existing_scan:
#                 # Provide a message to the user that the code has already been scanned
#                 print('hello')
#             else:
#                 # If a matching puzzle is found, store the code in Scan model
#                 qr_code = Scan.objects.create(user=request.user, code=qr_data)
#                 qr_code_id = qr_code.id
#                 print('hi')

#         return redirect('puzzle')

#     # This line should be indented to be part of the outer function, not inside the "if request.method == 'POST':" block.
#     return render(request, 'scanner.html', {'qr_code_id': qr_code_id})
@login_required
def scan(request):
    if request.method == 'POST':
        qr_data = request.POST.get('qr')
        pz = Puzzle.objects.get(Name=qr_data)

        if pz:
            Scan.objects.create(user=request.user, image=pz.Image)
            return redirect('puzzle')


    return render(request,'scanner.html')



def home(request):
    
    return render(request,'scanner.html')

def puzzle(request):
    qr = Scan.objects.filter(user=request.user)
    context = {
        "qr":qr
    }
     
    return render(request,'puzzle.html',context)


def hello(request):

    return render(request,'hello.html')


