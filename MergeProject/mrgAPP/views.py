from django.shortcuts import render

import os
from PyPDF2 import PdfMerger
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import PDFDocument

def home(request):
    # Fetch all uploaded documents
    documents = PDFDocument.objects.all()
    return render(request, 'mrgAPP/home.html', {'documents': documents})

def upload_pdf(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Save the file to the database
        document = PDFDocument.objects.create(name=file.name, file=file)
        document.save()
        return redirect('home')
    return render(request, 'mrgAPP/upload.html')
