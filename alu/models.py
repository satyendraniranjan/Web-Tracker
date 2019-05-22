from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from django.utils import timezone
import datetime



class ALUCounts(models.Model):
        name = models.CharField(max_length=30, unique=True)
        description = models.CharField(max_length=100)

        def __str__(self):
                return self.name

        def get_tracker_count(self):
                date_from = datetime.datetime.now() - datetime.timedelta(days=1)
                return AluPostComTracker.objects.filter(board=self, Date__gte=date_from).count()
#                return Tracker.objects.filter(board=self).extra({'date_created' : "date(Date)"}).values('date_created').annotate(created_count=Count('id'))


class AluProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
            return self.user.username

    def get_tracker_count(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)).count()

    def get_activity_count11(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self) & Q(Site_Activity_Type='Cabinet Swap')).count()

    def get_activity_count1(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='Change In SAMB')).count()

    def get_activity_count2(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='Health Check')).count()

    def get_activity_count3(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='LAM Testing')).count()

    def get_activity_count4(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='LATP/FATP Testing')).count()

    def get_activity_count5(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='Cabinet Swap')).count()

    def get_activity_count6(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='Mini M Decom Macro')).count()

    def get_activity_count7(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='New Integration')).count()

    def get_activity_count8(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='Relo Site')).count()

    def get_activity_count9(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='Technology ADD')).count()

    def get_activity_count10(self):
            return AluPostComTracker.objects.filter( Q(Assignee=self)& Q(Site_Activity_Type='Troubleshooting')).count()


"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        AluProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""

