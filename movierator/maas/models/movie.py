from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    year = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class WatchList(models.Model):

    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)

class WatchedList(models.Model):

    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)