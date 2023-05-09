from django.db import models


class Note(models.Model):
    champ_id = models.TextField()
    name = models.TextField()
    title = models.TextField()
    maestria = models.TextField()
    imagem = models.TextField()

    def __str__(self):
        return f'{self.id}. {self.title}'