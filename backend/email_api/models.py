
from django.db import models
class EmailAnalysis(models.Model):
    content = models.TextField()
    classification = models.CharField(max_length=20)
    confidence = models.FloatField()
    keywords = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
