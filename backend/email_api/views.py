
from django.shortcuts import render
from django.http import JsonResponse
from .utils import analyze_email
from .models import EmailAnalysis

def home(request):
    return render(request, "index.html")

def analyze(request):
    if request.method == "POST":
        text = request.POST.get("email_text","")
        result = analyze_email(text)
        EmailAnalysis.objects.create(
            content=text,
            classification=result["classification"],
            confidence=result["confidence"],
            keywords=",".join(result["keywords"])
        )
        return JsonResponse(result)
