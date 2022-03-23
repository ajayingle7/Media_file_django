from django.shortcuts import render
from .models import Naukari
# Create your views here.



def naukariView(request):
    template_file = "app1/naukari.html"
    context = {}

    if request.method =="POST":
        eid = request.POST.get("eid")
        ename = request.POST.get("ename")
        resume = request.POST.get("resume")

        obj = Naukari(eid=eid, ename=ename, resume=resume)
        obj.save()



    return render(request,template_file,context)



def getImage(request):
    template_name = "app1/getimage.html"
    obj = Naukari.objects.all()
    context= {"data":obj}



    return render(request,template_name,context)

