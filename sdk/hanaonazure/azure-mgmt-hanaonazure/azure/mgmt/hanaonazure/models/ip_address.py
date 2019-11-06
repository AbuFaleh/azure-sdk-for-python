# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IpAddress(Model):
    """Specifies the IP address of the network interface.

    :param ip_address: Specifies the IP address of the network interface.
    :type ip_address: str
    """

    _attribute_map = {
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IpAddress, self).__init__(**kwargs)
        self.ip_address = kwargs.get('ip_address', None)