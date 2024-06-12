from django.shortcuts import render
from .forms import UploadFileForm
import ast

def is_valid_python(file_content):   
    try:
        ast.parse(file_content)
        return True
    except SyntaxError:
        return False

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_content = file.read().decode('utf-8')

            if is_valid_python(file_content):
                message = 'The uploaded file is a valid Python file.'
            else:
                message = 'The uploaded file is not a valid Python file.'
            return render(request, 'result.html', {'message': message})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
