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
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['title', 'year'], name='uniqueDB')
        # ]
    
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


class Footer(models.Model):
    footerCategory = [('stack', 'stack'), ('links', 'links'), ('developer', 'developer')]
    category = models.CharField(max_length=25, choices=footerCategory)
    title = models.CharField(max_length=25)
    icon = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category', 'title', 'link'], name='uniqueFooter')
        ]

    def __str__(self):
        return self.title
    