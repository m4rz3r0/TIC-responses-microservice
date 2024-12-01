# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.response_detail import ResponseDetail  # noqa: E501
from swagger_server.models.response_submission import ResponseSubmission  # noqa: E501
from swagger_server.test import BaseTestCase


class TestResponsesController(BaseTestCase):
    """ResponsesController integration test stubs"""

    def test_responses_id_get(self):
        """Test case for responses_id_get

        Obtener detalles de una respuesta
        """
        response = self.client.open(
            '/responses/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_responses_post(self):
        """Test case for responses_post

        Enviar respuestas a una encuesta
        """
        body = ResponseSubmission()
        response = self.client.open(
            '/responses',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
