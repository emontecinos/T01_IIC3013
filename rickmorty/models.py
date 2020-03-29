from django.db import models

class Episode(models.Model):
    api_id = models.CharField(max_length=200)
    name = models.CharField(max_length = 200)
    air_date = models.CharField(max_length = 200)
    ep_code = models.CharField(max_length = 200)
    characters = models.CharField(max_length=200)
    api_url = models.CharField(max_length = 200, default="google.cl")


class Location(models.Model):
    api_id = models.CharField(max_length=200)
    name = models.CharField(max_length = 200)
    loc_type = models.CharField(max_length = 200)
    dimension = models.CharField(max_length = 200)
    residents = models.CharField(max_length=200)
    api_url = models.CharField(max_length = 200,default="google.cl")

class Character(models.Model):
    FEMALE = 'FE'
    MALE = 'MA'
    GENDERLESS = 'GE'
    UNKNOWN = 'UN'
    ALIVE = 'AL'
    DEAD = 'DE'
    GENDER_CHOICES = [
        (FEMALE,'Female'),
        (MALE, 'Male'),
        (GENDERLESS, 'Genderless'),
        (UNKNOWN, 'Unknown'),
    ]
    STATUS_CHOICES = [
        (ALIVE,'Alive'),
        (DEAD,'Dead'),
        (UNKNOWN,'Unknown'),
    ]
    api_id = models.CharField(max_length=200)
    name = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200,
        choices = STATUS_CHOICES,
        default = ALIVE,
        )
    species = models.CharField(max_length = 200)
    char_type = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 200,
        choices = GENDER_CHOICES,
        default = UNKNOWN,
        )
    origin = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    image = models.URLField(max_length=200)
    episodes = models.CharField(max_length = 200)
    api_url = models.CharField(max_length = 200,default="google.cl")

