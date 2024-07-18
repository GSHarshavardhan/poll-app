from django.db import models


class Poll(models.Model):
    question_text = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name= 'choices', on_delete= models.CASCADE)
    choice_text = models.CharField(max_length= 256)
    vote_count = models.IntegerField(default= 0)

    def __str__(self) -> str:
        return self.choice_text
