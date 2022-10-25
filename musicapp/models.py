from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank = True)
    age = models.IntegerField(blank=True)

    def __str__(self):
        return self.first_name 

    



class Song(models.Model):
    title = models.CharField(max_length=100, blank=True)
    date_released = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    artist_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.title




class Lyric(models.Model):
    content = models.CharField(max_length=1000000) 
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
    