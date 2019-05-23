from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from ericsson.models import EricssonPostComTracker, Ericsson_Count, EricssonProfile,EricssonRSATracker



@admin.register(EricssonPostComTracker)
class TrackerAdmin(ImportExportModelAdmin):

    list_display = ('cascade', 'Technology', 'admin', 'created_date')
    fieldsets = [
        ('Tracker Information', {'fields': ['admin','Assignee','cascade','Technology', 'Market', 'eNB','ENM','IP_OAM','Tech_Email','Tech_Contact','CIC_Airboss_Mail','RSD_Airboss_Mail','RSD_Manager_Mail','Construction_Manager_Mail', 'CSMS', 'FE_Name','Site_Status_pre_Activity', 'Site_Status_post_Activity','Remarks','OAR_Date','OAC_Date','Secondary_Fibre_check','Site_Pre_Status','Site_Post_Status','Kpi_Profile','Revisit_Required','Revisit'], 'classes': ['collapse']}),
        ('Date Information', {'fields': ['created_date','Date']}),
    ]
    list_filter = ['created_date']
    search_fields = ['cascade']
    actions = ['download_csv']


admin.site.register(Ericsson_Count)
admin.site.register(EricssonProfile)


@admin.register(EricssonRSATracker)
class RSATrackerAdmin(ImportExportModelAdmin):

    list_display = ('cascade', 'Technology', 'admin', 'created_date')
    fieldsets = [
        ('Tracker Information', {'fields': ['Date','admin','board','Assignee','cascade','Market', 'Technology',  'eNB', 'ENM', 'LATP_Date', 'MME_Pool', 'IP_OAM','Remark', 'RSA_Hold_Reason', 'Site_Last_Logged_Date', 'Volte_Soft_Launch','Site_Status_pre_Activity', 'Site_Status_post_Activity','OAR_Date','OAC_Date','Final_RSA_Status','Latest_Software_Version', 'Site_Unlock_Status', 'Lock_Unlock_Remark', 'TVW_Available','TVW_Available_FMCC_Database','Acd_Status','Notification_To_RSD','TVW_Related_Remarks','RSD_Airboss_Mail','Augment_ID'], 'classes': ['collapse']}),
        ('Date Information', {'fields': ['created_date']}),
    ]
    list_filter = ['created_date']
    search_fields = ['cascade']
    actions = ['download_csv']