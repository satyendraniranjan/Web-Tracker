from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

#class Trackertabular(admin.TabularInline):
 #   model = Tracker
 #   fk_name = "title"

@admin.register(Tracker)
class TrackerAdmin(ImportExportModelAdmin):

    list_display = ('cascade', 'Technology', 'admin', 'created_date','Assignee')
    fieldsets = [
        ('Tracker Information', {'fields': ['admin','Assignee','cascade','Technology', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication','Activity','Site_Status_pre_Activity', 'Site_Status_post_Activity','E_Link_Status_of_BH0_for_CDU30','MJ_Object_Marked','RET','Alarms_Preventing_RET_Config','Frequency_Earfcn_Checked_from_LSM_BSM','IP_Route_or_IP_Address','Volte_MME_IP_Config','Review_LATP_Complete','Remarks','OAR_Date','OAC_Date','Lock_Unlock_Verified_By','Final_Comments'], 'classes': ['collapse']}),
        ('Date Information', {'fields': ['created_date','Date']}),
    ]
    list_filter = ['created_date']
    search_fields = ['cascade']
    actions = ['download_csv']


@admin.register(RSATracker)
class RSATrackerAdmin(ImportExportModelAdmin):

    list_display = ('cascade', 'Technology', 'User_Name', 'created_date')
    fieldsets = [
        ('Tracker Information', {'fields': ['User_Name','cascade','Technology', 'Type','Assignee',  'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Site_Status_pre_Activity', 'Site_Status_post_Activity','RET','OAR_Date','OAC_Date','Lock_Unlock_Verified_By','SV_Actualization','Other_Remarks','SiteType','Schedule_Name','Fail','Fail_Reason','RTRV_SON_SO_status','Ticket_Raised_For_Issue','Ticket_no','TVW_Available','TVW_Available_FMCC_Database','Acd_Status','TVW_Related_Remarks'], 'classes': ['collapse']}),
        ('Date Information', {'fields': ['created_date','Date']}),
    ]
    list_filter = ['created_date']
    search_fields = ['cascade']
    actions = ['download_csv']




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ('user', 'birth_date')
    list_filter = ['birth_date']

admin.site.register(Samsung)



