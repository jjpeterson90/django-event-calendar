from django.urls import path, include
from .views import EventListView, EventCreateView, EventDetailView, EventUpdateView, EventDeleteView

app_name = 'events'

urlpatterns = [
    path('events/', EventListView.as_view(), name='events-list'),
    path('events/new', EventCreateView.as_view(), name='events-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='events-detail'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='events-update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='events-delete'),
]
