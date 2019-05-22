from alu.models import AluPostComTracker, AluRsaTracker
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class AluPostComTrackerForm(forms.ModelForm):


    cascade = forms.CharField(required=True)
    CSMS = forms.CharField(required=True)
    FE_Name = forms.CharField(required=True)

    class Meta:
        model = AluPostComTracker
        fields = ('cascade','Date','Technology', 'Assignee','OEM', 'Market', 'eNB','OSS', 'RSD_Air_Boss','Bridge_No','Onshore_Eng_Name', 'CSMS','FE_Name','Activity_status','Site_Activity_Type','Site_Status_pre_Activity', 'Site_Status_post_Activity','OAR_Date','OAC_Date','Pre_Reserve','Post_Reserve','Pre_E_Tilt_Values','Post_E_Tilt_Values','Pre_Max_User_Count','Post_Max_User_Count','Revisit_Required','Is_Pre_Integration_site','Final_Comments')
        widgets = {
            'Date': DateInput(),
            'OAC_Date': DateInput(),
            'OAR_Date': DateInput(),
        }
    def __init__(self,*args, **kwargs):
        super(AluPostComTrackerForm, self).__init__(*args, **kwargs)
        self.fields['Market'].required = True
        self.fields['Assignee'].required = True
        self.fields['Bridge_No'].required = True
        self.fields['Date'].required = True
        self.fields['OEM'].required = True
        self.fields['Technology'].required = True
        self.fields['Site_Activity_Type'].required = True
        self.fields['Pre_Reserve'].label = "Pre Reserve/Not Reserve"
        self.fields['Post_Reserve'].label = "Post Reserve/Not Reserve"



class AluRsaTrackerForm(forms.ModelForm):



    class Meta:
        model = AluRsaTracker
        fields = ('cascade','Technology','Date','Assignee','OEM', 'Market', 'eNB','OSS','Source','Ageing','Site_Type', 'CSMS','Alarm_Status','OAR_Date','OAC_Date','Nims','ACD','TVW','PRTS','Patrol','Trams','NEO','Initial_Status','Final_Status','Volte_Soft_Launch_Status','Category','SV_3115','Owner','CICO','Remark')
        widgets = {
            'Date': DateInput(),
        }
    def __init__(self,*args, **kwargs):
        super(AluRsaTrackerForm, self).__init__(*args, **kwargs)
        self.fields['Assignee'].required = False
        self.fields['Source'].required = False
        self.fields['Site_Type'].required = False
        self.fields['OEM'].label = "BTS/OEM"
        self.fields['OAR_Date'].label = "OAR"
        self.fields['OAC_Date'].label = "OAC"
        self.fields['Patrol'].label = "PATROL"
        self.fields['Trams'].label = "TRAMPS"
        self.fields['Nims'].label = "NIMS"

