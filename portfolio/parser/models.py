from django.db import models

#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField("date published")


class Person(models.Model):
    link = models.CharField(max_length=200)#56   https://www.instagram.com/ + name
    name = models.CharField(max_length=30)
    timestamp = models.IntegerField(default=0)

#class Following(models.Model):
#    link = models.CharField(max_length=200)#56   https://www.instagram.com/ + name
#    name = models.CharField(max_length=30)
#    timestamp = models.IntegerField(defa  ult=0)
#
#class Followers(models.Model):
#    link = models.CharField(max_length=200)#56   https://www.instagram.com/ + name
#    name = models.CharField(max_length=30)
#    timestamp = models.IntegerField(default=0)

#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)




# Goals with instagram parser app:
#   First landing page is just file upload
#   then it takes you to second page which outputs the data it parsed out when it downloaded it
#   show relationship with data such as
#   who follows you but you dont follow them
#   who you follow but don't follow you back
#   you can then choose to do more relationship with the data if you choose

