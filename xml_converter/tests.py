import json
from pathlib import Path

from django.test import TestCase, Client

from xml_converter.forms import XmlFileForm

TEST_DIR = Path(__file__).parent / Path('test_files')
TEST_ADDRESS = {
    "Root": {
        "Address": [
            {
                "StreetLine1": "123 Main St.",
                "StreetLine2": "Suite 400",
                "City": "San Francisco",
                "State": "CA",
                "PostCode": "94103"
            },
            {
                "StreetLine1": "400 Market St.",
                "City": "San Francisco",
                "State": "CA",
                "PostCode": "94108"
            }
        ]
    }
}


class XMLConversionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_connected_convert_empty_document(self):
        with (TEST_DIR / Path('empty.xml')).open() as fp:
            response = self.client.post('/connected/', {
                'file': fp,
            })
            # Testing response status code
            self.assertEqual(response.status_code, 200)
            # Testing template rendered
            self.assertTemplateUsed(response, 'upload_page.html')
            # Testing form used
            form = response.context['form']
            self.assertIsInstance(form, XmlFileForm)
            # Testing data returned
            data = response.context['data']
            self.assertEqual(data, json.dumps({
                "Root": None,
            }, indent=2))

    def test_api_convert_empty_document(self):
        with (TEST_DIR / Path('empty.xml')).open() as fp:
            response = self.client.post('/api/converter/convert/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "Root": None,
            })

    def test_connected_convert_addresses(self):
        with (TEST_DIR / Path('addresses.xml')).open() as fp:
            response = self.client.post('/connected/', {
                'file': fp,
            })
            # Testing response status code
            self.assertEqual(response.status_code, 200)
            # Testing template rendered
            self.assertTemplateUsed(response, 'upload_page.html')
            # Testing form used
            form = response.context['form']
            self.assertIsInstance(form, XmlFileForm)
            # Testing data returned
            data = response.context['data']
            self.assertEqual(data, json.dumps(TEST_ADDRESS, indent=2))

    def test_api_convert_addresses(self):
        with (TEST_DIR / Path('addresses.xml')).open() as fp:
            response = self.client.post('/api/converter/convert/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, TEST_ADDRESS)
