from _include.Hydra.Hydra.form.image.form_blob_image_upload import BlobImageUploadForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context
import urllib2
import urllib


def blob_image_upload(request):
    if request.method == 'POST':
        form = BlobImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with open(form.file) as image:
                    response = urllib2.urlopen('http://api.mealsloth.com/blob-image-upload/',
                                               urllib.urlencode({'file': image}))
                    result = response.read()
                    print(result)
                    return HttpResponseRedirect('/tools')
            except IOError:
                return HttpResponseRedirect('/users')
        else:
            return HttpResponse("Invalid form")
    else:
        return render(request, 'page/tool/blob-image-upload.html', Context({'form': BlobImageUploadForm()}))