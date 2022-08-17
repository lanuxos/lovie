from django.db import models
from django.urls import reverse

class Matabase(models.Model):
    title = models.CharField(max_length=200, help_text="Enter movies' title")
    year = models.CharField(max_length=4, help_text="Enter released year, eg: xxxx")
    choices = (
        ('d', 'Downloaded'),
        ('w', 'Watched'),
        ('r', 'Removed'),
    )
    status = models.CharField(max_length=10, choices=choices, default='d', help_text="d: Downloaded, w: Watched, r: Removed")
    
    createdDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-createdDate', 'title']
    
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.title + " [" + str(self.year) + "]"

class Mag(models.Model):
    '''
    action, adventure, animated, 
    comedy, crime, 
    drama, detective, documentary,
    epics,
    fantasy, 
    gangster,
    historical, horror, 
    musical, mystery,
    noir, 
    period,
    romance, 
    science fiction, superhero, supernatural
    thriller, 
    war, western,
    zombie,
    '''
    magReference = models.ForeignKey(Matabase, on_delete= models.CASCADE)
    mag = models.CharField(max_length=50)

    class Meta:
        ordering = ['magReference']

    def __str__(self):
        return f'{self.magReference.title} [{self.mag}]'