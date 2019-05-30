from django.shortcuts import redirect
from ericsson.forms import EricssonPostComTrackerForm,EricsssonRSATrackerForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from ericsson.models import EricssonPostComTracker, EricssonRSATracker, Ericsson_Count
from django.http import HttpResponse
import csv
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect




@login_required
def ericssontracker_list(request):

        latest_tracker_list = EricssonPostComTracker.objects.order_by('-created_date')
        context = {
            'latest_tracker_list': latest_tracker_list,
       }
        return render(request, 'ericsson/ericssontracker_list1.html', context)


@login_required
def ericssontracker_new(request):
    if request.method == "POST":
        form = EricssonPostComTrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.board = Ericsson_Count.objects.get(id=2)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('ericssontracker_list')
    else:
        form = EricssonPostComTrackerForm
    return render(request, 'ericsson/ericssontracker_edit.html', {'form': form})



@login_required
def ericssontracker_detail(request, pk):
    tracker = get_object_or_404(EricssonPostComTracker, pk=pk)
    return render(request, 'ericsson/ericssontracker_list.html', {'tracker': tracker})


@login_required
def ericssontracker_edit(request, pk):
    tracker = get_object_or_404(EricssonPostComTracker, pk=pk)
    if request.method == "POST":
        form = EricssonPostComTrackerForm(request.POST)
#        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.board = Ericsson_Count.objects.get(id=2)
            tracker.board = Ericsson_Count.objects.get(id=2)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('ericssontracker_list')
    else:
        form = EricssonPostComTrackerForm(instance=tracker)
    return render(request, 'ericsson/ericssontracker_edit.html', {'form': form})

@login_required
def ericssontracker_edit1(request, pk):
    tracker = get_object_or_404(EricssonPostComTracker, pk=pk)
    if request.method == "POST":
        form = EricssonPostComTrackerForm(request.POST, instance=tracker)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.board = Ericsson_Count.objects.get(id=2)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('ericssontracker_list')
    else:
        form = EricssonPostComTrackerForm(instance=tracker)
    return render(request, 'ericsson/ericssontracker_edit.html', {'form': form})


