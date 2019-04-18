# iot_data/models.py

from django.db import models
from channels.models import Channel,User

# Create your models here.

class IotData(models.Model):
<<<<<<< HEAD
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE,related_name='iotdata')
    timestamp = models.DateTimeField(auto_now_add=True)
    channel_num = models.PositiveSmallIntegerField()
=======
    created_at = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel,on_delete=models.SET_NULL,related_name='iotdata')
>>>>>>> 0ba43668421ede56fb066d8f6ed11d0995a7f988
    field_num = models.PositiveSmallIntegerField()
    data = models.DecimalField(max_digits=19, decimal_places=10)
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='iotdata')
    
    # unclear to ZK what this is for? when could it be entered false?
    upload_success = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.created_at} channel: {self.channel_num} field: {self.field_num} data: {self.data}'
