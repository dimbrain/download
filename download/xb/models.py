from django.db import models


class Thread(models.Model):
    thread_id = models.IntegerField()
    start_page = models.IntegerField()
    end_page = models.IntegerField()
    in_progress = models.BooleanField()
    is_error = models.BooleanField()

    def __str__(self):
        return '{0} : from {1} to {2}'.format(self.thread_id, self.start_page, self.end_page)


class Image(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=500)

    def get_image_url(self):
        return self.image_url

    def get_thumbnail_url(self):
        return self.image_url.__str__().replace('/i/','/t/')
