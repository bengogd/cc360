from django.shortcuts import render

# Create your views here.
def ai_personalize(request):
    context = {}
    return render(request, "personalize/personalize.html", context)