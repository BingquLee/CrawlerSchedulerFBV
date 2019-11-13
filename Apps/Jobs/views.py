from django.http import JsonResponse
from django.shortcuts import render
import time


# Create your views here.
from django.views.decorators.http import require_http_methods

from Apps.Jobs.utils import set_jobs_util, get_jobs_util, delete_job_util, get_accounts_util

from global_utils import today, date_min2ts, ts2date_min


@require_http_methods(['GET'])
def jobs_render(request):
    return render(request, 'index.html')


@require_http_methods(['GET'])
def get_accounts_list(request):
    channel = request.GET.get("channel", "Tiktok")
    accounts_list = get_accounts_util(channel)
    return JsonResponse(accounts_list, safe=False)


@require_http_methods(['POST'])
def set_jobs(request):
    channel = request.POST.get("channel")
    account = request.POST.get("account")
    publish_freq = request.POST.get("publish_freq")
    publish_time = request.POST.get("publish_time")
    if publish_freq == 'Once':
        publish_time = publish_time
    else:
        if '-' not in publish_time:
            publish_time = today() + ' ' + publish_time
        else:
            publish_time = publish_time
        publish_ts = date_min2ts(publish_time)
        if publish_ts <= int(time.time()):
            publish_ts += 24 * 60 * 60
        else:
            publish_ts = publish_ts
        publish_time = ts2date_min(publish_ts)
    text = request.POST.get("text", "")
    file_amount = request.POST.get("file_amount", 1)
    status = 0
    status_code = 201 if set_jobs_util(channel, account, publish_time, publish_freq, text, file_amount, status) else 400
    return render(request, 'OK.html', status=status_code)


@require_http_methods(['GET'])
def get_jobs(request):
    channel = request.GET.get("channel", "Tiktok")
    item_list = get_jobs_util(channel)
    print(item_list)
    return JsonResponse(item_list, safe=False)


@require_http_methods(['GET'])
def delete_job(request):
    job_id = request.GET.get("job_id")
    status_code = 201 if delete_job_util(job_id) else 400
    return render(request, 'OK.html', status=status_code)
