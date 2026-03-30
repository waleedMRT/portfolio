from django.db import models

class ProfileImage(models.Model):
    profile_image = models.ImageField(upload_to='photos/%y/%m/%d' , blank=True , null=True)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='pphotos/%y/%m/%d', blank=True, null=True)
    technologies = models.CharField(max_length=250 , help_text="فصل كل تقنية بفاصلة")
    project_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def tech_list(self):
        """ترجع قائمة بالتقنيات مفصولة بفاصلة"""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []

# Create your models here.
