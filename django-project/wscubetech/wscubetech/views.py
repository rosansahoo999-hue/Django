from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm

def homePage(request):
    data = {
        'title': 'Home New',
        'bdata': 'WelCome to WsCubeTech',
        'clist': ['PHP', 'Java', 'Django'],
        'numbers': [10, 20, 30, 40, 50],
        'student_details': [
            {'name': 'rosan', 'phone': 9309520974},
            {'name': 'ritu', 'phone': 8328905591}
        ]
    }
    return render(request, "index.html", data)

def submitform(request):
    finalans = 0
    fn=usersForm()

    data = {'form': fn}
    try:
            if request.method=="POST":
            # n1 = int(request.POST['num1'])
            # n2 = int(request.POST['num2'])
                n1 = int(request.POST.get("num1"))
                n2 = int(request.POST.get("num2"))
                n3 = int(request.POST.get("num3"))
                # print(n1+n2);
                finalans=n1+n2+n3
                data = {
                    # "n1": n1,
                    # "n2": n2,
                    "form": fn,
                    "output": finalans,
                }


                return HttpResponse(finalans)
    except:
        pass


def aboutUs(request):
    if request.method=="GET":
        output=request.GET.get('output')
    # return HttpResponse("<b>Welcome To WsCubeTech</b>")
    return render(request,"about.html",{'output':output})

def course(request):
    return render(request, "course.html")

def courseDetails(request, courseid):
    return HttpResponse(courseid)

def calculator(request):
    return render(request, 'calculator.html')

def contactDetails(request):
    return render(request, 'contact.html')

def calculator(request):
    c = ''
    try:
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == '+':
                c = n1 + n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '*':
                c = n1 * n2
            elif opr == '/':
                c = n1 / n2
    except:
        c = ('invalid opr....')
        
    return render(request, 'calculator.html', {'c': c})

def evenodd(request):
    c = ''
    if request.method=='POST':
        n = eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"
    return render(request, 'evenodd.html', {'c': c})

def userForm(request):
    finalans = 0
    try:
        if request.method=="GET":
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
            n1 = int(request.GET.get("num1"))
            n2 = int(request.GET.get("num2"))
            # print(n1+n2);
            finalans=n1+n2
    except:
        pass
    return render(request, "userform.html", {"output": finalans})

def userForm_post(request):
    finalans = 0
    fn=usersForm()

    data = {'form':fn}
    try:
        if request.method=="POST":
        # n1 = int(request.POST['num1'])
        # n2 = int(request.POST['num2'])
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            n3 = int(request.POST.get("num3"))
            # print(n1+n2);
            finalans=n1+n2+n3
            data = {
                # "n1": n1,
                # "n2": n2,
                'form': fn,
                "output": finalans,
            }
            url="/about-us/?output={}".format(finalans)

            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass
    return render(request, "userform2.html", data)