import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


# Create your models here.

class Deal(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=False, max_length=200)

    def __str__(self):
        return self.name


'''
class Contact(models.Model):
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(primary_key=True, unique=True, blank=False, max_length=200)
    message = models.TextField(blank=False, max_length=200)
    not_a_robot = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.email

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class TimeEntry(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

lender = bank profile, non bank, credit union, life insurance company,
products = sba - 7a, equipment, mortgage, working cap, letters of credit,
geography = northeast,
    county =
industry = medical, manufacturing,
loan_backed_by = nursing home, hotel, apartment building (garden or highrise),
property =



junior lender - makes a profile
    todd lender
    jr loan officer




initial terms vs closing terms

lender



for windsor - build a team - admin at top, processor, underwriter, closer, relationship manager (sales)



sean's team is all 3 for the bank...has a credit committee,



lets say im adding a deal
    common modules -
    2 ways for a borrower to get on platform -invited by bank or broker
        borrower comes in, i need to upload these docs
        9/10 times will delegate to other people....instead of email chain, invites users to the deal

            bank team will always be the same...different deals and different loan officers

        borrower will invite different people
        back office will invite other people based on the deal
            title



marketplace modules -
    bizbuysell sucks - as a banker, its so public.
    goal - make a private network



lender modules -
workflow module
PFS (personal financial statement) module
Integrations


if we build it in a way where the PFS is verifiying, buyer screening - digital buyer due diligence
    4506T verifications
        tax form - veritax
    soft credit pull
    banks make you fit into their box.

every borrower should know its for the professional, not for them
'''
