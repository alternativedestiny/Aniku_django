import os
import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth
from .models import Movie, Animation

# 全局变量
movie_start = 0


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def user(request):
    """
    :param request
    """
    if request.user.is_authenticated:
        return render(request, 'user.html')
    else:
        return render(request, 'login.html', {'message': 'login'})


def movie(request):
    m0 = Movie.objects.order_by('id')[0]
    context = {'id': m0.id,
               'name_cn': m0.name_cn,
               'name_en': m0.name_en,
               'publish_y': m0.publish_y,
               'poster': m0.poster,
               'director': m0.director,
               'starring': m0.starring,
               'tags': m0.tags,
               'size': m0.size,
               'db_id': m0.db_id
               }
    return render(request, 'movie.html', context)


def login(request):
    return render(request, 'login.html', {'message': 'login'})


# 登陆检验函数
def login_check(request):
    username = request.POST.get("username", "")  # 获取用户名
    password = request.POST.get("password", "")  # 获取密码
    user_profile = auth.authenticate(
        request, username=username, password=password)
    if user_profile is not None:  # 判断用户信息是否存在
        auth.login(request, user_profile)  # 登陆
        return render(request, 'dashboard.html')
    else:  # 否则返回登陆页面，并提示错误信息
        return render(request, 'login.html', {"message": "账户密码错误，请重新输入！"})


def logout(request):
    auth.logout(request)
    return render(request, 'dashboard.html')


def open_file(request):
    file_path = r'D:\Project\地调avc\images\石港2019-01-01.png'
    os.startfile(file_path)
    context = {'message': '文件已打开'}
    return JsonResponse(context)


def open_folder(request):
    path = r'D:\Project\地调avc\images'
    os.system("explorer.exe %s" % path)
    context = {'message': '文件已打开'}
    return JsonResponse(context)


def get_info(request):
    # api: http://www.daicuo.vip/api/douban
    context = {'message': 'error'}
    if request.method == 'POST':
        m_id = request.POST.get("id", "")
        db_id = request.POST.get("db_id", "")
        url = 'http://api.daicuo.cc/douban/?key=4358180e94223d3f&id=' + db_id
        result = requests.get(url)
        if result.status_code == 200:
            r = json.loads(result.text)
            m = Movie.objects.get(id=m_id)
            m.name_cn = r['data']['vod_name']
            m.name_en = r['data']['vod_title']
            m.director = r['data']['vod_director']
            m.publish_y = int(r['data']['vod_filmtime'][0:4])
            m.starring = r['data']['vod_actor']
            m.tags = r['data']['vod_type']
            m.poster = r['data']['vod_pic']
            m.save()
            # print(r['data']['vod_name'])
            # print(r['data']['vod_filmtime'])
            context = {'message': 'get info'}
    return JsonResponse(context)


def movie_list(request):
    number = 20
    if Movie.objects.count() < movie_start * 20:
        number = Movie.objects.count() - movie_start * 20
    for i in range(number):

    context = {'message': Movie.objects.count()}
    return JsonResponse(context)
