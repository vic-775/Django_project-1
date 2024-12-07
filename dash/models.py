from django.db import models
from sklearn.tree import DecisionTreeClassifier
from django.core.validators import MinValueValidator, MaxValueValidator
import joblib
# Create your models here.
GENDER = (
    (0,'Female'), (1, 'Male')
)

class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(12),MaxValueValidator(20)], null=True)
    sex = models.PositiveBigIntegerField(choices=GENDER,null=True)
    height = models.PositiveSmallIntegerField(null=True)
    predictions = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        ml_model = joblib.load('models/sport_ml_model.joblib')
        self.predictions = ml_model.predict([[self.age, self.height, self.sex]])
        return super().save(*args, *kwargs)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        return self.name
        
    