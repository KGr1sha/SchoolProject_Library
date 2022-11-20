from django.db import models

CLASS_NUMBER_CHOICES = [
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
]


class Book(models.Model):

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    class_number = models.IntegerField(choices=CLASS_NUMBER_CHOICES)

    def __str__(self):
        return self.name + ' ' + self.author + ' ' + str(self.class_number)


class Student(models.Model):
    CLASS_INDEX_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ]

    FIO = models.CharField(max_length=200)
    class_number = models.IntegerField(choices=CLASS_NUMBER_CHOICES)
    class_index = models.IntegerField(choices=CLASS_INDEX_CHOICES)

    def __str__(self):
        return self.FIO + ' ' \
               + str(self.class_number) + '-' \
               + str(self.class_index)




