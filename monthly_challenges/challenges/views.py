from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "This is a view for January!",
    "february": "This is a view for February!",
    "march": "This is a view for March!",
    "april": "This is a view for April!",
    "may": "This is a view for May!",
    "june": "This is a view for June!",
    "july": "This is a view for July!",
    "august": "This is a view for August!",
    "september": "This is a view for September!",
    "october": "This is a view for October!",
    "november": "This is a view for November!",
    "december": None,
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })

"""
    for month in months: 
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args = [month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
"""
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Month not found")

    forward_month = months[month -1]
    forward_path = reverse("month_challenge", args= [forward_month]) #/challenge
    return HttpResponseRedirect(forward_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month
        })
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)
    except:
        raise Http404()
        #response_data = render_to_string("404.html")
        #return HttpResponseNotFound(response_data)
    