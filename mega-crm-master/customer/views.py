from django.shortcuts import render
from main.models import Save
from crm.models import MessageModel, Chat, Announcement

# Create your views here.
def home(request):
    allann = Announcement.objects.all()
    saves = Save.objects.filter(user=request.user)
    context = {
        'title': "Customer Dashboard",
        'anns' : allann,
        'saves' : saves
        }
    return render(request, 'customer/index.html', context)

def profile(request):
    context = {'title': "My Profile"}
    return render(request, 'customer/profile.html', context)

def saved(request):
    saves = Save.objects.filter(user=request.user)
    
    context = {
        'title': "Saved Products",
        'saves' : saves
        }
    
    return render(request, 'customer/saved.html', context)

def viewtickets(request):
    tickets = MessageModel.objects.filter(by=request.user)
    context = {
        'title': "View Tickets",
        'tickets' : tickets
        }
    return render(request, 'customer/view-tickets.html', context)

def createticket(request):
    if request.method == 'GET':
        context = {
        'title': "Create a Ticket"
        }
        return render(request, 'customer/create-a-ticket.html', context)
    else:
        subject = request.POST['subject']
        type = request.POST['type']
        message = request.POST['message']
        mmodel = MessageModel.objects.create(desc=subject, type=type, by=request.user)
        mmodel.save()
        chat = Chat.objects.create(messagemodel=mmodel, message=message, sentby=request.user)
        mmodel.chats.add(chat)
        context = {
        'title': "Create a Ticket",
        'message' : 'Support ticket created'
        }
        return render(request, 'customer/create-a-ticket.html', context)

def viewannouncemts(request):
    announcements = Announcement.objects.all()
    context = {
        'title': "View Announcements",
        'announcements' : announcements
    }
    return render(request, 'customer/view-announcements.html', context)



