
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserSkill(models.Model):
    user_id = models.IntegerField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'skill')

    def __str__(self):
        return f"User {self.user_id} - {self.skill.name}"
