from django.shortcuts import render

# Create your views here.
def gig_csr(request):
    context = {}
    return render(request, "representative/gig_csr.html", context)
