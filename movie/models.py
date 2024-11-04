from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(15), MaxValueValidator(110)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    STATUS = (
        ('pro', 'Pro'),
        ('simple', 'Simple')
    )
    status = models.CharField(max_length=10, choices=STATUS, default='simple')

    def __str__(self):
        return self.username


class Country(models.Model):
    objects = None
    country_name = models.CharField(max_length=40)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=16)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    director_image = models.ImageField(upload_to='img/', verbose_name='Image', null=True, blank=True)

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=16, unique=True)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MaxValueValidator(150)])
    actor_image = models.ImageField(upload_to='img/', verbose_name='Image', null=True, blank=True)

    def __str__(self):
        return self.actor_name


class Janre(models.Model):
    janre_name = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.janre_name}'


class Movie(models.Model):
    movie_name = models.CharField(max_length=95)
    year = models.DateField(auto_now_add=True)
    country = models.ManyToManyField(Country, related_name='country_movie')
    director = models.ManyToManyField(Director, related_name='director_movie')
    actor = models.ManyToManyField(Actor, related_name='actor')
    janre = models.ManyToManyField(Janre, related_name='janre_movie')
    TYPES = (
        ('144p', '144p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    )
    types = models.CharField(max_length=10, choices=TYPES, default='144p')
    movie_time = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='trailer', verbose_name='Trailer', null=True, blank=True)
    movie_image = models.ImageField(upload_to='img/', verbose_name='movie_image', null=True, blank=True)
    STATUS_MOVIE = (
        ('pro', 'Pro'),
        ('simple', 'Simple')
    )
    status_movie = models.CharField(max_length=10, choices=STATUS_MOVIE, default='simple')

    def __str__(self):
        return f'{self.movie_name}'


class MovieLanguages(models.Model):
    language = models.CharField(max_length=25)
    video = models.FileField (upload_to='video/', verbose_name='Video', null=True, blank=True)
    movie = models.ForeignKey(Movie, related_name='movie', on_delete=models.CASCADE)


class Moments(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_moments', on_delete=models.CASCADE)
    movie_moments = models.FileField (upload_to='img/', verbose_name='epizods', null=True, blank=True)


class Rating(models.Model):
    user = models.ForeignKey(Profile, related_name='user_rating', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_rating', on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)], verbose_name='stars')
    parent =  models.ForeignKey('self', related_name='replies', null=True, blank=True,
                                on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.text}-{self.created_date}'


class Favorite(models.Model):
    user = models.OneToOneField(Profile, related_name='user_favorite', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, related_name='cart_favorite', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_favorite', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie}'


class History(models.Model):
    user = models.ForeignKey(Profile, related_name='user_history', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='movie_history', on_delete=models.CASCADE)
    viewed_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'










