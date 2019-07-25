# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.amf_id import AmfId  # noqa: F401,E501
from swagger_server.models.plmn_id import PlmnId  # noqa: F401,E501
from swagger_server import util


class Guami(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, plmn_id=None, amf_id=None):  # noqa: E501
        """Guami - a model defined in Swagger

        :param plmn_id: The plmn_id of this Guami.  # noqa: E501
        :type plmn_id: PlmnId
        :param amf_id: The amf_id of this Guami.  # noqa: E501
        :type amf_id: AmfId
        """
        self.swagger_types = {
            'plmn_id': PlmnId,
            'amf_id': AmfId
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'amf_id': 'amfId'
        }
        self._plmn_id = plmn_id
        self._amf_id = amf_id

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Guami of this Guami.  # noqa: E501
        :rtype: Guami
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this Guami.


        :return: The plmn_id of this Guami.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this Guami.


        :param plmn_id: The plmn_id of this Guami.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def amf_id(self):
        """Gets the amf_id of this Guami.


        :return: The amf_id of this Guami.
        :rtype: AmfId
        """
        return self._amf_id

    @amf_id.setter
    def amf_id(self, amf_id):
        """Sets the amf_id of this Guami.


        :param amf_id: The amf_id of this Guami.
        :type amf_id: AmfId
        """
        if amf_id is None:
            raise ValueError("Invalid value for `amf_id`, must not be `None`")  # noqa: E501

        self._amf_id = amf_id