import xmltodict
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request):
        xml_file = request.data.get('file', None)
        try:
            obj = xmltodict.parse(xml_file.read())
        except BaseException:
            raise ValidationError({"error": "Invalid XML."})
        return Response(obj)
