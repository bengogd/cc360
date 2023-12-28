from django.shortcuts import render

# Create your views here.
def ai_help_desk(request):
    context = {}
    return render(request, "chatbot/ai_chatbot.html", context)
