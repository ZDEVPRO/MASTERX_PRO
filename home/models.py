from django.db import models


class Mijozlar_New(models.Model):
    name = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    master = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    message = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return '%s - %s - %s - %s' % (self.name, self.service, self.master, self.date)

class Aloqa_New(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500)

    def __str__(self):
        return '%s - %s -%s' % (self.name, self.subject, self.phone)


