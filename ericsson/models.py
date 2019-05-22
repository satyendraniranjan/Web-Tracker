from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q



class Ericsson_Count(models.Model):
        name = models.CharField(max_length=30, unique=True)
        description = models.CharField(max_length=100)

        def __str__(self):
                return self.name

        def get_tracker_count(self):
                date_from = datetime.datetime.now() - datetime.timedelta(days=1)
                return EricssonPostComTracker.objects.filter(board=self, Date__gte=date_from).count()
#                return Tracker.objects.filter(board=self).extra({'date_created' : "date(Date)"}).values('date_created').annotate(created_count=Count('id'))




class EricssonProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
            return self.user.username

    def get_tracker_count(self):
            return EricssonPostComTracker.objects.filter( Q(Assignee=self)).count()




class EricssonPostComTracker(models.Model):
        admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='')
        cascade = models.CharField(max_length=255, default='')
        Assignee = models.ForeignKey(EricssonProfile, on_delete=models.CASCADE, related_name='ericssonprofile')
        board = models.ForeignKey(Ericsson_Count, related_name='ericssoncounts', on_delete=models.CASCADE, null=True)

        Technology_CHOICES1 = (

                ('800 FDD', '800 FDD'),
                ('1900 FDD', '1900 FDD'),
                ('2.5 TDD', '2.5 TDD'),
                ('1900 800 FDD', '1900/800 FDD'),
                ('1900 CDMA', '1900 CDMA'),
                ('800 CDMA', '800 CDMA'),
                ('800/1900 CDMA', '800/1900 CDMA'),
        )

        Technology = models.CharField(max_length=255, choices=Technology_CHOICES1)


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
        ENM = models.CharField(max_length=255, default='',blank=True)
        CSMS = models.CharField(max_length=255, default='',blank=True)
        IP_OAM = models.CharField(max_length=255, default='', blank=True)
        FE_Name = models.CharField(max_length=255, default='',blank=True)
        Tech_Email = models.CharField(max_length=255, default='', blank=True)
        Tech_Contact = models.CharField(max_length=255, default='', blank=True)
        CIC_Airboss_Mail = models.CharField(max_length=255, default='', blank=True)
        RSD_Airboss_Mail = models.CharField(max_length=255, default='', blank=True)
        RSD_Manager_Mail= models.CharField(max_length=255, default='', blank=True)
        Construction_Manager_Mail = models.CharField(max_length=255, default='', blank=True)




        Activity_CHOICES2 = (
                ('Alarm Report', 'Alarm Report'),
                ('OSF Recreated', 'OSF Recreated'),
                ('Troubleshooting', 'Troubleshooting'),
                ('LATP Testing', 'LATP Testing'),
                ('FATP Testing', 'FATP Testing'),
                ('Integration & Testing', 'Integration & Testing'),
                ('Integration Only', 'Integration Only'),
                ('Pre - Integration', 'Pre - Integration'),
                ('LAM', 'LAM'),
        )

        Activity = models.CharField(max_length=255, choices=Activity_CHOICES2,blank=True)

        Activity_status_CHOICES3 = (
                ('Completed', 'Completed'),
                ('In Progress', 'In Progress'),
                ('Pending', 'Pending'),

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

        )

        Site_Status_post_Activity = models.CharField(max_length=255, choices=Site_Status_post_Activity_CHOICES4, blank=True)


        Secondary_Fibre_check_CHOICES12 = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )

        Secondary_Fibre_check = models.CharField(max_length=255,choices=Secondary_Fibre_check_CHOICES12, blank=True)

        Site_Pre_Status_CHOICES12 = (
                ('Integrated', 'Integrated'),
                ('Ready to integrate', 'Ready to integrate'),


        )

        Site_Pre_Status = models.CharField(max_length=255, choices=Site_Pre_Status_CHOICES12, blank=True)

        Site_Post_Status_CHOICES12 = (
                ('Integrated', 'Integrated'),
                ('Tested', 'Tested'),

        )


        Site_Post_Status = models.CharField(max_length=255, choices=Site_Post_Status_CHOICES12, blank=True)

        Kpi_CHOICES12 = (
                ('Complete', 'Complete'),
                ('Pending', 'Pending'),

        )


        Kpi_Profile = models.CharField(max_length=255,choices=Kpi_CHOICES12, blank=True)



        Volte_Soft_CHOICES7 = (
                ('Yes', 'Yes'),
                ('No', 'No'),
                ('NA', 'NA'),
        )

        Volte_Soft = models.CharField(max_length=255, choices=Volte_Soft_CHOICES7, blank=True)

        Revisit_Required_CHOICES7 = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )

        Revisit_Required = models.CharField(max_length=255, choices=Revisit_Required_CHOICES7, blank=True)

        Revisit_CHOICES7 = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )

        Revisit = models.CharField(max_length=255, choices=Revisit_CHOICES7, blank=True)


        Remarks = models.CharField(max_length=255, default='',blank=True)
        OAR_Date = models.DateField(null=True,blank=True)
        OAC_Date = models.DateField(null=True,blank=True)








        created_date = models.DateTimeField(default=timezone.now)
        Date = models.DateField(null=True, blank=True)
        # date format %Y-%m-%d

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.cascade



class RSATracker(models.Model):
        admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='',null=True,related_name='ericssonrsaadmin')
        ericrsa = models.ForeignKey(Ericsson_Count, related_name='ericssonrsa', on_delete=models.CASCADE)
        cascade = models.CharField(max_length=255, default='',blank=True)
        Assignee = models.ForeignKey(EricssonProfile, on_delete=models.CASCADE, related_name='ericssonrsaprofile')
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

        Technology = models.CharField(max_length=255, choices=Technology_CHOICES1,blank=True)

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
                ('20Mhz', '20Mhz'),
                ('5+10Mhz 5Mhz', '5+10Mhz/5Mhz'),
                ('5+10Mhz 3Mhz', '5+10Mhz/3Mhz'),
                ('10+5Mhz 5Mhz', '10+5Mhz/5Mhz'),
                ('10+5Mhz 3Mhz', '10+5Mhz/3Mhz'),
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

        Assignee = models.CharField(max_length=255, default='',blank=True)
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
        Date = models.DateTimeField(null=True,blank=True)
        # date format %Y-%m-%d

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.cascade

