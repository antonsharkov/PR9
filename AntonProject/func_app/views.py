from django.http import HttpResponse
import massivs
import scipy

# Create your views here.

def index(request, a, b, c, d):
    return HttpResponse(f"Начальный массив: {scipy.array([[a, b], [c, d]])} \n Измененный массив: {massivs.massivs(a, b, c, d)}")