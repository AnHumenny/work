import os

from django.http import HttpResponse
from django.shortcuts import render
from base.settings import BASE_DIR



def start_filebrowser(request):

    return render(request, 'filewiever/index.html')

def file_dlink_gomel(request):
    directory = f'{BASE_DIR}/filewiever/files/gomel/dlink'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    context = {
        'files_dlink': files,
        'directory': directory,
    }
    return render(request, 'filewiever/all_list.html', context)

def file_ubiquity_gomel(request):
    directory = f'{BASE_DIR}/filewiever/files/gomel/ubiquity'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    context = {
        'files_ubiquity': files,
        'directory': directory,
    }
    return render(request, 'filewiever/all_list.html', context)

def file_client_gomel(request):
    directory = f'{BASE_DIR}/filewiever/files/gomel/client'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    context = {
        'files_client': files,
        'directory': directory,
    }
    return render(request, 'filewiever/all_list.html', context)

def file_railway_gomel(request):
    directory = f'{BASE_DIR}/filewiever/files/gomel/railway'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    context = {
        'files_railway': files,
        'directory': directory,
    }
    return render(request, 'filewiever/all_list.html', context)

def file_instruction_gomel(request):
    directory = f'{BASE_DIR}/filewiever/files/gomel/instruction'
    files = os.listdir(directory)
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
    context = {
        'files_instruction': files,
        'directory': directory,
    }
    return render(request, 'filewiever/all_list.html', context)


def file_download_dlink(request, file):
    directory = f'{BASE_DIR}/filewiever/files/gomel/dlink'  # Укажите путь к Вашей директории
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)

def file_download_ubiquity(request, file):
    directory = f'{BASE_DIR}/filewiever/files/gomel/ubiquity'  # Укажите путь к Вашей директории
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)

def file_download_client(request, file):
    directory = f'{BASE_DIR}/filewiever/files/gomel/client'  # Укажите путь к Вашей директории
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)


def file_download_railway(request, file):
    directory = f'{BASE_DIR}/filewiever/files/gomel/railway'  # Укажите путь к Вашей директории
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)

def file_download_instruction(request, file):
    directory = f'{BASE_DIR}/filewiever/files/gomel/instruction'  # Укажите путь к Вашей директории
    file_path = os.path.join(directory, file)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file}"'
            return response
    else:
        return HttpResponse("File not found", status=404)