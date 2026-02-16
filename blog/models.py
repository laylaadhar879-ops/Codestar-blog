from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    ticket_holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_tickets"
    )
    date_issued = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )

    def __str__(self):
        return f"Ticket for {self.ticket_holder}"
