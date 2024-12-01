# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.response_submission_answers import ResponseSubmissionAnswers  # noqa: F401,E501
from swagger_server import util


class ResponseDetail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, survey_id: int=None, user_id: int=None, answers: List[ResponseSubmissionAnswers]=None):  # noqa: E501
        """ResponseDetail - a model defined in Swagger

        :param id: The id of this ResponseDetail.  # noqa: E501
        :type id: int
        :param survey_id: The survey_id of this ResponseDetail.  # noqa: E501
        :type survey_id: int
        :param user_id: The user_id of this ResponseDetail.  # noqa: E501
        :type user_id: int
        :param answers: The answers of this ResponseDetail.  # noqa: E501
        :type answers: List[ResponseSubmissionAnswers]
        """
        self.swagger_types = {
            'id': int,
            'survey_id': int,
            'user_id': int,
            'answers': List[ResponseSubmissionAnswers]
        }

        self.attribute_map = {
            'id': 'id',
            'survey_id': 'survey_id',
            'user_id': 'user_id',
            'answers': 'answers'
        }
        self._id = id
        self._survey_id = survey_id
        self._user_id = user_id
        self._answers = answers

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseDetail':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseDetail of this ResponseDetail.  # noqa: E501
        :rtype: ResponseDetail
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this ResponseDetail.


        :return: The id of this ResponseDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ResponseDetail.


        :param id: The id of this ResponseDetail.
        :type id: int
        """

        self._id = id

    @property
    def survey_id(self) -> int:
        """Gets the survey_id of this ResponseDetail.


        :return: The survey_id of this ResponseDetail.
        :rtype: int
        """
        return self._survey_id

    @survey_id.setter
    def survey_id(self, survey_id: int):
        """Sets the survey_id of this ResponseDetail.


        :param survey_id: The survey_id of this ResponseDetail.
        :type survey_id: int
        """

        self._survey_id = survey_id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this ResponseDetail.


        :return: The user_id of this ResponseDetail.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this ResponseDetail.


        :param user_id: The user_id of this ResponseDetail.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def answers(self) -> List[ResponseSubmissionAnswers]:
        """Gets the answers of this ResponseDetail.


        :return: The answers of this ResponseDetail.
        :rtype: List[ResponseSubmissionAnswers]
        """
        return self._answers

    @answers.setter
    def answers(self, answers: List[ResponseSubmissionAnswers]):
        """Sets the answers of this ResponseDetail.


        :param answers: The answers of this ResponseDetail.
        :type answers: List[ResponseSubmissionAnswers]
        """

        self._answers = answers
