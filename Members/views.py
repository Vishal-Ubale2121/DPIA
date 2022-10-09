from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Assessment.models import Master
import json
import os


def login_user(request):
    if request.method == 'POST':
        request.session['username'] = request.POST.get('username')
        password = request.POST.get('password')
        username = request.session.get('username')
        user = authenticate(request, username=username, password=password)
        db_instance = Master.objects.all()
        instance_list = []
        single_list = []
        for instance in db_instance:
            instance_list.append(instance.__dict__)
        for item in instance_list:
            single_list.append(item)
        dict_count = 1
        session_dict = {}
        display_list = ['DPIA1', 'DPIA2']
        for items in db_instance:
            session_dict['session_dict_{}'.format(dict_count)] = items.__dict__
            session_dict.get('session_dict_{}'.format(dict_count))['_state'] = \
                str(session_dict.get('session_dict_{}'.format(dict_count))['_state'])
            session_dict.get('session_dict_{}'.format(dict_count))['date'] = \
                session_dict.get('session_dict_{}'.format(dict_count))['date'].strftime("%d %B %Y")
            dict_count += 1
        if user is not None:
            login(request, user)
            num = 1
            display_name = {}
            context = {'authorised': True,
                       'display_list': display_list,
                       'db_range': range(1, 3),
                       'db_instance': len(db_instance),
                       'session_dict': session_dict}
            for i in session_dict:
                context['session_dict_{}'.format(num)] = session_dict.get('session_dict_{}'.format(num))
                context['title{}'.format(num)] = session_dict.get('session_dict_{}'.format(num)).get('title')
                context['date{}'.format(num)] = session_dict.get('session_dict_{}'.format(num)).get('date')
                context['status{}'.format(num)] = session_dict.get('session_dict_{}'.format(num)).get('status')
                context['role{}'.format(num)] = session_dict.get('session_dict_{}'.format(num)).get('role')
                context['display_data'] = display_name
                num += 1
            return render(request, 'session_screen.html', context)
        else:
            context = {
                'text': 'Invalid Username or Password'
            }
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login.html', context)

    if request.user.is_authenticated:
        db_instance = Master.objects.all()
        instance_list = []
        single_list = []
        for instance in db_instance:
            instance_list.append(instance.__dict__)
        for item in instance_list:
            single_list.append(item)
        dict_count = 1
        session_dict = {}
        display_list = ['DPIA1', 'DPIA2']
        for items in db_instance:
            session_dict['session_dict_{}'.format(dict_count)] = items.__dict__
            session_dict.get('session_dict_{}'.format(dict_count))['_state'] = \
                str(session_dict.get('session_dict_{}'.format(dict_count))['_state'])
            session_dict.get('session_dict_{}'.format(dict_count))['date'] = \
                session_dict.get('session_dict_{}'.format(dict_count))['date'].strftime("%d %B %Y")
            dict_count += 1
        num = 1
        display_name = {}
        context = {'authorised': True,
                   'display_list': display_list,
                   'db_range': range(1, 3),
                   'db_instance': len(db_instance),
                   'session_dict': session_dict}
        for i in session_dict:
            context['session_dict_{}'.format(num)] = session_dict.get('session_dict_{}'.format(num))
            context['title{}'.format(num)] = session_dict.get('session_dict_{}'.format(num)).get('title')
            context['date{}'.format(num)] = session_dict.get('session_dict_{}'.format(num)).get('date')
            context['status{}'.format(num)] = session_dict.get('session_dict_{}'.format(num)).get('status')
            context['role{}'.format(num)] = session_dict.get('session_dict_{}'.format(num)).get('role')
            context['display_data'] = display_name
            num += 1
        return render(request, 'session_screen.html', context)
    else:
        return render(request, 'login.html')


@login_required
def logout_user(request):
    logout(request)
    return render(request, 'logout.html')






