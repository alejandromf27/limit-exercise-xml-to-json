import xmltodict
from django.shortcuts import render
from xml_converter.forms import XmlFileForm

TEMPLATE_HTML = "upload_page.html"


def upload_page(request):
    if request.method == 'POST':
        form = XmlFileForm(request.POST, request.FILES)

        if not form.is_valid():
            context = {'form': form}
            return render(request, TEMPLATE_HTML, context)

        xml_file = request.FILES.get('file', None)
        try:
            obj = xmltodict.parse(xml_file.read())
        except BaseException:
            context = {'form': form, 'error': "Invalid XML"}
            return render(request, TEMPLATE_HTML, context)

        context = {'form': form, 'data': obj}
        return render(request, TEMPLATE_HTML, context)

    form = XmlFileForm()
    context = {'form': form}
    return render(request, TEMPLATE_HTML, context)
