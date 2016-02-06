from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

class Problem(models.Model):
    problem_text = models.CharField(max_length=200)
    cur_score = models.IntegerField(default=0)
    num_problems = models.IntegerField(default=1)
    def __str__(self):
    	return self.problem_text

class Answer(models.Model):
	problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True)
	is_correct = models.BooleanField(default=False)
	answer_text = models.CharField(max_length=200)
	def __str__(self):
		return self.answer_text