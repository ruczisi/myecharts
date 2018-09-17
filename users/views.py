from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from users import models

# Create your views here.

def userprofile(request,pk):
    if pk == None:
        return HttpResponseRedirect('/users/login')
    else:
        user = get_object_or_404(models.Users,pk=pk)
        context = dict(
            profile = user
        )
    return render(request,'registration/profile.html',context=context)