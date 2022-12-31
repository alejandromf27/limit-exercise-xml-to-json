import json

import xmltodict
from django.shortcuts import render
from xml_converter.forms import XmlFileForm

TEMPLATE_HTML = "upload_page.html"


def upload_page(request):
    if request.method == 'POST':
        # Creating form
        form = XmlFileForm(request.POST, request.FILES)

        if not form.is_valid():
            context = {'form': form, 'error': "Invalid form"}
            return render(request, TEMPLATE_HTML, context)

        # Converting xml to dict and handling exceptions
        xml_file = request.FILES.get('file', None)
        try:
            obj = xmltodict.parse(xml_file.read())
        except BaseException:
            context = {'form': form, 'error': "Invalid XML"}
            return render(request, TEMPLATE_HTML, context)

        # Rendering template and the json formatted
        context = {'form': form, 'data': json.dumps(obj, indent=2)}
        return render(request, TEMPLATE_HTML, context)

    # Rendering empty form
    form = XmlFileForm()
    context = {'form': form}
    return render(request, TEMPLATE_HTML, context)
