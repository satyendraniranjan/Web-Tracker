from django.shortcuts import redirect
from alu.forms import AluPostComTrackerForm, AluRsaTrackerForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from alu.models import AluPostComTracker,AluProfile,ALUCounts,AluRsaTracker
from django.http import HttpResponse
import csv
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import ListView




class AluTrackerListView(ListView):
    model = ALUCounts
    context_object_name = 'boards'
    template_name = 'alu/aludashboard.html'

class AluTrackerListView1(ListView):
    model = AluProfile
    context_object_name = 'boards'

    template_name = 'alu/aludashboard1.html'


@login_required
def alutracker_list(request):

#    if not request.user.is_authenticated:
#        return render(request, 'registration/login.html')
#    else:
#        posts = Tracker.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        latest_tracker_list = AluPostComTracker.objects.order_by('-created_date')
        context = {
            'latest_tracker_list': latest_tracker_list,
       }
        return render(request, 'alu/alutracker_list.html', context)


@login_required
def alutracker_new(request):
    if request.method == "POST":
        form = AluPostComTrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.board = ALUCounts.objects.get(id=2)
            tracker.created_date = timezone.now()

            tracker.save()
            return redirect('alutracker_list')
    else:
        form = AluPostComTrackerForm
    return render(request, 'alu/tracker_edit.html', {'form': form})



@login_required
def alutracker_detail(request, pk):
    tracker = get_object_or_404(AluPostComTracker, pk=pk)
    return render(request, 'alu/tracker_list.html', {'tracker': tracker})


@login_required
def alutracker_edit(request, pk):
    tracker = get_object_or_404(AluPostComTracker, pk=pk)
    if request.method == "POST":
        form = AluPostComTrackerForm(request.POST)
#        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.board = ALUCounts.objects.get(id=2)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('alutracker_list')
    else:
        form = AluPostComTrackerForm(instance=tracker)
    return render(request, 'alu/tracker_edit.html', {'form': form})

@login_required
def alutracker_edit1(request, pk):
    tracker = get_object_or_404(AluPostComTracker, pk=pk)
    if request.method == "POST":
        form = AluPostComTrackerForm(request.POST, instance=tracker)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.board = ALUCounts.objects.get(id=2)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('alutracker_list')
    else:
        form = AluPostComTrackerForm(instance=tracker)
    return render(request, 'alu/tracker_edit.html', {'form': form})


