from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.views.decorators.http import require_http_methods

from Apps.Jobs.utils import set_jobs_util, get_jobs_util, delete_job_util
from Apps.Users.utils import get_users_util
from global_utils import today


@require_http_methods(['GET'])
def jobs_render(request):
    page_num = int(request.GET.get('page_num', 1))
    page_size = int(request.GET.get('page_size', 10))
    item_list = get_jobs_util(page_num, page_size)
    user_list = get_users_util()

    return render(request, 'Jobs.html', {"item_list": item_list, "user_list": user_list})


@require_http_methods(['POST'])
def set_jobs(request):
    channel = request.POST.get("channel")
    account = request.POST.get("account")
    publish_freq = request.POST.get("publish_freq")
    publish_time = request.POST.get("publish_time") if publish_freq == 'Once' else '{} {}'.format(today(), request.POST.get("publish_time").split(' ')[-1])
    text = request.POST.get("text", "")
    file_amount = request.POST.get("file_amount", 1)
    status = 0
    status_code = 201 if set_jobs_util(channel, account, publish_time, publish_freq, text, file_amount, status) else 400
    return render(request, 'OK.html', status=status_code)


@require_http_methods(['GET'])
def delete_job(request):
    job_id = request.GET.get("job_id")
    status_code = 201 if delete_job_util(job_id) else 400
    return render(request, 'OK.html', status=status_code)