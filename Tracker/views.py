from django.shortcuts import redirect
from .forms import *
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
import csv
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .resources import *
from django.views.generic import ListView
from django.db.models import Q


class TrackerListView(ListView):
    model = Samsung
    context_object_name = 'boards'
    template_name = 'tracker/dashboard.html'

class TrackerListView1(ListView):
    model = Profile
    context_object_name = 'boards'

    template_name = 'tracker/dashboard1.html'



@login_required
def tracker_list(request):

#    if not request.user.is_authenticated:
#        return render(request, 'registration/login.html')
#    else:
#        posts = Tracker.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        latest_tracker_list = Tracker.objects.order_by('-created_date')
        context = {
            'latest_tracker_list': latest_tracker_list,
       }
        return render(request, 'tracker/tracker_list1.html', context)



@login_required
def assignment_list(request):

#    if not request.user.is_authenticated:
#        return render(request, 'registration/login.html')
#    else:
#        posts = Tracker.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        latest_assignment_list = Assignment.objects.order_by('-created_date')
        context = {
            'latest_assignment_list': latest_assignment_list,
       }
        return render(request, 'assignment/assignment_list.html', context)

@login_required
def tracker_new(request):
    if request.method == "POST":
        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('tracker_list')
    else:
        form = TrackerForm
    return render(request, 'tracker/tracker_edit.html', {'form': form})
""" if request.user.is_superuser:
    if request.user.is_staff:
    if request.method == "POST":
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.admin = request.user
            assignment.created_date = timezone.now()
            assignment.save()
            return redirect('assignment_detail', pk=assignment.pk)

    else:
        form = AssignmentForm
    return render(request, 'assignment/assignment_edit.html', {'form': form})
else:"""


@login_required
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    return render(request, 'assignment/assignment_detail.html', {'assignment': assignment})

@login_required
def assignment_edit(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == "POST":
        form = AssignmentForm(request.POST, instance=assignment)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.admin = request.user
            assignment.created_date = timezone.now()
            assignment.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'assignment/assignment_edit.html', {'form': form})

