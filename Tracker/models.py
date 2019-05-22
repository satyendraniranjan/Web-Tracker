from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()





class Samsung(models.Model):
        name = models.CharField(max_length=30, unique=True)
        description = models.CharField(max_length=100)

        def __str__(self):
                return self.name

        def get_tracker_count(self):
                date_from = datetime.datetime.now() - datetime.timedelta(days=1)
                return Tracker.objects.filter(board=self, Date__gte=date_from).count()
#                return Tracker.objects.filter(board=self).extra({'date_created' : "date(Date)"}).values('date_created').annotate(created_count=Count('id'))

        def get_rsatracker_count(self):
                return RSATracker.objects.filter(rsa=self).count()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
            return self.user.username

    def get_tracker_count(self):
            return Tracker.objects.filter( Q(Assignee=self)).count()

    def get_activity_count1(self):
            return Tracker.objects.filter( Q(Assignee=self) & Q(Activity='C&I')).count()

    def get_activity_count2(self):
            return Tracker.objects.filter( Q(Assignee=self) & Q(Activity='Troubleshoot')).count()
    def get_activity_count3(self):
            return Tracker.objects.filter( Q(Assignee=self) & Q(Activity='LATP Testing')).count()

    def get_activity_count4(self):
            return Tracker.objects.filter( Q(Assignee=self) & Q(Activity='FATP Testing')).count()

    def get_activity_count5(self):
            return Tracker.objects.filter( Q(Assignee=self) & Q(Activity='Pre-Integration')).count()

    def get_activity_count6(self):
            return Tracker.objects.filter( Q(Assignee=self) & Q(Activity='Update to FE')).count()




"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

