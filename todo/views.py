from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Todo
from .forms import ToDoForm, CustomUserCreationForm
from .serializers import TodoSerializer

@method_decorator(csrf_exempt, name='dispatch')
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'تم إنشاء الحساب بنجاح!')
            return redirect('task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح!')
            return redirect('task_list')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')
    return render(request, 'todo/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح!')
    return redirect('login')

@login_required
def task_list(request):
    tasks = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'تم إضافة المهمة بنجاح!')
            return redirect('task_list')
    else:
        form = ToDoForm()
    return render(request, 'todo/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث المهمة بنجاح!')
            return redirect('task_list')
    else:
        form = ToDoForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Todo, pk=pk, user=request.user)
    task.delete()
    messages.success(request, 'تم حذف المهمة بنجاح!')
    return redirect('task_list')

@login_required
def task_toggle(request, pk):
    task = get_object_or_404(Todo, pk=pk, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task_list')
 