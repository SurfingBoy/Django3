from django.test import TestCase

# Create your tests here.
from polls.models import Question

que=Question()
que.question_text('什么水果最好吃')
que.pub_date('2018-04-01')
que.save()