class AluPostComTracker(models.Model):
        admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')
        cascade = models.CharField(max_length=255, default='')
        Assignee = models.ForeignKey(AluProfile, on_delete=models.CASCADE, related_name='aluprofile')
        board = models.ForeignKey(ALUCounts, related_name='alucounts', on_delete=models.CASCADE, null=True)

        Technology_CHOICES1 = (
                ('800 CDMA', '800 CDMA'),
                ('1900 CDMA', '1900 CDMA'),
                ('800 FDD', '800 FDD'),
                ('1900 FDD', '1900 FDD'),
                ('2.5 TDD', '2.5 TDD'),
                ('700 FDD', '700 FDD'),
        )

        Technology = models.CharField(max_length=255, choices=Technology_CHOICES1)

        Type_OEM8 = (
                ('Airscale', 'Airscale'),
                ('ALU', 'ALU'),
                ('NSN', 'NSN'),
        )

        OEM = models.CharField(max_length=255, choices=Type_OEM8, blank=True)


        market = (
                ('Kansas', 'Kansas'),
                ('Alaska', 'Alaska'),
                ('PR / VI', 'PR / VI'),
                ('DFW', 'DFW'),
                ('East Texas', 'East Texas'),
                ('Inland Northwest', 'Inland Northwest'),
                ('Albuquerque', 'Albuquerque'),
                ('Jacksonville', 'Jacksonville'),
                ('Nashville', 'Nashville'),
                ('West Texas', 'West Texas'),
                ('Washington DC', 'Washington DC'),
                ('East Iowa', 'East Iowa'),
                ('MT / WY', 'MT / WY'),
                ('South Carolina', 'South Carolina'),
                ('Riverside / San Bernardino', 'Riverside / San Bernardino'),
                ('East Kentucky', 'East Kentucky'),
                ('Alabama', 'Alabama'),
                ('West Kentucky', 'West Kentucky'),
                ('Dakotas', 'Dakotas'),
                ('Orlando', 'Orlando'),
                ('Central Iowa', 'Central Iowa'),
                ('Georgia', 'Georgia'),
                ('Missouri', 'Missouri'),
                ('Lower Central Valley', 'Lower Central Valley'),
                ('Atlanta / Athens', 'Atlanta / Athens'),
                ('Southern Jersey', 'Southern Jersey'),
                ('Idaho', 'Idaho'),
                ('LA Metro', 'LA Metro'),
                ('West Washington', 'West Washington'),
                ('Orange County', 'Orange County'),
                ('Oregon / SW Washington', 'Oregon / SW Washington'),
                ('Mississippi', 'Mississippi'),
                ('South Texas', 'South Texas'),
                ('San Antonio', 'San Antonio'),
                ('Milwaukee', 'Milwaukee'),
                ('Cincinnati', 'Cincinnati'),
                ('North Wisconsin', 'North Wisconsin'),
                ('Rochester', 'Rochester'),
                ('Houston', 'Houston'),
                ('Norfolk', 'Norfolk'),
                ('Miami / West Palm', 'Miami / West Palm'),
                ('Las Vegas', 'Las Vegas'),
                ('Cleveland', 'Cleveland'),
                ('East Michigan', 'East Michigan'),
                ('Chicago', 'Chicago'),
                ('SF Bay', 'SF Bay'),
                ('GA/SC Coast', 'GA/SC Coast'),
                ('Delaware', 'Delaware'),
                ('Phoenix', 'Phoenix'),
                ('West Iowa / Nebraska', 'West Iowa / Nebraska'),
                ('Pittsburgh', 'Pittsburgh'),
                ('Austin', 'Austin'),
                ('Tampa', 'Tampa'),
                ('Louisiana', 'Louisiana'),
                ('Gulf Coast', 'Gulf Coast'),
                ('Long Island', 'Long Island'),
                ('Charlotte', 'Charlotte'),
                ('Toledo', 'Toledo'),
                ('Minnesota', 'Minnesota'),
                ('Columbus', 'Columbus'),
                ('Philadelphia Metro', 'Philadelphia Metro'),
                ('Colorado', 'Colorado'),
                ('Oklahoma', 'Oklahoma'),
                ('Upper Central Valley', 'Upper Central Valley'),
                ('Ft. Wayne / South Bend', 'Ft. Wayne / South Bend'),
                ('Boston', 'Boston'),
                ('Raleigh / Durham', 'Raleigh / Durham'),
                ('Winston / Salem', 'Winston / Salem'),
                ('Arkansas', 'Arkansas'),
                ('San Diego', 'San Diego'),
                ('Myrtle Beach', 'Myrtle Beach'),
                ('Upstate NY East', 'Upstate NY East'),
                ('Central Illinois', 'Central Illinois'),
                ('Northern Jersey', 'Northern Jersey'),
                ('Central Pennsylvania', 'Central Pennsylvania'),
                ('The Panhandle', 'The Panhandle'),
                ('Providence', 'Providence'),
                ('Upstate NY Central', 'Upstate NY Central'),
                ('West Michigan', 'West Michigan'),
                ('Utah', 'Utah'),
                ('Tucson / Yuma', 'Tucson / Yuma'),
                ('New York City', 'New York City'),
                ('VT / NH / ME', 'VT / NH / ME'),
                ('Hawaii', 'Hawaii'),
                ('Northern Connecticut', 'Northern Connecticut'),
                ('Richmond', 'Richmond'),
                ('Western Pennsylvania', 'Western Pennsylvania'),
                ('Southern Virginia', 'Southern Virginia'),
                ('Memphis', 'Memphis'),
                ('Baltimore', 'Baltimore'),
                ('Southern Connecticut', 'Southern Connecticut'),
                ('Indianapolis', 'Indianapolis'),
                ('New Orleans', 'New Orleans'),
                ('Buffalo', 'Buffalo'),
                ('South West Florida', 'South West Florida'),
                ('North LA', 'North LA'),
                ('South Bay', 'South Bay'),
                ('West Virginia', 'West Virginia'),
        )

        Market = models.CharField(max_length=255, choices=market,blank=True)


        eNB = models.CharField(max_length=255, default='',blank=True)
        CSMS = models.CharField(max_length=255, default='', blank=True)
        OSS = models.CharField(max_length=255, default='',blank=True)
        RSD_Air_Boss = models.CharField(max_length=255, default='',blank=True)
        FE_Name = models.CharField(max_length=255, default='',blank=True)
        Onshore_Eng_Name = models.CharField(max_length=255, default='', blank=True)
        Pre_E_Tilt_Values = models.CharField(max_length=255, default='', blank=True)
        Post_E_Tilt_Values = models.CharField(max_length=255, default='', blank=True)
        Pre_Max_User_Count = models.CharField(max_length=255, default='', blank=True)
        Post_Max_User_Count = models.CharField(max_length=255, default='', blank=True)

        Revisit_Required_CHOICES4 = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )
        Revisit_Required = models.CharField(max_length=255, choices=Revisit_Required_CHOICES4, blank=True)

        Is_Pre_Integration_site_CHOICES4 = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )
        Is_Pre_Integration_site = models.CharField(max_length=255, choices=Is_Pre_Integration_site_CHOICES4, blank=True)

        Mode_of_Communication_CHOICES6 = (
                ('Bridge-1', 'Bridge-1'),
                ('Bridge-2', 'Bridge-2'),
                ('Bridge-3', 'Bridge-3'),
                ('Bridge-4', 'Bridge-4'),
                ('Bridge-5', 'Bridge-5'),
                ('Bridge-6', 'Bridge-6'),
                ('Bridge-7', 'Bridge-7'),
                ('Bridge-8', 'Bridge-8'),
                ('Bridge-9', 'Bridge-9'),
                ('Bridge-10', 'Bridge-10'),
                ('Bridge-11', 'Bridge-11'),
                ('Bridge-12', 'Bridge-12'),
                ('Bridge-13', 'Bridge-13'),
                ('Bridge-14', 'Bridge-14'),
                ('Bridge-15', 'Bridge-15'),
                ('E-Mail', 'E-Mail'),
        )

        Bridge_No = models.CharField(max_length=255, choices=Mode_of_Communication_CHOICES6,blank=True)


        Activity_status3 = (
                ('Cabinet Swap', 'Cabinet Swap'),
                ('Change In SAMB', 'Change In SAMB'),
                ('Health Check', 'Health Check'),
                ('LAM Testing', 'LAM Testing'),
                ('LATP/FATP Testing', 'LATP/FATP Testing'),
                ('Mini M Decom Macro', 'Mini M Decom Macro'),
                ('New Integration', 'New Interation'),
                ('Relo Site', 'Relo Site'),
                ('Technology ADD', 'Technology ADD'),
                ('Troubleshooting', 'Troubleshooting'),

        )

        Site_Activity_Type = models.CharField(max_length=255, choices=Activity_status3, blank=True)

        Activity_status_CHOICES3 = (
                ('Open', 'Open'),
                ('Close', 'Close'),
                ('Handover', 'Handover'),
        )

        Activity_status = models.CharField(max_length=255, choices=Activity_status_CHOICES3,blank=True)

        Site_Status_pre_Activity_CHOICES4 = (
                ('Lock', 'Lock'),
                ('Unlock', 'Unlock'),
                ('NA', 'N/A'),
        )

        Site_Status_pre_Activity = models.CharField(max_length=255, choices=Site_Status_pre_Activity_CHOICES4,blank=True)

        Site_Status_post_Activity_CHOICES4 = (
                ('Lock', 'Lock'),
                ('Unlock', 'Unlock'),
                ('NA', 'N/A'),
        )

        Site_Status_post_Activity = models.CharField(max_length=255, choices=Site_Status_post_Activity_CHOICES4, blank=True)

        Pre_Reserve_CHOICES4 = (
                ('Reserved', 'Reserved'),
                ('CP-INH', 'CP-INH'),
                ('Not Reserved', 'Not Reserved'),
                ('Grow', 'Grow'),
                ('Equipped', 'Equipped'),

        )

        Pre_Reserve = models.CharField(max_length=255, choices=Pre_Reserve_CHOICES4,blank=True)

        Post_Reserve_CHOICES4 = (
                ('Reserved', 'Reserved'),
                ('CP-INH', 'CP-INH'),
                ('Not Reserved', 'Not Reserved'),
                ('Grow', 'Grow'),
                ('Equiped', 'Equiped'),
        )

        Post_Reserve = models.CharField(max_length=255, choices=Post_Reserve_CHOICES4, blank=True)

        OAR_Date = models.DateField(null=True,blank=True)
        OAC_Date = models.DateField(null=True,blank=True)
        Final_Comments = models.TextField( default='',blank=True)

        created_date = models.DateTimeField(default=timezone.now)
        Date = models.DateField(null=True, blank=True)
        # date format %Y-%m-%d

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.cascade


