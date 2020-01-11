from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)

	image= models.ImageField(default='default.png',upload_to='profile_pics')

	bio= models.CharField(max_length=200,default="No bio")

	def __str__(self):

		return f'{self.user.username} Profile'

class Follow(models.Model):
      following = models.ForeignKey(User, related_name="who_follows",on_delete=models.CASCADE)
      follower = models.ForeignKey(User, related_name="who_is_followed",on_delete=models.CASCADE)
      follow_time = models.DateTimeField(auto_now=True)

      def __unicode__(self):
          return str(self.follow_time)

      def __str__(self):
      
          return "{} follows {}".format(self.following,self.follower)        

