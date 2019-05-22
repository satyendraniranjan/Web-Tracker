from ericsson.models import EricssonPostComTracker
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class EricssonPostComTrackerForm(forms.ModelForm):


    cascade = forms.CharField(required=True)
    eNB = forms.CharField(required=True)
    CSMS = forms.CharField(required=True)
    FE_Name = forms.CharField(required=True)

    class Meta:
        model = EricssonPostComTracker
        fields = ('Date','Assignee','cascade','eNB','Technology', 'ENM','IP_OAM','Market','Volte_Soft','CSMS','FE_Name','Tech_Email','Tech_Contact','CIC_Airboss_Mail','RSD_Airboss_Mail','RSD_Manager_Mail','Construction_Manager_Mail','Activity','Activity_status','Site_Status_pre_Activity','Secondary_Fibre_check', 'Site_Status_post_Activity','Kpi_Profile','Remarks','Revisit_Required','Revisit','Site_Pre_Status','Site_Post_Status','OAR_Date','OAC_Date')
        widgets = {
            'Date': DateInput(),
            'OAC_Date': DateInput(),
            'OAR_Date': DateInput(),

        }


    def __init__(self,*args, **kwargs):
        super(EricssonPostComTrackerForm, self).__init__(*args, **kwargs)
        self.fields['Market'].required = True
        self.fields['Date'].required = True
        self.fields['Technology'].required = True
        self.fields['Activity'].required = True
        self.fields['Activity_status'].required = True
        self.fields['Site_Status_pre_Activity'].required = True
        self.fields['eNB'].label = "ENodeB Name"
        self.fields['FE_Name'].label = "FE Name"
        self.fields['Tech_Email'].label = "FE Email"
        self.fields['Tech_Contact'].label = "FE Contact"
        self.fields['CSMS'].label = "CSMS"
        self.fields['Site_Status_pre_Activity'].label = "Cell State before Activity"
        self.fields['Site_Status_post_Activity'].label = "Cell State after Activity"


