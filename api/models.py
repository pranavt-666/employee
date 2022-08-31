from django.db import models

class employees(models.Model):
    name = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    salary = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='employee_images',null=True)

    def __str__(self):
        return self.name

        