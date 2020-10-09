from django.db import models

class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""

        return self.text


class Entry(models.Model):
    '''学习到有关某个主题的具体知识'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''返会模型的字符串表示'''

        if len(self.text) < 50:
            return self.text + '.'
        else:
            return self.text[:50] + '...'

class Pizza(models.Model):
    '''披萨店的披萨名称'''
    name = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''返回披萨的名称'''

        return self.name

class Topping(models.Model):
    '''披萨配料'''
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        '''返回模型的字符串表示'''

        return self.name + '.'