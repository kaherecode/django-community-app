from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'members/index.html')


def member_view(request, member_id):
    return render(request, 'members/member_view.html', locals())
