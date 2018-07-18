from django.shortcuts import render
from django.http import *
from django.shortcuts import *
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import auth
from django.core.mail import send_mail
# Create your views here.


def blog(request):
     if request.method=='POST':
        form1=subscribe(request.POST)
        if form1.is_valid():
            cd=form1.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form1.save()
            return HttpResponseRedirect('/blog/')
     else:
         form1=subscribe()
         return render(request,'blog.html',{'form':form1})
        
     if request.method=='POST':
        form=Comment_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data['text'])
            f=form.save(commit=False)
            f.created_by=request.user
            f.save()
            return redirect('/blog/')
     else:
        form=Comment_form()
        data=Comment.objects.all()
        nested_data=Nested_Comment.objects.all()
        #print(data)
     return render(request,'blog.html',{'data':data,'nested':nested_data})

def nested_comment(request):
    form = Nested_Comment_form(request.POST)
    comment_id=request.POST['comment']
    cmt=Comment.objects.get(id=comment_id)
    print(cmt)
    if form.is_valid():
        f=form.save(commit=False)
        f.created_by=request.user
        f.comment=cmt
        f.save()
        return redirect('/blog/')
    
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/blog/')
    else:
        form=subscribe()
    return render(request,'blog.html',{'form':form})

def about(request):
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/about/')
    else:
        form=subscribe()
    return render(request,'about.html',{'form':form})

def contact(request):
    if request.method=='POST':
        form=con_form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU FOR CONTACTING US ...!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['cemail']])
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=con_form()
        return render(request,'contact.html',{'form':form})

    if request.method=='POST':
        form1=subscribe(request.POST)
        if form1.is_valid():
            cd=form1.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU FOR SUBSCRIBING US ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form1.save()
            return HttpResponseRedirect('/')
    else:
        form1=subscribe()
    return render(request,'contact.html',{'form':form1})  
      
def index(request):
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=subscribe()
    return render(request,'index-2.html',{'form':form})

def team(request):
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/team/')
    else:
        form=subscribe()
    return render(request,'team.html',{'form':form})
    

def causes(request):
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/causes-grid/')
    else:
        form=subscribe()
    return render(request,'causes-grid.html',{'form':form})

def donate(request):
     if request.method=='POST':
          form=donate_form(request.POST)
          if form.is_valid():
               cd=form.cleaned_data
               subject='UMANG NGO'
               msg='THANKYOU WE WILL PROCESS YOU REQUEST ...!'
               send_mail(subject,msg,'umangforlife@gmail.com',[cd['demail']])
               form.save()
               return HttpResponseRedirect('/donate/')
     else:
          form=donate_form()
          return render(request,'donate.html',{'form':form})

     if request.method=='POST':
          form1=subscribe(request.POST)
          if form1.is_valid():
               cd=form1.cleaned_data
               subject='UMANG NGO'
               msg='THANKYOU FOR SUBSCRIBING US ..!!'
               send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
               form1.save()
               return HttpResponseRedirect('/')
     else:
          form1=subscribe()
     return render(request,'donate.html',{'form':form1})

def events(request):
    all_product=event.objects.all()
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/events-grid/')
    else:
        form=subscribe()
    return render(request,'events-grid.html',{'form':form,'pro':all_product})

def login(request):
     
     if request.method=='POST':
          form=subscribe(request.POST)
          if form.is_valid():
               cd=form.cleaned_data
               subject='UMANG NGO'
               msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
               send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
               form.save()
               return HttpResponseRedirect('/login/')
     else:
          form=subscribe()
     return render(request,'login.html',{'form':form})

def auth_user(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,
                           password=password)
    if user is not None:
        auth.login(request,user)
        
        return HttpResponseRedirect('/blog/')
    else:
        return HttpResponseRedirect('/Invalid/')

def sign(request):
     if request.method=='POST':
          form=reg_form(request.POST)
          if form.is_valid():
               cd=form.cleaned_data
               User.objects.create_user(username=cd['username'],
                                     semail=cd['semail'],
                                     password=cd['password'])
               # form.save()
               return HttpResponseRedirect('/login/')
     else:
          form=reg_form()
          return render(request,'sign.html',{'form':form})
              
     if request.method=='POST':
          form1=subscribe(request.POST)
          if form1.is_valid():
               cd=form1.cleaned_data
               subject='UMANG NGO'
               msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
               send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
               form1.save()
               return HttpResponseRedirect('/sign/')
     else:
          form1=subscribe()
     return render(request,'sign.html',{'form':form1})
             
  

    


def children(request):
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/children/')
    else:
        form=subscribe()
    return render(request,'Children.html',{'form':form})
  

def oldage(request):
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/oldage/')
    else:
        form=subscribe()
    return render(request,'Old-AgeHomes.html',{'form':form})

def widow(request):
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/widow/')
    else:
        form=subscribe()
    return render(request,'WidowWomen.html',{'form':form})
    

def animals(request):
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/animals/')
    else:
        form=subscribe()
    return render(request,'Animals.html',{'form':form})

def feedback(request):
    
    if request.method=='POST':
        form=feed_form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU FOR YOUR FEEDBACK !!'
            send_mail(subject,msg,'UMANG',[cd['femail']])
            form.save()
            return HttpResponseRedirect('/feedback/')
    else:
        form=feed_form()
        return render(request,'feedback.html',{'form':form})
    
    if request.method=='POST':
        form1=subscribe(request.POST)
        if form1.is_valid():
            cd=form1.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU FOR SUBSCRIBING US ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form1.save()
            return HttpResponseRedirect('/feedback/')
    else:
        form1=subscribe()
    return render(request,'feedback.html',{'form':form1})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def single_event(request):    
    all_product=event.objects.all() 
    return render(request,'events-grid.html',{          
                                       'pro':all_product
                                       })



def search(request):
    
    if request.method=='POST':
        form=subscribe(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='UMANG NGO'
            msg='THANKYOU TO SUBSCRIBE YOUR EMAIL ..!!'
            send_mail(subject,msg,'umangforlife@gmail.com',[cd['email']])
            form.save()
            return HttpResponseRedirect('/search/')
    else:
        form=subscribe()
        return render(request,'search.html',{'form':form})
    
    if request.method=='POST':
        s=request.POST.get('search')
        s=event.objects.filter(event_name__icontains=s)
        if s:
            return render(request,'search.html',{'q':s})
        else:
            return render(request,'search.html',{'msg':'Not found'})

        


