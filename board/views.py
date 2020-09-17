from django.shortcuts import render
from .models import Board


def board_list(request):
    # -id -> id 역순
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})