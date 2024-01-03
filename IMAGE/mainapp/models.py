from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'images')
    emotion = models.CharField(max_length = 50 , blank = True)
    uploaded_at = models.DateTimeField(auto_now=True)

    # def save(self , *args , **kwargs):
    #     local_tz = pytz_timezone(str(timezone.get_current_timezone()))
    #     self.uploaded_at = timezone.localtime(self.uploaded_at , local_tz)
    #     super(Image , self).save(*args , **kwargs)


  








   
    



    


