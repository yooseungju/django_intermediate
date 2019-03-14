from django.shortcuts import render, redirect
from .models import Board


# Create your views here.
def index(request):
    # pprint(request)
    # pprint(type(request))
    # pprint(dir(request))
    # pprint(request.scheme)
    # pprint(request.get_host())
    # pprint(request.get_full_path())
    # pprint(request.build_absolute_uri())
    # pprint(request.META)
    # pprint(request.method)
    
    boards = Board.objects.order_by('-pk')
    context = {
        'boards' : boards,
    }
    return render(request, 'boards/index.html', context)
    
    
def new(request):
    # create 동작일때
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title= title, content=content)
        board.save()
        return redirect('boards:detail', pk=board.id)
    #new 일때
    else:
        return render(request, 'boards/new.html')
    
def detail(request, pk):
    board = Board.objects.get(pk=pk)
    content = {
        'board' : board
    }
    return render(request, 'boards/detail.html', content)
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    else: 
        return redirect('boards:detail', board.pk)
    
def edit(request, pk):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board.objects.get(pk=pk)
        board.title = title
        board.content = content
        board.save()
        return redirect('boards:detail', board.id)
    else:
        board = Board.objects.get(pk = pk)
        context ={
            'board' : board ,
        }
        return render(request, 'boards/edit.html', context)
    

    
    