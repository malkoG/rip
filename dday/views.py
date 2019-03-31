from django.shortcuts import render, redirect
from django.db.models.functions import Now

from .models import Dday
from .forms import DdayCreationForm

# Create your views here.
def list_ddays(request):
    ddays = Dday.objects.filter(end_date__gte=Now())

    context = {
        'ddays': ddays
    }

    return render(request, 'dday/list_ddays.html', context)

def create_dday(request):
    if request.method == "POST":
        form = DdayCreationForm(request.POST)

        if not form.is_valid():
            return redirect("dday_creation_view")

        dday = form.save(commit=False)
        dday.who = request.user

        dday.save()

        return redirect("dday_list_view")

    form = DdayCreationForm()

    context = {
        'form': form
    }

    return render(request, 'dday/create_dday.html', context)