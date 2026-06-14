from django.db import models

class Task(models.Model):

    CATEGORY_CHOICES = (
        ('Health', 'Health'),
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Personal', 'Personal'),
    )

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    completed = models.BooleanField(default=False)

    due_date = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title