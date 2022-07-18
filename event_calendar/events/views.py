from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from events.models import Event

# Create your views here.

class EventListView(ListView):
    queryset = Event.objects.order_by("ends_at")
    
class EventDetailView(DetailView):
    model = Event
    
class EventCreateView(CreateView):
    model = Event
    fields = ['name', 'description', 'starts_at', 'ends_at']
    
class EventUpdateView(UpdateView):
    model = Event
    fields = ['name', 'description', 'starts_at', 'ends_at']
    
class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('events:events-list')
    
def create_view(request):
    if request.method == 'POST':
        response = ''
        return JsonResponse({'found data': True})