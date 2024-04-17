from salesforce import models
from datetime import date

# Create your models here.


class Account(models.Model):

    name = models.CharField(
        db_column="Name", max_length=255, verbose_name="Account Name"
    )

    billing_street = models.TextField(db_column="BillingStreet", blank=True, null=True)
    is_active = models.CharField(
        db_column="Active__c", max_length=10, blank=True, null=True
    )


class Opportunity(models.Model):
    name = models.CharField(db_column="Name", max_length=120, blank=True, null=True)
    stage_name = models.CharField(
        db_column="StageName", max_length=255, blank=True, null=True
    )
    close_date = models.DateTimeField(
        db_column="CloseDate", null=False, default=date(2024, 1, 1)
    )


class OppTeam(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="OpportunityTeam__c", blank=True, null=True
    )

    class Meta(models.Model.Meta):
        db_table = "OpportunityTeam__c"
        verbose_name = "OppTeam"
        verbose_name_plural = "OppTeam"
