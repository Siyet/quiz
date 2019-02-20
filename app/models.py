from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    # icon = models.ImageField(upload_to='media/icons/', verbose_name="Иконка")
    is_public = models.BooleanField(verbose_name="Опубликован?")

    def __str__(self):
        return self.title

    def get_public_answers_count(self):
        return self.questions.filter(is_public=True).count()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="questions", verbose_name="Категория")
    text = models.CharField(max_length=255, verbose_name="Текст вопроса")
    image = models.ImageField(upload_to='media/images/', verbose_name="Картинка ответ", blank=True)
    short_image = models.ImageField(upload_to='media/images/', verbose_name="Картинка вопрос", blank=True)
    is_public = models.BooleanField(verbose_name="Опубликован?", default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers", verbose_name="Вопрос")
    text = models.CharField(max_length=255, verbose_name="Текст ответа")
    is_true = models.BooleanField(verbose_name="Верный ответ?")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class Team(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    order_num = models.PositiveSmallIntegerField(default=0, verbose_name="Порядковый номер")
    points = models.PositiveSmallIntegerField(default=0, verbose_name="Количество очков")
    games_num = models.PositiveSmallIntegerField(default=0, verbose_name="Отыграно раундов")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ['games_num', 'order_num']


class Options(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование")
    value = models.CharField(max_length=255, verbose_name="Значение")

    class Meta:
        verbose_name = "Опция"
        verbose_name_plural = "Опции"
    