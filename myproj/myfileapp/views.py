from django.shortcuts import render, HttpResponse
from django.core.files import File
from .forms import MyfileUploadForm
from .models import file_upload

def index(request):
    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)
        print(form.as_p)
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']
            file_upload(file_name=name, my_file=the_files).save()
            return HttpResponse("file upload")
        else:
            return HttpResponse('error')
    else:
        context = {
            'form':MyfileUploadForm()
        }      
        return render(request, 'index.html', context)
        

def show_file(request):
    # this for testing 
    all_data = file_upload.objects.all()

    context = {
        'data': all_data
        }
    return render(request, 'view.html', context)


def session(request):
    #for showing question and text field
    fileLocation = 'C:/Users/USER/Documents/abir_reza/myproj/media/'
    if request.method == 'POST':
        test = request.POST.getlist('ans')
        print(len(test))
        f = open("temp.txt", "w")
        for i in range (0,len(test)):
            if test[i] == "":
                f.write("n/a")
            f.write(test[i])
            f.write("\n")
        f.close()
    f = open(fileLocation+'Standard_CN_Question.txt', 'r')
    if f.mode == 'r':
       contents =f.read()
       f.close()
       contents = contents.split('\n')
       print (contents)
    if request.method == 'POST':
        form = MyfileUploadForm(request.POST, request.FILES)
        print(form.as_p)
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']
            file_upload(file_name=name, my_file=the_files).save()
            return HttpResponse("file upload")
    else:
        context = {
            'form':MyfileUploadForm(),
            'data' : contents
        }      
        return render(request, 'examsession.html', context)

    