def ericssonexport(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Ericsson_Post_Com_Tracker.csv"'

    writer = csv.writer(response)
    writer.writerow(['System Date','User Date','User Name','Assignee','cascade','eNB','Technology', 'ENM','IP_OAM','Market','Volte_Soft','CSMS','FE_Name','Tech_Email','Tech_Contact','CIC_Airboss_Mail','RSD_Airboss_Mail','RSD_Manager_Mail','Construction_Manager_Mail','Activity','Activity_status','Site_Status_pre_Activity','Secondary_Fibre_check', 'Site_Status_post_Activity','Kpi_Profile','Remarks','Revisit_Required','Revisit','Site_Pre_Status','Site_Post_Status','OAR_Date','OAC_Date'])

    latest_tracker_list1 = EricssonPostComTracker.objects.order_by('-created_date')
    for item in latest_tracker_list1:
        writer.writerow([item.created_date,item.Date,item.admin,item.admin,item.cascade,item.eNB, item.Technology, item.ENM, item.IP_OAM, item.Market, item.Volte_Soft, item.CSMS, item.FE_Name, item.Tech_Email,item.Tech_Contact, item.CIC_Airboss_Mail,item.RSD_Airboss_Mail,item.Construction_Manager_Mail,item.Activity, item.Activity_status, item.Site_Status_pre_Activity, item.Secondary_Fibre_check, item.Site_Status_post_Activity,item.Kpi_Profile,item.Remarks,item.Revisit_Required,item.Revisit,item.Site_Pre_Status,item.Site_Post_Status,item.OAR_Date,item.OAC_Date])

    return response

@login_required
def ericssonpostcomsearch(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(cascade__icontains=query) | Q(admin__username__icontains=query)

            results = EricssonPostComTracker.objects.filter(lookups).distinct().order_by('-created_date')

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'ericsson/ericssonpostcomsearch.html', context)

        else:
            return render(request, 'ericsson/ericssonpostcomsearch.html')

    else:
        return render(request, 'ericsson/ericssonpostcomsearch.html')




@login_required
def ericssonrsatracker_new(request):
    if request.method == "POST":
        form = EricsssonRSATrackerForm(request.POST)
        if form.is_valid():
            rsatracker = form.save(commit=False)
            rsatracker.admin = request.user
            rsatracker.board = Ericsson_Count.objects.get(id=2)
            rsatracker.created_date = timezone.now()
            rsatracker.save()
            return redirect('ericssonrsatracker_list')

    else:
        form = EricsssonRSATrackerForm
    return render(request, 'ericsson/rsaericsson/ericssonrsatracker_edit.html', {'form': form})

@login_required
def ericssonrsatracker_list(request):
        latest_tracker_list = EricssonRSATracker.objects.order_by('-created_date')
        context = {
            'latest_tracker_list': latest_tracker_list,
       }
        return render(request, 'ericsson/rsaericsson/ericssonrsatracker_list.html', context)

def ericssonExportRsaTracker(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RSATracker.csv"'

    writer = csv.writer(response)
    writer.writerow(['System Date','User Date','User Name','Assignee','cascade','Market','Technology', 'eNodeB_Name/Cell ID', 'ENM','LATP Complete Date','MME Pool form Appian','IP Adress OAM','Remark','RSA Holdup Reason', 'Site Last Logged in Date', 'Volte Soft Launch','Site Pre-Conditions', 'Site Post-Conditions','OAR_Date','OAC_Date','RSA Final STATUS','Latest Software Version','Sector/Site Unlock status','LOCK/Unlock Remarks','TVW available/actualized in SV','TVW available in FMCC Database','ACD Status','TVW/ACD Notification sent to RSD','Remarks to RSD','RSD email ID','Augment ID'])

    latest_tracker_list1 = EricssonRSATracker.objects.order_by('-created_date')
    for item in latest_tracker_list1:
        writer.writerow([item.created_date,item.Date,item.admin,item.Assignee,item.cascade,item.Market, item.Technology, item.eNB, item.ENM, item.LATP_Date,item.MME_Pool,item.IP_OAM,item.Remark,item.RSA_Hold_Reason,item.Site_Last_Logged_Date, item.Volte_Soft_Launch ,item.Site_Status_pre_Activity, item.Site_Status_post_Activity,item.OAR_Date,item.OAC_Date,item.Final_RSA_Status,item.Latest_Software_Version,item.Site_Unlock_Status,item.TVW_Available,item.TVW_Available_FMCC_Database,item.Acd_Status,item.Notification_To_RSD,item.TVW_Related_Remarks,item.RSD_Airboss_Mail,item.Augment_ID])

    return response

@login_required
def ericssonrsasearch(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(cascade__icontains=query) | Q(User_Name__username__icontains=query)

            results = EricssonRSATracker.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'rsatracker/ericssonrsasearch.html', context)

        else:
            return render(request, 'rsatracker/ericssonrsasearch.html')

    else:
        return render(request, 'rsatracker/ericssonrsasearch.html')

@login_required
def ericssonrsatracker_edit(request, pk):
    tracker = get_object_or_404(EricssonRSATracker, pk=pk)
    if request.method == "POST":
        form = EricsssonRSATrackerForm(request.POST)
#        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.User_Name = request.user
            tracker.board = Ericsson_Count.objects.get(id=2)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('ericssonrsatracker_list')
    else:
        form = EricsssonRSATrackerForm(instance=tracker)
    return render(request, 'rsaericsson/ericssonrsatracker_edit.html', {'form': form})

@login_required
def ericssonrsatracker_edit1(request, pk):
    tracker = get_object_or_404(EricssonRSATracker, pk=pk)
    if request.method == "POST":
        form = EricsssonRSATrackerForm(request.POST, instance=tracker)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.User_Name = request.user
            tracker.board = Ericsson_Count.objects.get(id=2)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('ericssonrsatracker_list')
    else:
        form = EricsssonRSATrackerForm(instance=tracker)
    return render(request, 'rsaericssson/ericssonrsatracker_edit.html', {'form': form})
