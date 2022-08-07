from django.db import models
from django.contrib.postgres.fields import ArrayField

#Customize the model by custom manager
class ClassificationTestManager(models.Manager):
    #Create the classification subject
    def create_classification_test(self, classification_id, annotations, workflow_id, user_id, subject_id):
        self.classification_id=classification_id
        self.annotations = annotations
        self.workflow_id=workflow_id
        self.user_id=user_id
        self.subject_id=subject_id
        classification_subject = self.create(classification_id=self.classification_id, annotation_0=self.annotations[0], annotation_1=self.annotations[1], annotation_2=self.annotations[2], annotation_3=self.annotations[3], workflow_id=self.workflow_id, user_id=self.user_id, subject_id=self.subject_id)
        return classification_subject

#Create the Django model
class ClassificationTest(models.Model):
    """The frame work for a single Gravity Spy annotation/classification from a volunteer
    id is 420780262
    annotation is [{'task': 'T0', 'value': [{'x': 401.2159729003906, 'y': 1486.4444580078125, 'tool': 0, 'frame': 0, 'details': []}]}]
    workflow is 21793
    user is 386563
    subject is 76084855    
    """
    #Field defining
    classification_id = models.IntegerField()
    annotation_0 = ArrayField(models.IntegerField())
    annotation_1 = ArrayField(models.IntegerField())
    annotation_2 = ArrayField(models.IntegerField())
    annotation_3 = ArrayField(models.IntegerField())
    workflow_id = models.IntegerField()
    user_id = models.IntegerField()
    subject_id = models.IntegerField()
    ##project_id?

    #Add a method on custom manager
    objects = ClassificationTestManager()

