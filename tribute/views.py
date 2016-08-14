from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Game, Card
from .forms import GameForm

def game_list(request):
    games = Game.objects.filter(created__lte=timezone.now()).order_by('-last_edit')
    return render(request, 'tribute/game_list.html', {'games': games})

def game_play(request, pk):
    post = get_object_or_404(Game, pk=pk)
    return render(request, 'tribute/game_play.html', {'post': post})

def game_new(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.created = timezone.now()
            game.save()
            return redirect('tribute.views.game_play', pk=game.pk)
    else:
        form = GameForm()
    return render(request, 'tribute/game_edit.html', {'form': form})

def game_edit(request, pk):
    game = get_object_or_404(Game, pk=pk)
    print("Editing game. pk = " + pk)
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save(commit=False)
            game.last_edit = timezone.now()
            game.save()
            return redirect('tribute.views.game_play', pk=game.pk)
    else:
        form = GameForm(instance=game)
    return render(request, 'tribute/game_edit.html', {'form': form})