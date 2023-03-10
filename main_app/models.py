from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    date_posted=models.DateField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Todo'
    def __str__(self):
        return self.title
    