from django.db import models

# Create your models here.

class Course(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  details = models.TextField()
  prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='required_for')
  image = models.ImageField(upload_to='course_banner/', null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, null=True)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students', null=True)

    def __str__(self):
        return self.name
