from django.http import JsonResponse
from django.shortcuts import render
import math

def index(request):
    return render(request, 'App/index.html')

def calculate_emi(request):
    if request.method == 'POST':
        principal = float(request.POST['principal'])
        rate = float(request.POST['rate'])
        time = float(request.POST['time'])
        
        monthly_rate = rate / (12 * 100)
        months = time * 12
        emi = (principal * monthly_rate * math.pow(1 + monthly_rate, months)) / (math.pow(1 + monthly_rate, months) - 1)
        
        return JsonResponse({'emi': round(emi, 2)})

    return JsonResponse({'error': 'Invalid request'}, status=400)
