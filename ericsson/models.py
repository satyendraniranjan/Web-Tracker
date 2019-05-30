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



class EricssonRSATracker(models.Model):
        admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='',null=True,related_name='ericssonrsaadmin')
        board = models.ForeignKey(Ericsson_Count, related_name='ericssonrsa', on_delete=models.CASCADE)
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
                ('2.5 TDD mMIMO', '2.5 TDD mMIMO'),
                ('2.5 5G', '2.5 5G'),

        )

        Technology = models.CharField(max_length=255, choices=Technology_CHOICES1,blank=True)



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

        eNB = models.CharField(max_length=255, default='', blank=True)

        ENM_CHOICES = (
                ('ATL01', 'ATL01'),
                ('FTW02', 'FTW02'),
                ('FTW03', 'FTW03'),

        )

        ENM = models.CharField(max_length=255,choices=ENM_CHOICES, blank=True)
        IP_OAM = models.CharField(max_length=255, default='', blank=True)
        RSA_Hold_Reason = models.CharField(max_length=255, default='', blank=True)
        Remark = models.CharField(max_length=255, default='', blank=True)

        Lock_Unlock_Remark = models.CharField(max_length=255, default='', blank=True)

        RSD_Airboss_choices = (
                ('Kevin.2.Ryan@sprint.com', 'Kevin.2.Ryan@sprint.com'),
                ('Kristin.Nickerson@sprint.com', 'Kristin.Nickerson@sprint.com'),
                ('Michael.Ochieng@sprint.com', 'Michael.Ochieng@sprint.com'),
                ('Mary.Gillihan@sprint.com', 'Mary.Gillihan@sprint.com'),
                ('Denise.Rhoads@sprint.com', 'Denise.Rhoads@sprint.com'),
                ('Beverly.Pass@sprint.com', 'Beverly.Pass@sprint.com'),
                ('Jannifer.Lancaster@sprint.com', 'Jannifer.Lancaster@sprint.com'),
                ('David.Myrsten@sprint.com', 'David.Myrsten@sprint.com'),
                ('Lorenzo.Benton@sprint.com', 'Lorenzo.Benton@sprint.com'),
                ('Jeff.Dominge@sprint.com', 'Jeff.Dominge@sprint.com'),
                ('Jared.Merringer@sprint.com', 'Jared.Merringer@sprint.com'),
                ('Janice.Cook@sprint.com', 'Janice.Cook@sprint.com'),
                ('Michael.2.Nigro@sprint.com', 'Michael.2.Nigro@sprint.com'),
                ('Alejandro.Luna@sprint.com', 'Alejandro.Luna@sprint.com'),
                ('Timothy.Somers@sprint.com', 'Timothy.Somers@sprint.com'),
                ('Barry.Ragsdale@sprint.com', 'Barry.Ragsdale@sprint.com'),
                ('Edward.2.Smith@sprint.com', 'Edward.2.Smith@sprint.com'),
                ('John.Karkoska@sprint.com', 'John.Karkoska@sprint.com'),
                ('Lisa.Backman@sprint.com', 'Lisa.Backman@sprint.com'),
                ('Kenneth.Compton@sprint.com', 'Kenneth.Compton@sprint.com'),
                ('James.Humberson@sprint.com', 'James.Humberson@sprint.com'),
                ('everett.ison@sprint.com', 'everett.ison@sprint.com'),
                ('William.Card@sprint.com', 'William.Card@sprint.com'),
                ('Carl.Merritt@sprint.com', 'Carl.Merritt@sprint.com'),
                ('Claude.Carder@sprint.com', 'Claude.Carder@sprint.com'),
                ('Donald.Pestuglicci@sprint.co', 'Donald.Pestuglicci@sprint.co'),
                ('Nathan.2.Lancaster@sprint.c', 'Nathan.2.Lancaster@sprint.c'),
                ('LA Metro', 'LA Metro'),
                ('Jason.Hughes@sprint.com', 'Jason.Hughes@sprint.com'),
                ('William.Scott@sprint.com', 'William.Scott@sprint.com'),
                ('Jeffrey.Brannan@sprint.com', 'Jeffrey.Brannan@sprint.com'),
                ('Thomas.Poitras@sprint.com', 'Thomas.Poitras@sprint.com'),
                ('Ronald.2.Morese@sprint.com', 'Ronald.2.Morese@sprint.com'),
                ('Keith.L.Lee@sprint.com', 'Keith.L.Lee@sprint.com'),
                ('Jesus.Machado@sprint.com', 'Jesus.Machado@sprint.com'),
                ('Terry.Stanford@sprint.com', 'Terry.Stanford@sprint.com'),
                ('Kristen.A.Moore@sprint.com', 'Kristen.A.Moore@sprint.com'),
                ('Dean.Spacone@sprint.com', 'Dean.Spacone@sprint.com'),
                ('Richard.Helmbright@sprint.com', 'Richard.Helmbright@sprint.com'),
                ('Dwayne.Baker@sprint.com', 'Dwayne.Baker@sprint.com'),
                ('Brian.Goretcki@sprint.com', 'Brian.Goretcki@sprint.com'),
                ('Erskine.Heatherley@sprint.com', 'Erskine.Heatherley@sprint.com'),
                ('Elizabeth.Riola@sprint.com', 'Elizabeth.Riola@sprint.com'),
                ('James.3.Moore@sprint.com', 'James.3.Moore@sprint.com'),
                ('Sidney.Pollard@sprint.com', 'Sidney.Pollard@sprint.com'),
                ('Matthew.Spiak@sprint.com', 'Matthew.Spiak@sprint.com'),
                ('Jeffrey.Wagner@sprint.com', 'Jeffrey.Wagner@sprint.com'),
                ('Michael.Moore@sprint.com', 'Michael.Moore@sprint.com'),
                ('Scott.Schultz@sprint.com', 'Scott.Schultz@sprint.com'),
                ('Jerry.Smith@sprint.com', 'Jerry.Smith@sprint.com'),
                ('James.Breakey@sprint.com', 'James.Breakey@sprint.com'),
                ('Brock.Hurlbert@sprint.com', 'Brock.Hurlbert@sprint.com'),
                ('Edward.T.Tudor@sprint.com', 'Edward.T.Tudor@sprint.com'),
                ('Ronald.Recine@sprint.com', 'Ronald.Recine@sprint.com'),
                ('Arnold.Neugaard@sprint.com', 'Arnold.Neugaard@sprint.com'),
                ('Logan.X.Hall@sprint.com', 'Logan.X.Hall@sprint.com'),
                ('Gregory.Plante@sprint.com', 'Gregory.Plante@sprint.com'),
                ('Scott.Hanks@sprint.com', 'Scott.Hanks@sprint.com'),
                ('Nasim.Raza@sprint.com', 'Nasim.Raza@sprint.com'),
                ('Adam.Shelton@sprint.com', 'Adam.Shelton@sprint.com'),
                ('blaine.rubenacker@sprint.com', 'blaine.rubenacker@sprint.com'),
                ('Paula.Staver@sprint.com', 'Paula.Staver@sprint.com'),
                ('Curtis.Eberspacher@sprint.com', 'Curtis.Eberspacher@sprint.com'),

        )

        RSD_Airboss_Mail = models.EmailField(max_length=255, choices= RSD_Airboss_choices, blank=True)
        Augment_ID = models.CharField(max_length=255, default='', blank=True)

        Volte_Soft_CHOICES = (
                ('WIP', 'WIP'),
                ('Completed', 'Completed'),

        )

        Final_RSA_Status = models.CharField(max_length=255, choices=Volte_Soft_CHOICES, blank=True)

        Volte_Soft_Latest_Software = (
                ('Yes', 'Yes'),
                ('No', 'No'),
                ('NA', 'NA'),
        )

        Latest_Software_Version = models.CharField(max_length=255, choices=Volte_Soft_Latest_Software, blank=True)

        Site_Unlock_Choice = (
                ('Site', 'Site'),
                ('Sector', 'Sector'),
                ('Carrier', 'Carrier'),
        )

        Site_Unlock_Status = models.CharField(max_length=255, choices=Site_Unlock_Choice, blank=True)

        Volte_Soft_CHOICES7 = (
                ('Yes', 'Yes'),
                ('No', 'No'),
                ('NA', 'NA'),
        )

        Volte_Soft_Launch = models.CharField(max_length=255, choices=Volte_Soft_CHOICES7, blank=True)

        Activity_CHOICESPTRV = (
                ('FTW_Houston', 'FTW_Houston'),
                ('KC_Atlanta', 'KC_Atlanta'),
                ('Orlando_miami', 'Orlando_miami'),
                ('NA', 'NA'),
        )
        MME_Pool = models.CharField(max_length=255, default='',choices=Activity_CHOICESPTRV,blank=True)


        Activity_CHOICESSV = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )

        TVW_Available = models.CharField(max_length=255, default='',choices=Activity_CHOICESSV,blank=True)

        Activity_CHOICESF = (

                ('Yes', 'Yes'),
                ('No', 'No'),
                ('NA', 'NA'),
        )
        TVW_Available_FMCC_Database = models.CharField(max_length=255, default='',choices=Activity_CHOICESF,blank=True)

        Activity_CHOICESA = (
                ('Yes', 'Yes'),
                ('No', 'No'),

        )
        Acd_Status = models.CharField(max_length=255, default='',choices=Activity_CHOICESA,blank=True)

        Notification_To_RSD_CHOICEST = (
                ('Yes', 'Yes'),
                ('No', 'No'),
                ('NA', 'NA'),
        )

        Notification_To_RSD = models.CharField(max_length=255, default='', choices= Notification_To_RSD_CHOICEST, blank=True)


        Activity_CHOICEST = (
                ('Individual email sent to RSD', 'Individual email sent to RSD'),
                ('informational only, no action required', 'informational only, no action required'),
                ('send completed ACD/TVW to West', 'send completed ACD/TVW to West'),

        )

        TVW_Related_Remarks = models.CharField(max_length=255, default='',choices=Activity_CHOICEST,blank=True)





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



        OAR_Date = models.DateField(null=True,blank=True)
        OAC_Date = models.DateField(null=True,blank=True)
        LATP_Date = models.DateField(null=True, blank=True)
        Site_Last_Logged_Date = models.DateField(null=True, blank=True)
        created_date = models.DateTimeField(default=timezone.now)
        Date = models.DateTimeField(null=True,blank=True)
        # date format %Y-%m-%d

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.cascade

