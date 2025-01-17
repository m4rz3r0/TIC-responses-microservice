# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResponseSubmissionAnswers(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, question_id: int=None, answer: str=None):  # noqa: E501
        """ResponseSubmissionAnswers - a model defined in Swagger

        :param question_id: The question_id of this ResponseSubmissionAnswers.  # noqa: E501
        :type question_id: int
        :param answer: The answer of this ResponseSubmissionAnswers.  # noqa: E501
        :type answer: str
        """
        self.swagger_types = {
            'question_id': int,
            'answer': str
        }

        self.attribute_map = {
            'question_id': 'question_id',
            'answer': 'answer'
        }
        self._question_id = question_id
        self._answer = answer

    @classmethod
    def from_dict(cls, dikt) -> 'ResponseSubmissionAnswers':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResponseSubmission_answers of this ResponseSubmissionAnswers.  # noqa: E501
        :rtype: ResponseSubmissionAnswers
        """
        return util.deserialize_model(dikt, cls)

    @property
    def question_id(self) -> int:
        """Gets the question_id of this ResponseSubmissionAnswers.


        :return: The question_id of this ResponseSubmissionAnswers.
        :rtype: int
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id: int):
        """Sets the question_id of this ResponseSubmissionAnswers.


        :param question_id: The question_id of this ResponseSubmissionAnswers.
        :type question_id: int
        """

        self._question_id = question_id

    @property
    def answer(self) -> str:
        """Gets the answer of this ResponseSubmissionAnswers.


        :return: The answer of this ResponseSubmissionAnswers.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        """Sets the answer of this ResponseSubmissionAnswers.


        :param answer: The answer of this ResponseSubmissionAnswers.
        :type answer: str
        """

        self._answer = answer