"""




class Tracker(models.Model):
        admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')
        Assignee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='assignee')
        cascade = models.CharField(max_length=255, default='')
        board = models.ForeignKey(Samsung, related_name='topics', on_delete=models.CASCADE, null=True)
        Technology_CHOICES1 = (
                ('800 CDMA', '800 CDMA'),
                ('1900 CDMA', '1900 CDMA'),
                ('800 FDD', '800 FDD'),
                ('1900 FDD', '1900 FDD'),
                ('2.5 TDD', '2.5 TDD'),
                ('1900 800 CDMA', '1900/800 CDMA'),
                ('1900 800 FDD', '1900/800 FDD'),
                ('1900 700 CDMA', '1900/700 CDMA'),
                ('700 FDD', '700 FDD'),
                ('800 FDD CDMA', '800 FDD/CDMA'),
        )

        Technology = models.CharField(max_length=255, choices=Technology_CHOICES1)

        Type_CHOICES8 = (
                ('CDU10', 'CDU10'),
                ('CDU20', 'CDU20'),
                ('CDU30', 'CDU30'),
                ('NA', 'NA'),
        )

        Type = models.CharField(max_length=255, choices=Type_CHOICES8,blank=True)

        Bandwidth_Checked_From_LSM_CHOICES10 = (
                ('3Mhz', '3Mhz'),
                ('5Mhz', '5Mhz'),
                ('10Mhz', '10Mhz'),
                ('15Mhz', '15Mhz'),
                ('20Mhz', '20Mhz'),
                ('5+10Mhz 5Mhz', '5+10Mhz/5Mhz'),
                ('5+10Mhz 3Mhz', '5+10Mhz/3Mhz'),
                ('10+5Mhz 5Mhz', '10+5Mhz/5Mhz'),
                ('10+5Mhz 3Mhz', '10+5Mhz/3Mhz'),
                ('5+5 Mhz/5 Mhz', '5+5 Mhz/5 Mhz'),
                ('5 Mhz/3 Mhz', '5 Mhz/3 Mhz'),
                ('5 Mhz/5 Mhz', '5 Mhz/5 Mhz'),
                ('10 Mhz/3 Mhz', '10 Mhz/3 Mhz'),
                ('10 Mhz/5 Mhz', '10 Mhz/5 Mhz'),
                ('15 Mhz/3 Mhz', '15 Mhz/3 Mhz'),
                ('15 Mhz/5 Mhz', '15 Mhz/5 Mhz'),
                ('5+5 Mhz/3 Mhz', '5+5 Mhz/3 Mhz'),
                ('NA', 'NA'),
        )

        Bandwidth_Checked_From_LSM = models.CharField(max_length=255, choices=Bandwidth_Checked_From_LSM_CHOICES10,blank=True)

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
        LSM = models.CharField(max_length=255, default='',blank=True)
        CSMS = models.CharField(max_length=255, default='',blank=True)
        FE_Name = models.CharField(max_length=255, default='',blank=True)


        Mode_of_Communication_CHOICES6 = (
                ('Whatsapp', 'Whatsapp'),
                ('Primary Bridge', 'Primary Bridge'),
                ('Secondary Bridge', 'Secondary Bridge'),
                ('IM', 'IM'),
                ('E-Mail', 'E-Mail'),
        )

        Mode_of_Communication = models.CharField(max_length=255, choices=Mode_of_Communication_CHOICES6,blank=True)

        Activity_CHOICES2 = (
                ('C&I', 'C&I'),
                ('Troubleshoot', 'Troubleshoot'),
                ('LATP Testing', 'LATP Testing'),
                ('FATP Testing', 'FATP Testing'),
                ('Pre-Integration', 'Pre-Integration'),
                ('Update to FE', 'Update to FE'),
                ('E911 Testing', 'E911 Testing'),
                ('LAM Testing', 'LAM Testing'),
                ('Grow with No Connectivity', 'Grow with No Connectivity'),
                ('Grow with Connectivity only', 'Grow with Connectivity only'),
        )

        Activity = models.CharField(max_length=255, choices=Activity_CHOICES2, blank=True)

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

        E_Link_Status_of_BH0_for_CDU30_CHOICES12 = (
                ('On', 'On'),
                ('OFF', 'OFF'),
                ('NA', 'NA'),

        )

        E_Link_Status_of_BH0_for_CDU30 = models.CharField(max_length=255, choices=E_Link_Status_of_BH0_for_CDU30_CHOICES12, blank=True)


        MJ_Object_Marked_CHOICES11 = (
                ('Marked', 'Marked'),
                ('Not Marked', 'Not Marked'),
                ('NA', 'NA'),

        )

        MJ_Object_Marked = models.CharField(max_length=255, choices=MJ_Object_Marked_CHOICES11,blank=True)

        RET_CHOICES9 = (
                ('Defined Matched', 'Defined/Matched'),
                ('Defined NotMatched', 'Defined/NotMatched'),
                ('Not Define', 'Not Define'),
                ('NA', 'NA'),
        )

        RET = models.CharField(max_length=255, choices=RET_CHOICES9, blank=True)

        Alarms_Preventing_RET_Config = models.CharField(max_length=255, default='', blank=True)

        Frequency_Earfcn_Checked_from_LSM_BSM_CHOICES7 = (
                ('Yes', 'Yes'),
                ('No', 'No'),
                ('Not Required', 'Not Required'),
        )

        Frequency_Earfcn_Checked_from_LSM_BSM = models.CharField(max_length=255, choices=Frequency_Earfcn_Checked_from_LSM_BSM_CHOICES7, blank=True)

        IP_Route_or_IP_Address = models.CharField(max_length=255, default='',blank=True)
        Volte_MME_IP_Config = models.CharField(max_length=255, default='',blank=True)
        Review_LATP_Complete = models.CharField(max_length=255, default='',blank=True)
        Remarks = models.CharField(max_length=255, default='',blank=True)
        OAR_Date = models.DateField(null=True,blank=True)
        OAC_Date = models.DateField(null=True,blank=True)
        Lock_Unlock_Verified_By = models.CharField(max_length=255, default='',blank=True)
        Verify_Status = models.CharField(max_length=255, default='',blank=True)
        Final_Comments = models.CharField(max_length=255, default='',blank=True)







        created_date = models.DateTimeField(default=timezone.now)
        Date = models.DateField(null=True, blank=True)
        # date format %Y-%m-%d

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.cascade


from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class RSATracker(models.Model):
        User_Name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')

        cascade = models.CharField(max_length=255, default='')
        Technology_CHOICES1 = (
                ('800 CDMA', '800 CDMA'),
                ('1900 CDMA', '1900 CDMA'),
                ('800 FDD', '800 FDD'),
                ('1900 FDD', '1900 FDD'),
                ('2.5 TDD', '2.5 TDD'),
                ('1900 800 CDMA', '1900/800 CDMA'),
                ('1900 800 FDD', '1900/800 FDD'),
                ('1900 700 CDMA', '1900/700 CDMA'),
                ('700 FDD', '700 FDD'),
                ('800 FDD CDMA', '800 FDD/CDMA'),
        )

        Technology = models.CharField(max_length=255, choices=Technology_CHOICES1)

        Type_CHOICES8 = (
                ('CDU10', 'CDU10'),
                ('CDU20', 'CDU20'),
                ('CDU30', 'CDU30'),
                ('NA', 'NA'),
        )

        Type = models.CharField(max_length=255, choices=Type_CHOICES8,blank=True)



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
        Assignee = models.ForeignKey(User, default='', on_delete=models.CASCADE, related_name='assignee1')
        eNB = models.CharField(max_length=255, default='',blank=True)
        LSM = models.CharField(max_length=255, default='',blank=True)
        SiteType = models.CharField(max_length=255, default='',blank=True)
        Schedule_Name = models.CharField(max_length=255, default='',blank=True)
        Fail = models.CharField(max_length=255, default='',blank=True)
        Fail_Reason = models.CharField(max_length=255, default='',blank=True)

        Activity_CHOICESPTRV = (
                (' 121000;121000;66000;66000', ' 121000;121000;66000;66000'),
                ('121000;121000', '121000;121000'),
                ('66000;66000', '66000;66000'),
                ('NA', 'NA'),
        )
        RTRV_SON_SO_status = models.CharField(max_length=255, default='',choices=Activity_CHOICESPTRV,blank=True)

        Activity_CHOICESTi = (
                ('PRTS', 'PRTS'),
                ('TRAMS', 'TRAMS'),
                ('NIMS', 'NIMS'),
                ('NEO', 'NEO'),
                ('PATROL', 'PATROL'),
        )
        Ticket_Raised_For_Issue = models.CharField(max_length=255, default='',choices=Activity_CHOICESTi,blank=True)
        Ticket_no = models.CharField(max_length=255, default='',blank=True)

        Activity_CHOICESSV = (
                ('Yes', 'Yes'),
                ('No', 'No'),
                ('Yes but incomplete data', 'Yes but incomplete data'),
        )

        TVW_Available = models.CharField(max_length=255, default='',choices=Activity_CHOICESSV,blank=True)

        Activity_CHOICESF = (
                ('TVW Available in West Extract Database', 'TVW Available in West Extract Database'),
                ('Yes', 'Yes'),
                ('No', 'No'),
                ('Rural Roaming Site. TVW not required.', 'Rural Roaming Site. TVW not required.'),
                ('NA', 'NA'),
        )
        TVW_Available_FMCC_Database = models.CharField(max_length=255, default='',choices=Activity_CHOICESF,blank=True)

        Activity_CHOICESA = (
                ('Task 3105 is Actualized', 'Task 3105 is Actualized'),
                ('ACD Accepted', 'ACD Accepted'),
                ('TVW Received from WEST', 'TVW Received from WEST'),
                ('Ready for drive test', 'Ready for drive test'),
                ('ACD Error', 'ACD Error'),
                ('ACD Rejected', 'ACD Rejected'),
                ('ACD Created', 'ACD Created'),
                ('ACD Sent', 'ACD Sent'),
                ('Blank', 'Blank'),
                ('Rural Roaming Site. ACD not required.', 'Rural Roaming Site. ACD not required.'),)

        Acd_Status = models.CharField(max_length=255, default='',choices=Activity_CHOICESA,blank=True)

        Activity_CHOICEST = (
                ('TVW Related Remarks', 'TVW Related Remarks'),
                ('informational only, no action required', 'informational only, no action required'),
                ('send completed ACD/TVW to West', 'send completed ACD/TVW to West'),
                ('Upload Complete TVW file to SV', 'Upload Complete TVW file to SV'),
        )

        TVW_Related_Remarks = models.CharField(max_length=255, default='',choices=Activity_CHOICEST,blank=True)


        Other_Remarks = models.CharField(max_length=255, default='',blank=True)

        SV_Actualization = models.CharField(max_length=255, default='',blank=True)

        CSMS = models.CharField(max_length=255, default='',blank=True)
        FE_Name = models.CharField(max_length=255, default='',blank=True)


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


        RET_CHOICES9 = (
                ('Defined in LSM', 'Defined in LSM'),
                ('Defined in BSM', 'Defined in BSM'),
                ('NA', 'NA'),
        )

        RET = models.CharField(max_length=255, choices=RET_CHOICES9, blank=True)

        OAR_Date = models.DateField(null=True,blank=True)
        OAC_Date = models.DateField(null=True,blank=True)
        Lock_Unlock_Verified_By = models.CharField(max_length=255, default='',blank=True)
        created_date = models.DateTimeField(default=timezone.now)
        Date = models.DateField(null=True,blank=True)
        # date format %Y-%m-%d

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.cascade

        def save(self, *args, **kwargs):
                self.full_clean()  # performs regular validation then clean()
                super(RSATracker, self).save(*args, **kwargs)

        def clean(self):
                """
                Custom validation (read docs)
                PS: why do you have null=True on charfield?
                we could avoid the check for name
                """

                if self.cascade:
                        self.cascade = self.cascade.strip()
                if self.eNB:
                        self.eNB = self.eNB.strip()
                if self.Technology:
                        self.Technology = self.Technology.strip()
                if self.Type:
                        self.Type = self.Type.strip()
                if self.Market:
                        self.Market = self.Market.strip()


def validate_artist_name_choice(sender, instance, **kwargs):
        valid_types = [t[0] for t in sender.Technology_CHOICES1]
        if instance.Technology not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER Technology "{}" is not one of the permitted values: {}'.format(
                                instance.Technology,
                                ', '.join(valid_types)))

        valid_types = [t[0] for t in sender.Type_CHOICES8]
        if instance.Type not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER Type "{}" is not one of the permitted values: {}'.format(
                                instance.Type,
                                ', '.join(valid_types)))

        valid_types = [t[0] for t in sender.market]
        if instance.Market not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER Market "{}" is not one of the permitted values: {}'.format(
                                instance.Market,
                                ', '.join(valid_types)))

        """"
    
        valid_types = [t[0] for t in sender.sitetype_CHOICESPTRV]
        if instance.SiteType not in valid_types:
            from django.core.exceptions import ValidationError
            raise ValidationError(
                'RSA TRACKER SiteType "{}" is not one of the permitted values: {}'.format(
                    instance.SiteType,
                   ', '.join(valid_types)))
    
        valid_types = [t[0] for t in sender.Activity_CHOICESPTRV]
        if instance.RTRV_SON_SO_status not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER SiteType "{}" is not one of the permitted values: {}'.format(
                                instance.type,
                                ', '.join(valid_types)))
    
        valid_types = [t[0] for t in sender.Activity_CHOICESTi]
        if instance.Ticket_Raised_For_Issue not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER SiteType "{}" is not one of the permitted values: {}'.format(
                                instance.type,
                                ', '.join(valid_types)))
    
        valid_types = [t[0] for t in sender.Activity_CHOICESSV]
        if instance.TVW_Available not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER SiteType "{}" is not one of the permitted values: {}'.format(
                                instance.type,
                                ', '.join(valid_types)))
    
        valid_types = [t[0] for t in sender.Activity_CHOICESF]
        if instance.TVW_Available_FMCC_Database not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER SiteType "{}" is not one of the permitted values: {}'.format(
                                instance.type,
                                ', '.join(valid_types)))
    
        valid_types = [t[0] for t in sender.Activity_CHOICESA]
        if instance.Acd_Status not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER SiteType "{}" is not one of the permitted values: {}'.format(
                                instance.type,
                                ', '.join(valid_types)))
    
        valid_types = [t[0] for t in sender.Activity_CHOICEST]
        if instance.TVW_Related_Remarks not in valid_types:
                from django.core.exceptions import ValidationError
                raise ValidationError(
                        'RSA TRACKER SiteType "{}" is not one of the permitted values: {}'.format(
                                instance.type,
                                ', '.join(valid_types)))"""


models.signals.pre_save.connect(validate_artist_name_choice, sender=RSATracker)

