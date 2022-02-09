from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, DoneTodo
from django.shortcuts import redirect

def todoView(request):
    all_todo_items = TodoItem.objects.all()

    return render(request, 'todo.html', {'all_items': all_todo_items, 'error': ''})

def addTodo(request):
    content = request.POST['content']
    if not content.strip():
        all_todo_items = TodoItem.objects.all()
        return render(request, 'todo.html', {'all_items': all_todo_items, 'error': 'Please enter valid todo item'})
    new_todo_item = TodoItem(content=request.POST['content'])
    new_todo_item.save()
    return redirect('/todo/')

def deleteTodo(request, todo_id):

    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return redirect('/todo/')

def editTodo(request, todo_id):
    old_todo_item = TodoItem.objects.get(id=todo_id)
    print (old_todo_item)
    print (type(old_todo_item))
    old_todo_item.content = request.POST['content']
    old_todo_item.save()
    return redirect('/todo/')


def doneTodo(request, todo_id):
    done_toto_item = TodoItem.objects.get(id=todo_id)
    done_todo_item = DoneTodo(content=done_toto_item.content)
    done_todo_item.save()
    deleteTodo(request, todo_id)
    return redirect('/todo/')

def doneTasks(request):
    doneTodoItems = DoneTodo.objects.all()
    return render(request, 'todo.html', {'all_items': doneTodoItems})