from django.db import models
from django.contrib.contenttypes.models import ContentType


#****************
#teacher
#lesson
#classroom
#zameni
#user
#****************




class name_group(models.Model):
    name = models.CharField(max_length=10)
    group_id = models.CharField(max_length=10)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'

    def get_products(self):
        return lesson.objects.filter(categories__title=self.lesson)

class lesson(models.Model):
    data = models.TextField()
    group = models.CharField(max_length=10)
    number = models.PositiveIntegerField()
    lesson = models.TextField()
    teacher = models.TextField()
    day = models.CharField(max_length=25)
    zam = models.PositiveIntegerField(default=1)
    classroom = models.TextField(default=1)

    

    def __str__(self):
        if self.day == '1':
            self.day = 'Понедiлок'
        elif self.day == '2':
            self.day = 'Вiвторок'
        elif self.day == '3':
            self.day = 'Середа'
        elif self.day == '4':
            self.day = 'Четверг'
        elif self.day == '5':
            self.day = 'Пятниця'
            
        back = str(self.day)+' || '+str(self.group)+' || №'+str(self.number)+'|| Пара - '+str(self.lesson)
        return back

    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'


class lesson_e(models.Model):
    data = models.TextField()
    group = models.CharField(max_length=10)
    number = models.PositiveIntegerField()
    lesson = models.TextField()
    teacher = models.TextField()
    day = models.CharField(max_length=25)
    classroom = models.TextField(default=1)

    

    def __str__(self):
        if self.day == '1':
            self.day = 'Понедiлок'
        elif self.day == '2':
            self.day = 'Вiвторок'
        elif self.day == '3':
            self.day = 'Середа'
        elif self.day == '4':
            self.day = 'Четверг'
        elif self.day == '5':
            self.day = 'Пятниця'



        back = str(self.day)+' || '+str(self.group)+' || №'+str(self.number)+'|| Пара - '+str(self.lesson)
        #print(back)
        return back

    class Meta:
        verbose_name = 'Еталон'
        verbose_name_plural = 'Еталон'

