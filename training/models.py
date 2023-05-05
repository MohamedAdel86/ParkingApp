from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class User_Model(models.Model):
    Userkey = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, default="")
    phone_no = models.IntegerField(null=True)
    email = models.EmailField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    birthdate = models.DateField(null=True)
    reservation_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.Name)

class Parking_spot(models.Model):
    Name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    price = models.IntegerField()
    parkingphoto = models.ImageField(upload_to='images/')


class Worker(models.Model):
    worker_id = models.OneToOneField(User_Model, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(Parking_spot, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.worker_id.Name)




class Admin_user(models.Model):
    Userkey = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, default="")



class Reservation(models.Model):
    Date = models.DateTimeField(max_length=30, null=True)
    parking_spot = models.ForeignKey(Parking_spot, on_delete=models.CASCADE, null=True, blank=True, related_name='related_to_foreign_key_1')
    User_Model = models.ForeignKey(User_Model, on_delete=models.CASCADE, null=True,  blank=True, related_name='related_to_foreign_key_2')
    price = models.IntegerField(max_length=10)

    def __str__(self):
        return str(self.id)

class Contention(models.Model):
    user_id = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    nominee_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    reason = models.TextField()
    

# singletonPatern

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get(pk=1)
        except ObjectDoesNotExist:
            return cls()



class Control_content(SingletonModel):
    nomination = models.BooleanField(default=False)
    vote = models.BooleanField(default=False)
    contention = models.BooleanField(default=False)
    result = models.BooleanField(default=False)

    def __str__(self):
        return 'Control Content'

    class Meta:
        verbose_name_plural = "Control Content"
