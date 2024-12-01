import connexion
import six

from swagger_server.models.response_detail import ResponseDetail  # noqa: E501
from swagger_server.models.response_submission import ResponseSubmission  # noqa: E501
from swagger_server import util


def responses_id_get(id):  # noqa: E501
    """Obtener detalles de una respuesta

    Permite consultar una respuesta enviada anteriormente. # noqa: E501

    :param id: ID de la respuesta
    :type id: int

    :rtype: ResponseDetail
    """
    return 'do some magic!'


def responses_post(body):  # noqa: E501
    """Enviar respuestas a una encuesta

    Permite a los usuarios enviar sus respuestas a una encuesta específica. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResponseSubmission.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