class AluRsaTracker(models.Model):
        admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')
        cascade = models.CharField(max_length=255, default='')
        Assignee = models.ForeignKey(AluProfile, on_delete=models.CASCADE, related_name='alursaprofile')
        board = models.ForeignKey(ALUCounts, related_name='alursacounts', on_delete=models.CASCADE, null=True)

        Technology_CHOICES1 = (
                ('800 CDMA', '800 CDMA'),
                ('1900 CDMA', '1900 CDMA'),
                ('800 FDD', '800 FDD'),
                ('1900 FDD', '1900 FDD'),
                ('2.5 TDD', '2.5 TDD'),
                ('700 FDD', '700 FDD'),
                ('1900 FDD;800 FDD', '1900 FDD;800 FDD'),
                ('1900 CDMA;800 CDMA', '1900 CDMA;800 CDMA'),
        )

        Technology = models.CharField(max_length=255, choices=Technology_CHOICES1)

        Source_CHOICES1 = (
                ('Normal RSA', 'Normal RSA'),
                ('MIMO RSA', 'MIMO RSA'),
                ('Brenda OAC', 'Brenda OAC'),
                ('Brenda ATP', 'Brenda ATP'),
                ('Brenda RSA Only', 'Brenda RSA Only'),
                ('RSA Only', 'RSA Only'),
                ('Manual LATP', 'Manual LATP'),
                ('Spectrum clear', 'Spectrum Clear'),
                ('Mail RSA', 'Mail RSA'),
        )

        Source = models.CharField(max_length=255, choices=Source_CHOICES1)

        Site_Type_CHOICES1 = (
                ('Monopole', 'Monopole'),
                ('Roof Top', 'Roof Top'),
                ('Substantial Services', 'Substantial Services'),
                ('Macro', 'Macro'),
                ('Swap – NV to NV', 'Swap – NV to NV'),
                ('Swap – Legacy to NV', 'Swap – Legacy to NV'),
        )

        Site_Type = models.CharField(max_length=255, choices=Site_Type_CHOICES1)

        Type_OEM8 = (
                ('Airscale', 'Airscale'),
                ('ALU', 'ALU'),
                ('NSN', 'NSN'),
        )

        OEM = models.CharField(max_length=255, choices=Type_OEM8, blank=True)


        market = (
                ('Kansas', 'Kansas'),
                ('Alaska', 'Alaska'),
                ('PR / VI', 'PR / VI'),
                ('DFW', 'DFW'),
                ('East Texas', 'East Texas'),
                ('Inland Northwest', 'Inland Northwest'),
                ('Albuquerque', 'Albuquerque'),
                ('Jacksonville', 'Jacksonville'),
                ('Nashville', 'Nashville'),
                ('West Texas', 'West Texas'),
                ('Washington DC', 'Washington DC'),
                ('East Iowa', 'East Iowa'),
                ('MT / WY', 'MT / WY'),
                ('South Carolina', 'South Carolina'),
                ('Riverside / San Bernardino', 'Riverside / San Bernardino'),
                ('East Kentucky', 'East Kentucky'),
                ('Alabama', 'Alabama'),
                ('West Kentucky', 'West Kentucky'),
                ('Dakotas', 'Dakotas'),
                ('Orlando', 'Orlando'),
                ('Central Iowa', 'Central Iowa'),
                ('Georgia', 'Georgia'),
                ('Missouri', 'Missouri'),
                ('Lower Central Valley', 'Lower Central Valley'),
                ('Atlanta / Athens', 'Atlanta / Athens'),
                ('Southern Jersey', 'Southern Jersey'),
                ('Idaho', 'Idaho'),
                ('LA Metro', 'LA Metro'),
                ('West Washington', 'West Washington'),
                ('Orange County', 'Orange County'),
                ('Oregon / SW Washington', 'Oregon / SW Washington'),
                ('Mississippi', 'Mississippi'),
                ('South Texas', 'South Texas'),
                ('San Antonio', 'San Antonio'),
                ('Milwaukee', 'Milwaukee'),
                ('Cincinnati', 'Cincinnati'),
                ('North Wisconsin', 'North Wisconsin'),
                ('Rochester', 'Rochester'),
                ('Houston', 'Houston'),
                ('Norfolk', 'Norfolk'),
                ('Miami / West Palm', 'Miami / West Palm'),
                ('Las Vegas', 'Las Vegas'),
                ('Cleveland', 'Cleveland'),
                ('East Michigan', 'East Michigan'),
                ('Chicago', 'Chicago'),
                ('SF Bay', 'SF Bay'),
                ('GA/SC Coast', 'GA/SC Coast'),
                ('Delaware', 'Delaware'),
                ('Phoenix', 'Phoenix'),
                ('West Iowa / Nebraska', 'West Iowa / Nebraska'),
                ('Pittsburgh', 'Pittsburgh'),
                ('Austin', 'Austin'),
                ('Tampa', 'Tampa'),
                ('Louisiana', 'Louisiana'),
                ('Gulf Coast', 'Gulf Coast'),
                ('Long Island', 'Long Island'),
                ('Charlotte', 'Charlotte'),
                ('Toledo', 'Toledo'),
                ('Minnesota', 'Minnesota'),
                ('Columbus', 'Columbus'),
                ('Philadelphia Metro', 'Philadelphia Metro'),
                ('Colorado', 'Colorado'),
                ('Oklahoma', 'Oklahoma'),
                ('Upper Central Valley', 'Upper Central Valley'),
                ('Ft. Wayne / South Bend', 'Ft. Wayne / South Bend'),
                ('Boston', 'Boston'),
                ('Raleigh / Durham', 'Raleigh / Durham'),
                ('Winston / Salem', 'Winston / Salem'),
                ('Arkansas', 'Arkansas'),
                ('San Diego', 'San Diego'),
                ('Myrtle Beach', 'Myrtle Beach'),
                ('Upstate NY East', 'Upstate NY East'),
                ('Central Illinois', 'Central Illinois'),
                ('Northern Jersey', 'Northern Jersey'),
                ('Central Pennsylvania', 'Central Pennsylvania'),
                ('The Panhandle', 'The Panhandle'),
                ('Providence', 'Providence'),
                ('Upstate NY Central', 'Upstate NY Central'),
                ('West Michigan', 'West Michigan'),
                ('Utah', 'Utah'),
                ('Tucson / Yuma', 'Tucson / Yuma'),
                ('New York City', 'New York City'),
                ('VT / NH / ME', 'VT / NH / ME'),
                ('Hawaii', 'Hawaii'),
                ('Northern Connecticut', 'Northern Connecticut'),
                ('Richmond', 'Richmond'),
                ('Western Pennsylvania', 'Western Pennsylvania'),
                ('Southern Virginia', 'Southern Virginia'),
                ('Memphis', 'Memphis'),
                ('Baltimore', 'Baltimore'),
                ('Southern Connecticut', 'Southern Connecticut'),
                ('Indianapolis', 'Indianapolis'),
                ('New Orleans', 'New Orleans'),
                ('Buffalo', 'Buffalo'),
                ('South West Florida', 'South West Florida'),
                ('North LA', 'North LA'),
                ('South Bay', 'South Bay'),
                ('West Virginia', 'West Virginia'),
        )

        Market = models.CharField(max_length=255, choices=market,blank=True)


        eNB = models.CharField(max_length=255, default='',blank=True)
        CSMS = models.CharField(max_length=255, default='', blank=True)
        OSS = models.CharField(max_length=255, default='',blank=True)


        Ageing = models.IntegerField(default=0,blank=True)
        Alarm_Status = models.CharField(max_length=255, default='',blank=True)
        Nims = models.CharField(max_length=255, default='', blank=True)
        ACD = models.CharField(max_length=255, default='', blank=True)
        TVW = models.CharField(max_length=255, default='', blank=True)
        PRTS = models.CharField(max_length=255, default='', blank=True)
        Patrol = models.CharField(max_length=255, default='', blank=True)
        Trams = models.CharField(max_length=255, default='', blank=True)
        NEO = models.CharField(max_length=255, default='', blank=True)
        Category = models.CharField(max_length=255, default='', blank=True)
        Owner = models.CharField(max_length=255, default='', blank=True)

        Revisit_Required_CHOICES4 = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )
        Volte_Soft_Launch_Status = models.CharField(max_length=255, choices=Revisit_Required_CHOICES4, blank=True)

#        OAR_Date = models.DateField(null=True,blank=True)
#        OAC_Date = models.DateField(null=True,blank=True)
        OAR_CHOICES4 = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )
        OAR_Date = models.CharField(max_length=255, choices=OAR_CHOICES4, blank=True)

        OAC_CHOICES4 = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )
        OAC_Date = models.CharField(max_length=255, choices=OAC_CHOICES4, blank=True)

        Initial_Status = models.CharField(max_length=255, default='',blank=True)
        Final_Status = models.CharField(max_length=255, default='', blank=True)
        CICO_CHOICES4 = (
                ('Fail', 'Fail'),
                ('Pass', 'Pass'),

        )

        CICO = models.CharField(max_length=255, choices=CICO_CHOICES4, blank=True)
        SV_3115 = models.CharField(max_length=255, default='', blank=True)
        Remark = models.CharField(max_length=255, default='', blank=True)

        created_date = models.DateTimeField(default=timezone.now)
        Date = models.DateField(null=True, blank=True)
        # date format %Y-%m-%d

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.cascade