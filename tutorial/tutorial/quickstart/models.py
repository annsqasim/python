from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    SEVERITY = (
        (1, 'Major'),
        (2, 'Critical'),
        (3, 'Minor')
    )
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, blank=True, default='')
    severity = models.CharField(max_length=20,choices=SEVERITY, default='')
    assignee = models.ForeignKey('auth.user', related_name='assignee')
    reporter = models.ForeignKey('auth.user', related_name='reporter')
    is_done = models.BooleanField(default=False)
    donedate = models.DateTimeField(null=True)