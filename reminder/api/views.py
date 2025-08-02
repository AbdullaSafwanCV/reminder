from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from board.models import Reminder
from .serializers import ReminderSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
