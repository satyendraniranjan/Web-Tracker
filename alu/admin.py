from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from alu.models import AluPostComTracker,AluProfile,ALUCounts,AluRsaTracker



@admin.register(AluPostComTracker)
class AluPostTrackerAdmin(ImportExportModelAdmin):

    list_display = ('cascade', 'Technology', 'admin', 'created_date')
    fieldsets = [
        ('Tracker Information', {'fields': ['admin','cascade','Technology','Assignee','board','OEM', 'Market', 'eNB','OSS', 'RSD_Air_Boss','Bridge_No','Onshore_Eng_Name', 'CSMS','FE_Name','Activity_status','Site_Status_pre_Activity', 'Site_Status_post_Activity','OAR_Date','OAC_Date','Pre_Reserve','Post_Reserve','Pre_E_Tilt_Values','Post_E_Tilt_Values','Pre_Max_User_Count','Post_Max_User_Count','Revisit_Required','Is_Pre_Integration_site','Final_Comments'], 'classes': ['collapse']}),
        ('Date Information', {'fields': ['created_date','Date']}),
    ]
    list_filter = ['created_date']
    search_fields = ['cascade']
    actions = ['download_csv']


@admin.register(AluProfile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ('user', 'birth_date')

admin.site.register(ALUCounts)


@admin.register(AluRsaTracker)
class AluRsaTrackerAdmin(ImportExportModelAdmin):

    list_display = ('cascade', 'Technology', 'admin', 'created_date')
    fieldsets = [
        ('Tracker Information', {'fields': ['admin','cascade','Technology','Date','Assignee','OEM', 'Market', 'eNB','OSS','Source','Ageing','Site_Type', 'CSMS','Alarm_Status','OAR_Date','OAC_Date','Nims','ACD','TVW','PRTS','Patrol','Trams','NEO','Initial_Status','Final_Status','Volte_Soft_Launch_Status','Category','SV_3115','Owner','CICO','Remark'], 'classes': ['collapse']}),
        ('Date Information', {'fields': ['created_date','Date']}),
    ]
    list_filter = ['created_date']
    search_fields = ['cascade']
    actions = ['download_csv']
