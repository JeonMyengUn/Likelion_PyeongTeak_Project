from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Card


def home(request):
    return render(request, 'home.html')

def new(request):
    if request.user.is_authenticated:
        card = Card.objects
        return render(request, 'new.html', {'Card':card})
    else:
        return redirect('/accounts/signup/')

def create(request):
    card = Card.object.create()
    card.to = request.POST['to']
    card.From = request.POST['From']
    card.title = request.POST['title']
    card.content = request.POST['content']
    card.img = request.POST['img']
    card.pub_date = timezone.datetime.now()
    card.save()
    return redirect('/detail/'+ str(card.id))
    
def detail(request, card_id):
    details = get_object_or_404(Card, pk=card_id)
    return render(request, 'detail.html', {'details':details})
