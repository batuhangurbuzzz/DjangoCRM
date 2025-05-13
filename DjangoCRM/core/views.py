from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logoutUser(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')


def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


def customerRecord(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customerRec = Record.objects.get(id=pk)
        
        return render(request, 'record.html', {'customerRec':customerRec})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
def deleteRecord(request, pk):
    if request.user.is_authenticated:
        delete = Record.objects.get(id=pk)
        delete.delete()
        messages.success(request, "Records Deleted Successfully!")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
def addRecord(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                addRecords = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
    
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    
    
def updateRecord(request, pk):
    if request.user.is_authenticated:
        currentRecord = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=currentRecord)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated...")
            return redirect('home')
        return render(request, 'updated_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
            
         