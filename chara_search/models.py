from django.db import models

# Create your models here.
class Character(models.Model):
    #player = models.ForeignKey(Player, on_delete=models.CASCADE) <--Potential new feature to connect Characters to player
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    character_class = models.CharField(max_length=20)
    display_name = models.CharField(max_length=50,blank=True)

    def __str__(self):
        objtext = self.display_name
        return objtext

    def save(self, *args, **kwargs):
        self.display_name = self.first_name + " " +  self.last_name
        super(Character, self).save(*args,**kwargs)

class Stats(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    strength = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

    def __str__(self):
        objtext = self.character.display_name
        return objtext
