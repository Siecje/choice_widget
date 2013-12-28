from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    degree = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        display_txt = '%s, (%s - %s)' % (self.school, self.start_year, self.end_year)
        return display_txt
