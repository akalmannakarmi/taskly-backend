from django.db import models
from user.models import CustomUser

# Create your models here.
class Task(models.Model):
    PRIORITY = [
        (-2,"Lowest"),
        (-1,"Low"),
        (0,"Normal"),
        (1,"High"),
        (2,"Highest"),
    ]
    STATUS = [
        (0,"Pending"),
        (1,"Active"),
        (2,"On-Hold"),
        (3,"Complete"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY, default=0)
    points = models.IntegerField(default=0)
    progress = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    start_date = models.DateField(null=True)
    deadline_date = models.DateField(null=True)