from django.db import models
from django.utils import timezone

class Post(models.Model): #Post est le nom de notre modèle models.Model signifie que Post est un modèle Django. Comme ça, Django sait qu'il doit l'enregistrer dans la base de données.
    author = models.ForeignKey('auth.User')#C'est un lien vers un autre modèle.
    title = models.CharField(max_length=200)#champ texte avec un nombre limité de caractères.
    text = models.TextField()#champ texte sans limite de caractères
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True) #le champ en question est une date ou une heure

    def publish(self):# permet de publier le post.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):# renvoient (return) du texte
        return self.title
