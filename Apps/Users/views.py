from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods

from Apps.Users.utils import add_users_util, delete_user_util, get_users_util


@require_http_methods(['GET', 'POST'])
def add_users(request):
    if request.method == 'GET':
        user_list = get_users_util()
        return render(request, 'Users.html', {"user_list": user_list})
    else:
        user_id = request.POST.get('user_id')
        session_id = request.POST.get('session_id')
        status_code = 201 if add_users_util(user_id=user_id, session_id=session_id) else 400
        return render(request, 'OK.html', status=status_code)



@require_http_methods(['GET'])
def delete_user(request):
    user_id = request.GET.get('user_id')
    status_code = 201 if delete_user_util(user_id) else 400
    return render(request, 'OK.html', status=status_code)
