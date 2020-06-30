from django.db import models

# Create your models here.



class CreateGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=False)
    timestamp = models.DateField(auto_now=True, auto_now_add=False)
    slug = models.CharField(max_length=250)


    def __str__(self):
        return str(self.name) 


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey('CreateGroup',on_delete=models.CASCADE)
    comment = models.CharField(default = "-",max_length=100)
    question_file = models.FileField(upload_to='question/documents/',blank=True, null=True)
    cover = models.ImageField(upload_to='question/covers/', null=True, blank=True)
    created_at = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.group_id) +' || ' + self.comment
    
    
    def delete(self, *args, **kwargs):
        self.question_file.delete()
        super().delete(*args, **kwargs)

