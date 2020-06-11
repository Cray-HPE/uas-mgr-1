#
# Copyright 2019, Cray Inc.  All Rights Reserved.
#
# coding: utf-8
# pylint: disable=missing-docstring

from __future__ import absolute_import
from typing import Dict

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UAI(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    # pylint: disable=dangerous-default-value,too-many-arguments
    def __init__(self, uai_name: str = None, username: str = None,
                 publickey: str = None, uai_img: str = None,
                 uai_status: str = None, uai_msg: str = None,
                 uai_connect_string: str = None, uai_portmap: dict = {},
                 uai_host: str = None, uai_age: str = None):
        """UAI - a model defined in Swagger

        :param uai_name: The uai_name of this UAI.
        :type uai_name: str
        :param username: The username of this UAI.
        :type username: str
        :param publickey: The publickey of this UAI.
        :type publickey: str
        :param uai_img: The uai_img of this UAI.
        :type uai_img: str
        :param uai_status: The uai_status of this UAI.
        :type uai_status: str
        :param uai_msg: The uai_msg of this UAI.
        :type uai_msg: str
        :param uai_connect_string: The uai_connect_string of this
                                   UAI.
        :type uai_connect_string: str
        :param uai_portmap: The uai_portmap of this UAI.
        :type uai_portmap: Dict[str, int]
        :param uai_host: The physical host for this UAI.
        :type uai_host: str
        :param uai_age: Age of the UAI.
        :type uai_age: str
        """

        self.swagger_types = {
            'uai_name': str,
            'username': str,
            'publickey': str,
            'uai_img': str,
            'uai_status': str,
            'uai_msg': str,
            'uai_connect_string': str,
            'uai_portmap': Dict[str, int],
            'uai_host': str,
            'uai_age': str
        }

        self.attribute_map = {
            'uai_name': 'uai_name',
            'username': 'username',
            'publickey': 'publickey',
            'uai_img': 'uai_img',
            'uai_status': 'uai_status',
            'uai_msg': 'uai_msg',
            'uai_connect_string': 'uai_connect_string',
            'uai_portmap': 'uai_portmap',
            'uai_host': 'uai_host',
            'uai_age': 'uai_age'
        }
        self._uai_name = uai_name
        self._username = username
        self._publickey = publickey
        self._uai_img = uai_img
        self._uai_status = uai_status
        self._uai_msg = uai_msg
        self._uai_connect_string = uai_connect_string
        self._uai_portmap = uai_portmap
        self._uai_host = uai_host
        self._uai_age = uai_age

    @classmethod
    def from_dict(cls, dikt) -> 'UAI':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UAI of this UAI.
        :rtype: UAI
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uai_name(self) -> str:
        """Gets the uai_name of this UAI.


        :return: The uai_name of this UAI.
        :rtype: str
        """
        return self._uai_name

    @uai_name.setter
    def uai_name(self, uai_name: str):
        """Sets the uai_name of this UAI.


        :param uai_name: The uai_name of this UAI.
        :type uai_name: str
        """

        self._uai_name = uai_name

    @property
    def username(self) -> str:
        """Gets the username of this UAI.


        :return: The username of this UAI.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this UAI.


        :param username: The username of this UAI.
        :type username: str
        """

        self._username = username

    @property
    def publickey(self) -> str:
        """Gets the publickey of this UAI.


        :return: The publickey of this UAI.
        :rtype: str
        """
        return self._publickey

    @publickey.setter
    def publickey(self, publickey: str):
        """Sets the publickey of this UAI.


        :param publickey: The publickey of this UAI.
        :type publickey: str
        """

        self._publickey = publickey

    @property
    def uai_img(self) -> str:
        """Gets the uai_img of this UAI.


        :return: The uai_img of this UAI.
        :rtype: str
        """
        return self._uai_img

    @uai_img.setter
    def uai_img(self, uai_img: str):
        """Sets the uai_img of this UAI.


        :param uai_img: The uai_img of this UAI.
        :type uai_img: str
        """

        self._uai_img = uai_img

    @property
    def uai_status(self) -> str:
        """Gets the uai_status of this UAI.


        :return: The uai_status of this UAI.
        :rtype: str
        """
        return self._uai_status

    @uai_status.setter
    def uai_status(self, uai_status: str):
        """Sets the uai_status of this UAI.


        :param uai_status: The uai_status of this UAI.
        :type uai_status: str
        """

        self._uai_status = uai_status

    @property
    def uai_msg(self) -> str:
        """Gets the uai_msg of this UAI.


        :return: The uai_msg of this UAI.
        :rtype: str
        """
        return self._uai_msg

    @uai_msg.setter
    def uai_msg(self, uai_msg: str):
        """Sets the uai_msg of this UAI.


        :param uai_msg: The uai_msg of this UAI.
        :type uai_msg: str
        """

        self._uai_msg = uai_msg

    @property
    def uai_connect_string(self) -> str:
        """Gets the uai_connect_string of this UAI.


        :return: The uai_connect_string of this UAI.
        :rtype: str
        """
        return self._uai_connect_string

    @uai_connect_string.setter
    def uai_connect_string(self, uai_connect_string: str):
        """Sets the uai_connect_string of this UAI.


        :param uai_connect_string: The uai_connect_string of this UAI.
        :type uai_connect_string: str
        """

        self._uai_connect_string = uai_connect_string

    @property
    def uai_portmap(self) -> Dict[str, int]:
        """Gets the uai_portmap of this UAI.


        :return: The uai_portmap of this UAI.
        :rtype: Dict[str, int]
        """
        return self._uai_portmap

    @uai_portmap.setter
    def uai_portmap(self, uai_portmap: Dict[str, int]):
        """Sets the uai_portmap of this UAI.


        :param uai_portmap: The uai_portmap of this UAI.
        :type uai_portmap: Dict[str, int]
        """

        self._uai_portmap = uai_portmap

    @property
    def uai_host(self) -> str:
        """Gets the uai_host of this UAI.


        :return: The uai_host of this UAI.
        :rtype: str
        """
        return self._uai_host

    @uai_host.setter
    def uai_host(self, uai_host: str):
        """Sets the uai_host of this UAI.


        :param uai_host: The uai_host of this UAI.
        :type uai_host: str
        """

        self._uai_host = uai_host

    @property
    def uai_age(self) -> str:
        """Gets the uai_age of this UAI.


        :return: The uai_age of this UAI.
        :rtype: str
        """
        return self._uai_age

    @uai_age.setter
    def uai_age(self, uai_age: str):
        """Sets the uai_age of this UAI.


        :param uai_age: The uai_age of this UAI.
        :type uai_age: str
        """

        self._uai_age = uai_age
