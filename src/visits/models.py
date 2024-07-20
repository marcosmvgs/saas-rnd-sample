from django.db import models

class PageVisit(models.Model):
  # DB table 
  # id hidden column which is primary key autfield 1,2,3,4...
  path = models.TextField(null=True, blank=True) # column
  timestamp = models.DateTimeField(auto_now_add=True) # column
  
