# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._azure_blob_storage import AzureBlobStorage
__all__ = ['AzureBlobStorage']

try:
    from .patch import patch_sdk
    patch_sdk()
except ImportError:
    pass
