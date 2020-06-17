from django.db import models

# Create your models here.
# Classes are used to define the database 

class Question(models.Model):
    # A char field is charactars with max len(text) == 200
    question_text = models.CharField(max_length=200)
    # Date Field 
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        # To return the string if printed in terminal
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # The use of a Foreign Key. That tells Django each Choice is related to a 
    # single Question. Django supports all the common 
    # database relationships: many-to-one, many-to-many, and one-to-one.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
