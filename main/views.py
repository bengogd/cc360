from django.shortcuts import render

# Create your views here.

#Home view - index.html
def home(request):
    context = {}
    return render(request, "main/index.html", context)