@login_required
def tracker_detail(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    return render(request, 'tracker/tracker_list.html', {'tracker': tracker})


@login_required
def tracker_edit(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method == "POST":
        form = TrackerForm(request.POST)
#        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('tracker_list')
    else:
        form = TrackerForm(instance=tracker)
    return render(request, 'tracker/tracker_edit.html', {'form': form})

@login_required
def tracker_edit1(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method == "POST":
        form = TrackerForm(request.POST, instance=tracker)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('tracker_list')
    else:
        form = TrackerForm(instance=tracker)
    return render(request, 'tracker/tracker_edit.html', {'form': form})


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Post-Com Tracker.csv"'

    writer = csv.writer(response)
    writer.writerow(['System Date','User Date','User Name','cascade','Technology','Assignee', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication', 'Activity', 'Activity_status', 'Site_Status_pre_Activity', 'Site_Status_post_Activity','E_Link_Status_of_BH0_for_CDU30','MJ_Object_Marked','RET','Alarms_Preventing_RET_Config','Frequency_Earfcn_Checked_from_LSM_BSM','IP_Route_or_IP_Address','Volte_MME_IP_Config','Review_LATP_Complete','Remarks','OAR_Date','OAC_Date','Lock_Unlock_Verified_By','Verify_Status','Final_Comments'])

    latest_tracker_list1 = Tracker.objects.order_by('-created_date')
    for item in latest_tracker_list1:
        writer.writerow([item.created_date,item.Date,item.admin,item.cascade, item.Technology,  item.Assignee,item.Type, item.Bandwidth_Checked_From_LSM, item.Market, item.eNB, item.LSM, item.CSMS, item.FE_Name, item.Mode_of_Communication,item.Activity, item.Activity_status, item.Site_Status_pre_Activity, item.Site_Status_post_Activity,item.E_Link_Status_of_BH0_for_CDU30,item.MJ_Object_Marked,item.RET,item.Alarms_Preventing_RET_Config,item.Frequency_Earfcn_Checked_from_LSM_BSM,item.IP_Route_or_IP_Address,item.Volte_MME_IP_Config,item.Review_LATP_Complete,item.Remarks,item.OAR_Date,item.OAC_Date,item.Lock_Unlock_Verified_By,item.Verify_Status,item.Final_Comments])

    return response

def some_view1(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Post-Com Tracker.csv"'

    writer = csv.writer(response)
    writer.writerow(['System Date','User Date','User Name','cascade','Technology','Assignee', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name', 'Mode_of_Communication', 'Activity', 'Activity_status', 'Site_Status_pre_Activity', 'Site_Status_post_Activity','E_Link_Status_of_BH0_for_CDU30','MJ_Object_Marked','RET','Alarms_Preventing_RET_Config','Frequency_Earfcn_Checked_from_LSM_BSM','IP_Route_or_IP_Address','Volte_MME_IP_Config','Review_LATP_Complete','Remarks','OAR_Date','OAC_Date','Lock_Unlock_Verified_By','Verify_Status','Final_Comments'])

    latest_tracker_list1 = Tracker.objects.order_by('-created_date')
    for item in latest_tracker_list1:
        writer.writerow([item.created_date,item.Date,item.admin,item.cascade, item.Technology,  item.Assignee,item.Type, item.Bandwidth_Checked_From_LSM, item.Market, item.eNB, item.LSM, item.CSMS, item.FE_Name, item.Mode_of_Communication,item.Activity, item.Activity_status, item.Site_Status_pre_Activity, item.Site_Status_post_Activity,item.E_Link_Status_of_BH0_for_CDU30,item.MJ_Object_Marked,item.RET,item.Alarms_Preventing_RET_Config,item.Frequency_Earfcn_Checked_from_LSM_BSM,item.IP_Route_or_IP_Address,item.Volte_MME_IP_Config,item.Review_LATP_Complete,item.Remarks,item.OAR_Date,item.OAC_Date,item.Lock_Unlock_Verified_By,item.Verify_Status,item.Final_Comments])

    return response



def Calc_link(request):

    return render(request, 'tracker/Calc_link.html')

@login_required
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(cascade__icontains=query) | Q(admin__username__icontains=query) | Q(Date__icontains=query)

            results = Tracker.objects.filter(lookups).distinct().order_by('-created_date')

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'tracker/search1.html', context)

        else:
            return render(request, 'tracker/search1.html')

    else:
        return render(request, 'tracker/search1.html')


def about(request):
    return render(request, 'tracker/about.html')



def password_change_complete(request):
    return render(request, 'registration/password_reset_complete.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_change_complete')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

def contact_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
                pass

    else:
        form = ContactForm()
    return render(request, 'tracker/name.html', {'form': form})


def export(request):
    person_resource = TrackerResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response


from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        person_resource = TrackerResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

@login_required
def rsatracker_new(request):
    if request.method == "POST":
        form = RSATrackerForm(request.POST)
        if form.is_valid():
            rsatracker = form.save(commit=False)
            rsatracker.User_Name = request.user
            rsatracker.created_date = timezone.now()
            rsatracker.save()
            return redirect('rsatracker_list')

    else:
        form = RSATrackerForm
    return render(request, 'rsatracker/rsatracker_edit.html', {'form': form})

@login_required
def rsatracker_list(request):
        latest_tracker_list = RSATracker.objects.order_by('-created_date')
        context = {
            'latest_tracker_list': latest_tracker_list,
       }
        return render(request, 'rsatracker/rsatracker_list.html', context)

def ExportRsaTracker(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RSATracker.csv"'

    writer = csv.writer(response)
    writer.writerow(['CSMS','cascade','Market', 'eNB', 'LSM','SiteType','Type','Technology','Schedule_Name','User Name','Assignee','Assignment Date','Completion Date','Fail','Fail_Reason','RET','RTRV_SON_SO_status','Ticket_Raised_For_Issue','Ticket_no', 'Site_Status_pre_Activity', 'Site_Status_post_Activity','OAR_Date','OAC_Date','TVW_Available','TVW_Available_FMCC_Database','Acd_Status','TVW_Related_Remarks','Other_Remarks','Lock_Unlock_Verified_By','SV_Actualization'])

    latest_tracker_list1 = RSATracker.objects.order_by('-created_date')
    for item in latest_tracker_list1:
        writer.writerow([item.CSMS,item.cascade,item.Market, item.eNB,item.LSM,item.SiteType,item.Type, item.Technology,item.Schedule_Name,item.User_Name,item.Assignee,item.created_date,item.Date,item.Fail,item.Fail_Reason,item.RET, item.RTRV_SON_SO_status,item.Ticket_Raised_For_Issue,item.Ticket_no, item.Site_Status_pre_Activity, item.Site_Status_post_Activity,item.OAR_Date,item.OAC_Date,item.TVW_Available,item.TVW_Available_FMCC_Database,item.Acd_Status,item.TVW_Related_Remarks,item.Other_Remarks,item.Lock_Unlock_Verified_By,item.SV_Actualization])

    return response


def ExportRsaTracker1(request):
    # Create the HttpResponse object with the appropriate CSV header.
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="RSATracker.csv"'
            writer = csv.writer(response)
            lookups = Q(cascade__icontains=query) | Q(User_Name__username__icontains=query) | Q(Date__icontains=query)

            results = RSATracker.objects.filter(lookups).distinct()
            writer.writerow(['System Date','User Date','User Name','cascade','Technology','Assignee', 'Type', 'Bandwidth_Checked_From_LSM', 'Market', 'eNB', 'LSM', 'CSMS', 'FE_Name','Site_Status_pre_Activity', 'Site_Status_post_Activity','RET','OAR_Date','OAC_Date','Lock_Unlock_Verified_By','SV_Actualization','Other_Remarks','SiteType','Schedule_Name','Fail','Fail_Reason','RTRV_SON_SO_status','Ticket_Raised_For_Issue','Ticket_no','TVW_Available','TVW_Available_FMCC_Database','Acd_Status','TVW_Related_Remarks'])

            latest_tracker_list1 = results
            for item in latest_tracker_list1:
                writer.writerow([item.created_date,item.Date,item.User_Name,item.cascade, item.Technology,item.Assignee, item.Type, item.Bandwidth_Checked_From_LSM, item.Market, item.eNB, item.LSM, item.CSMS, item.FE_Name,item.Site_Status_pre_Activity, item.Site_Status_post_Activity,item.RET,item.OAR_Date,item.OAC_Date,item.Lock_Unlock_Verified_By,item.SV_Actualization,item.Other_Remarks,item.SiteType,item.Schedule_Name,item.Fail,item.Fail_Reason,item.RTRV_SON_SO_status,item.Ticket_Raised_For_Issue,item.Ticket_no,item.TVW_Available,item.TVW_Available_FMCC_Database,item.Acd_Status,item.TVW_Related_Remarks])

            return response
        else:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="RSATracker.csv"'
            writer = csv.writer(response)


            return response



@login_required
def rsasearch(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(cascade__icontains=query) | Q(User_Name__username__icontains=query) | Q(Date__icontains=query)

            results = RSATracker.objects.filter(lookups).distinct()


            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'rsatracker/rsasearch.html', context)

        else:
            return render(request, 'rsatracker/rsasearch.html')

    else:
        return render(request, 'rsatracker/rsasearch.html')

@login_required
def rsatracker_edit(request, pk):
    tracker = get_object_or_404(RSATracker, pk=pk)
    if request.method == "POST":
        form = RSATrackerForm(request.POST)
#        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.User_Name = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('rsatracker_list')
    else:
        form = RSATrackerForm(instance=tracker)
    return render(request, 'rsatracker/rsatracker_edit.html', {'form': form})

@login_required
def rsatracker_edit1(request, pk):
    tracker = get_object_or_404(RSATracker, pk=pk)
    if request.method == "POST":
        form = RSATrackerForm(request.POST, instance=tracker)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.User_Name = request.user
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('rsatracker_list')
    else:
        form = RSATrackerForm(instance=tracker)
    return render(request, 'rsatracker/rsatracker_edit.html', {'form': form})



"""def rsaexport(request):
    person_resource = TrackerResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response


from tablib import Dataset

def rsasimple_upload(request):
    if request.method == 'POST':
        person_resource = TrackerResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/rsasimple_upload.html')"""
