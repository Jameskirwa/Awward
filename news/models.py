from django.db import models

# Create your models here.
class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,categories):
        cls.objects.filter(categories=categories).delete()
        
class technologies(models.Model):
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.technologies

    def save_technology(self):
        self.save()

    @classmethod
    def delete_technology(cls,technologies):
        cls.objects.filter(technologies=technologies).delete()
        
class Project(models.Model):
    title = models.CharField(max_length=150)
    landing_page = models.ImageField(upload_to='landing/')
    description = models.CharField(max_length=255)
    live_link = models.CharField(max_length=255)
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall = models.IntegerField(blank=True,default=0)
    categories = models.ManyToManyField(categories,blank = True)
    technologies = models.ManyToManyField(technologies,blank = True)
    posted  = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects                

