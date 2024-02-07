from django.http import HttpRequest ,HttpResponseRedirect,HttpResponseServerError
from django.shortcuts import render,redirect
from .forms import user
from service.models import Contact
from service.forms import ContactForm
from service.models import dynamicService
from news.models import News
from django.contrib import messages

def your_view(request):
    # Replace this with your actual code to fetch or generate data
    servicesdata = dynamicService.objects.all()

    # Debugging message
    messages.info(request, f"Debug: {servicesdata}")

    return render(request, 'about.html', {'servicesdata': servicesdata})

def user(request):
     finalans = 0
     form = user()
     data = {"form ": form}
     try :
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])
        finalans = n1+n2
        data= {
            'form': fon,
            'output': finalans
        }
       
        url = "/about-us?output{}".format(finalans)
        return redirect(url)
     except:
        pass

def home(request):
    servicesdata = dynamicService.objects.all().order_by()
    newsdata = News.objects.all().order_by()

    data ={
        'servicesdata':servicesdata,
        'newsdata':newsdata
    }
    return render(request,"index.html",data)

def newsdetails(request,slug):
    newsdetails = News.objects.get(News_slug=slug)
    data = {
        'newsdetails':newsdetails
    }
    return render(request,"newsdetails.html",data)


def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def submitform(request):
    try :
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])
        finalans = n1+n2
        data={
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
       
        url = "/about-us?output{}".format(finalans)
        return redirect(url)
    except:
        pass
def service(request):
    servicesdata = dynamicService.objects.all().order_by('id')
    data ={
        'servicesdata':servicesdata
    }
    return render(request,"service.html",data)

def about(request):
    output = None
    if request.method == "GET":
            output = request.GET.get(output)
    return render(request,"about.html",{"output" : output})

def error(request):
    output = None
    if request.method == "GET":
        output = request.GET.get(output)
    return render(request,"404.html",{"output" : output})

def forms(request):
    finalans=0
    data={}
    try :
        n1 = int(request.POST['num1'])
        n2 = int(request.POST['num2'])
        finalans = n1+n2
        data={
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
       
        url = "about-us/?output{}".format(finalans)
        # return HttpResponseRedirect('about-us/')
        return redirect('about-us/')

    except:
        pass    

    return render(request,"forms.html",data)


def marksheet(request):
    if request.method == 'post':
        if request.POST.get('sybject1')=="":
            return render(request,"marksheet.html",{'error':true})
        s1 = eval(request.POST.get("subject1"))
        s2 = eval(request.POST.get("subject2"))
        s3 = eval(request.POST.get("subject3"))
        s4 = eval(request.POST.get("subject4"))
        s5 = eval(request.POST.get("subject5"))
        t = s1+ s2+s3+s4+s5 
        p = t*100/500
        data = {
            'total': t,
            'percentage': p
        }
        return render(request,"marksheet.html",data)
    return render(request, "marksheet.html")

def getcontact(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('index.html') # Replace 'cycle.html' with your success template
        else:
            form = ContactForm()

        # Render the 'contact.html' template with the form and its errors
        return render(request, 'contact.html', {'form': form})

    except Exception as e:
        # Include an error message in case of unexpected errors
        return HttpResponseServerError(f"Unexpected error: {e}")
    


def datafinding(request):
    servicedata = dynamicService.objects.all()
    if request.method =='GET':
            st = request.GET.get("servicename")
            if st!=None:
                servicedata = dynamicService.objects.filter(service_name__icontains = st)
                data ={
                    'servicedata' : servicedata
                 }   
    return render(request,'index.html',data) 



def custom_404_view(request: HttpRequest, exception: Exception = None):
    return render(request, '404.html', status=404)

