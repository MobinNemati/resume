from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse



def base_view(request):
    return render(request, 'resume/index.html', {'name':'Mobin Nemati', 'age':'17',
                                                  'city':'Qazvin', 'education':'Studying (High school)', 'language':'Persian, English'})

