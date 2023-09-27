from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name + " " + self.email


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    has_access = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.has_access:
            return self.user.name + " has access to " + self.product.name
        else:
            return self.user.name + " does not have access to " + self.product.name


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    video_link = models.URLField()
    duration = models.IntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.name + " " + str(self.duration)


class LessonStatus(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)
    viewed_time = models.IntegerField(default=0)
    last_viewed_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if not self.viewed:
            return self.user.name + " has not viewed " + self.lesson.name
        else:
            return self.user.name + " has viewed " + self.lesson.name
