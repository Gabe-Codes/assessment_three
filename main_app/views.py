from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Sum
from .models import Widget
from .forms import WidgetForm

def home(request):
    widgets = Widget.objects.all()
    total = widgets.aggregate(Sum('quantity'))
    widget_form = WidgetForm()
    return render(request, 'home.html', {
        'widgets': widgets,
        'widget_form': widget_form,
        'total': total['quantity__sum']
    })

def widget_create(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home')


def widget_delete(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('home')