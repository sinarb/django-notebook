from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import AddNoteFrom
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home_config(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user).order_by('-created')
        paginator = Paginator(notes, 3)
        page_number = request.GET.get('page')
        objects_list = paginator.get_page(page_number)
        return render(request, 'home/home.html', {'notes': objects_list, 'do': 'افزودن'})
    else:
        return redirect('account:login')


def detail(request, user_id):
    if request.user.is_authenticated:
        # todo = Note.objects.get(id=id,user=request.user)
        note = get_object_or_404(Note,id=user_id, user=request.user)
        return render(request, 'home/details.html', {'note': note})
    else:
        return redirect('account:login')


def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddNoteFrom(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                Note.objects.create(title=cd['title'], body=cd['body'],user=request.user)
                messages.success(request, 'یادداشت با موفقیت ثبت شد', extra_tags='success')
                return redirect("home:main")
        else:
            form = AddNoteFrom()
        return render(request, 'home/addnote.html', {'form': form, 'do': 'افزودن'})
    else:
        return redirect('account:login')


def edit(request, user_id):
    if request.user.is_authenticated:
        # note = Note.objects.get(id=user_id)
        note = get_object_or_404(Note, id=user_id, user=request.user)
        if request.method == 'POST':
            form = AddNoteFrom(instance=note, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'یادداشت با موفقیت ویرایش شد', extra_tags='success')
                return redirect("home:main")
        else:
            form = AddNoteFrom(instance=note)
        return render(request, 'home/addnote.html', {'form': form, 'do': 'ویرایش'})
    else:
        return redirect('account:login')


def search(request):
    if request.user.is_authenticated:
        q = request.GET.get('q')
        notes = Note.objects.filter(title__icontains=q, user=request.user).order_by('-created')
        page_number = request.GET.get('page')
        paginator = Paginator(notes, 3)
        objects_list = paginator.get_page(page_number)
        return render(request, 'home/home.html', {'notes': objects_list, 'q': q, 'do': 'افزودن'})
    else:
        return redirect('account:login')


def delete(request, user_id):
    if request.user.is_authenticated:
        note = Note.objects.get(id=user_id,user=request.user)
        note.delete()
        messages.success(request, 'یادداشت با موفقیت حذف شد', extra_tags='success')
        return redirect('home:main')
    else:
        return redirect('account:login')
