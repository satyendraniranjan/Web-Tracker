from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import fields, CheckboxInput
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class TrackerForm(forms.ModelForm):


    cascade = forms.CharField(required=True)
    eNB = forms.CharField(required=True)
    LSM = forms.CharField(required=True)
    CSMS = forms.CharField(required=True)
    FE_Name = forms.CharField(required=True)


    class Meta:
        model = Tracker
        fields = ('cascade','Date','Assignee','Technology', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication', 'Activity', 'Activity_status', 'Site_Status_pre_Activity', 'Site_Status_post_Activity','E_Link_Status_of_BH0_for_CDU30','MJ_Object_Marked','RET','Alarms_Preventing_RET_Config','Frequency_Earfcn_Checked_from_LSM_BSM','IP_Route_or_IP_Address','Volte_MME_IP_Config','Review_LATP_Complete','Remarks','OAR_Date','OAC_Date','Lock_Unlock_Verified_By','Verify_Status','Final_Comments')
        widgets = {
            'Date': DateInput(),
            'OAC_Date': DateInput(),
            'OAR_Date': DateInput(),
        }
    def __init__(self,*args, **kwargs):
        super(TrackerForm, self).__init__(*args, **kwargs)
#        self.fields['Assignee'] = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Samsung Users'))
        self.fields['Assignee'].required = True
        self.fields['Market'].required = True
        self.fields['Date'].required = True
        self.fields['Type'].required = True
        self.fields['Technology'].required = True
        self.fields['Bandwidth_Checked_From_LSM'].required = True
        self.fields['Mode_of_Communication'].required = True
        self.fields['Activity'].required = True
        self.fields['Activity_status'].required = True
        self.fields['Site_Status_pre_Activity'].required = True


class RSATrackerForm(forms.ModelForm):

    cascade = forms.CharField(required=True)
#    Market = forms.CharField(required=True)
    eNB = forms.CharField(required=True)
    LSM = forms.CharField(required=True)
    SiteType = forms.CharField(required=True)
    CSMS = forms.CharField(required=True)
#    Type = forms.CharField(required=True)
#    Technology = forms.CharField(required=True)
    Schedule_Name = forms.CharField(required=True)



    def __init__(self,*args, **kwargs):
        super(RSATrackerForm, self).__init__(*args, **kwargs)
        self.fields['Assignee'] = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Samsung Users'))
        self.fields['TVW_Available'].label = "TVW Available in SV"
#        self.fields['LSM'].help_text = "LSM want to be sure!"
        self.fields['Market'].required = True
        self.fields['Type'].required = True
        self.fields['Technology'].required = True


    def clean(self, *args, **kwargs):
        cascade = self.cleaned_data.get('cascade', '').strip()
        Type = self.cleaned_data.get('type', '').strip()
        RET = self.cleaned_data.get('ret', '').strip()
        Fail = self.cleaned_data.get('fail', '').strip()
        self.cleaned_data.get('eNB', '').strip()

        """   if cascade not in ['Satyendra', 'Niranjan']:
                msg = "Must fill something."
                self.fields['RET'].required=True
                self.add_error('Type', msg)
                self.add_error('cascade', msg)
                raise forms.ValidationError("Emails don't match")
                return self.cleaned_data
            if RET:
                msg = "Must fill something."
                self.add_error('RET', msg)
            if not Fail:
                msg = "Must fill something."
                self.add_error('Fail', msg)"""




    class Meta:
        model = RSATracker
        fields = ('Date','CSMS','cascade','Market', 'eNB', 'LSM','SiteType','Type','Technology','Schedule_Name','Assignee','Fail','Fail_Reason','RET','RTRV_SON_SO_status','Ticket_Raised_For_Issue','Ticket_no', 'Site_Status_pre_Activity', 'Site_Status_post_Activity','OAR_Date','OAC_Date','TVW_Available','TVW_Available_FMCC_Database','Acd_Status','TVW_Related_Remarks','Other_Remarks','Lock_Unlock_Verified_By','SV_Actualization')
        widgets = {
            'Date': DateInput(),
            'OAC_Date': DateInput(),
            'OAR_Date': DateInput(),
            'SV_Actualization': DateInput(),
        }




class ContactForm(forms.Form):

    CHOICES = (
        (11, 'Credit Card'),
        (12, 'Student Loans'),
        (13, 'Taxes'),
        (21, 'Books'),
        (22, 'Games'),
        (31, 'Groceries'),
        (32, 'Restaurants'),
    )

    category = forms.ChoiceField(choices=CHOICES,required=False)
    #    email = forms.EmailField(max_length=254, required=False)
    is_sat = forms.BooleanField()
    name = forms.CharField(max_length=30,required=False)
    email = forms.EmailField(max_length=254,required=False)
#    choice = forms.ChoiceField()

    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput(),
        required=False
    )


    """def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get("name")
        category = cleaned_data.get('category')
        is_sat = cleaned_data.get("is_sat")
        if name == 'name':
            raise ValidationError('Draft entries may not have a publication date.')
        if category == '':
            raise ValidationError('This is Value error.')
        if not is_sat:
            raise ValidationError('This is a is_sat error')"""



#        if self.fields['is_sat']:
#             self.fields['email'].required = False
#        else:
#           self.fields['email'].required = True


    def __init__(self,*args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = forms.ModelChoiceField(queryset=User.objects.all())
        self.fields['is_sat'].widget=CheckboxInput()
        self.fields['name'].required = True
        if self.fields['name']:
             self.fields['profile'] = forms.CharField(max_length=200)
             self.fields['profile'].initial = 'whatever you want'

        if not self.fields['name']:
             self.fields['profile'] = forms.CharField(max_length=200)
             self.fields['profile'].initial = 'whatever you want'