def Alu_Export(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ALU-Post-Com Tracker.csv"'

    writer = csv.writer(response)
    writer.writerow(['System Date','User Date','User Name','cascade','Technology', 'Assignee','OEM', 'Market', 'eNB','OSS', 'RSD_Air_Boss','Bridge_No','Onshore_Eng_Name', 'CSMS','FE_Name','Activity','Activity_status','Site_Activity_Type','Site_Status_pre_Activity', 'Site_Status_post_Activity','OAR_Date','OAC_Date','Pre_Reserve','Post_Reserve','Pre_E_Tilt_Values','Post_E_Tilt_Values','Pre_Max_User_Count','Post_Max_User_Count','Revisit_Required','Is_Pre_Integration_site','Final_Comments'])

    latest_tracker_list1 = AluPostComTracker.objects.order_by('-created_date')
    for item in latest_tracker_list1:
        writer.writerow([item.created_date,item.Date,item.admin,item.cascade, item.Technology, item.Assignee,item.OEM, item.Market, item.eNB, item.OSS, item.RSD_Air_Boss, item.Bridge_No,item.Onshore_Eng_Name,item.CSMS,item.FE_Name,item.Site_Activity_Type, item.Activity_status, item.Site_Status_pre_Activity, item.Site_Status_post_Activity,item.OAR_Date,item.OAC_Date,item.Pre_Reserve,item.Post_Reserve,item.Post_E_Tilt_Values,item.Pre_E_Tilt_Values,item.Pre_Max_User_Count,item.Post_Max_User_Count,item.Revisit_Required,item.Is_Pre_Integration_site,item.Final_Comments])

    return response

@login_required
def alusearch(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(cascade__icontains=query) | Q(admin__username__icontains=query)

            results = AluPostComTracker.objects.filter(lookups).distinct().order_by('-created_date')

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'alu/alusearch.html', context)

        else:
            return render(request, 'alu/alusearch.html')

    else:
        return render(request, 'alu/alusearch.html')




@login_required
def Alursatracker_new(request):
    if request.method == "POST":
        form = AluRsaTrackerForm(request.POST)
        if form.is_valid():
            rsatracker = form.save(commit=False)
            rsatracker.admin = request.user
            rsatracker.board = ALUCounts.objects.get(id=1)
            rsatracker.created_date = timezone.now()
            rsatracker.save()
            return redirect('Alursatracker_list')

    else:
        form = AluRsaTrackerForm
    return render(request, 'alursa/alursatracker_edit.html', {'form': form})

@login_required
def Alursatracker_list(request):
        latest_tracker_list = AluRsaTracker.objects.order_by('-created_date')
        context = {
            'latest_tracker_list': latest_tracker_list,
       }
        return render(request, 'alursa/alursatracker_list1.html', context)

def AluExportRsaTracker(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RSATracker.csv"'

    writer = csv.writer(response)
    writer.writerow(['cascade','Technology','System Date','User Date','User Name','Assignee', 'BTS/OEM', 'Market', 'eNB', 'OSS', 'Source', 'Ageing','Site_Type', 'CSMS','Alarm Status','OAR_Date','OAC_Date','NIMS','ACD','TVW','PRTS','PATROL','TRAMPS','NEO','Initial Status','Final Status','Volte Soft Launch','Category','SV 3115','Owner','CICO','Remark'])

    latest_tracker_list1 = AluRsaTracker.objects.order_by('-created_date')
    for item in latest_tracker_list1:
        writer.writerow([item.cascade, item.Technology,item.created_date,item.Date,item.admin,item.Assignee, item.OEM, item.Market, item.eNB, item.OSS, item.Source, item.Ageing,item.Site_Type, item.CSMS,item.Alarm_Status,item.OAR_Date,item.OAC_Date,item.Nims,item.ACD,item.TVW,item.PRTS,item.Patrol,item.Trams,item.NEO,item.Initial_Status,item.Final_Status,item.Volte_Soft_Launch_Status,item.Category,item.SV_3115,item.Owner,item.CICO,item.Remark])

    return response

@login_required
def Alursasearch(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(cascade__icontains=query) | Q(User_Name__username__icontains=query)

            results = AluRsaTracker.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'alursa/alursasearch.html', context)

        else:
            return render(request, 'alursa/alursasearch.html')

    else:
        return render(request, 'alursa/alursasearch.html')

@login_required
def Alursatracker_edit(request, pk):
    tracker = get_object_or_404(AluRsaTracker, pk=pk)
    if request.method == "POST":
        form = AluRsaTrackerForm(request.POST)
#        form = TrackerForm(request.POST, instance=tracker)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.board = ALUCounts.objects.get(id=1)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('Alursatracker_list')
    else:
        form = AluRsaTrackerForm(instance=tracker)
    return render(request, 'alursa/alursatracker_edit.html', {'form': form})

@login_required
def Alursatracker_edit1(request, pk):
    tracker = get_object_or_404(AluRsaTracker, pk=pk)
    if request.method == "POST":
        form = AluRsaTrackerForm(request.POST, instance=tracker)
#        form = TrackerForm(request.POST)
        if form.is_valid():
            tracker = form.save(commit=False)
            tracker.admin = request.user
            tracker.board = ALUCounts.objects.get(id=1)
            tracker.created_date = timezone.now()
            tracker.save()
            return redirect('Alursatracker_list')
    else:
        form = AluRsaTrackerForm(instance=tracker)
    return render(request, 'alursa/alursatracker_edit.html', {'form': form})
