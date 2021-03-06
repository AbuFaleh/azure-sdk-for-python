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

try:
    from ._models_py3 import AddressSpace
    from ._models_py3 import ApplicationGateway
    from ._models_py3 import ApplicationGatewayBackendAddress
    from ._models_py3 import ApplicationGatewayBackendAddressPool
    from ._models_py3 import ApplicationGatewayBackendHttpSettings
    from ._models_py3 import ApplicationGatewayFrontendIPConfiguration
    from ._models_py3 import ApplicationGatewayFrontendPort
    from ._models_py3 import ApplicationGatewayHttpListener
    from ._models_py3 import ApplicationGatewayIPConfiguration
    from ._models_py3 import ApplicationGatewayPathRule
    from ._models_py3 import ApplicationGatewayProbe
    from ._models_py3 import ApplicationGatewayRequestRoutingRule
    from ._models_py3 import ApplicationGatewaySku
    from ._models_py3 import ApplicationGatewaySslCertificate
    from ._models_py3 import ApplicationGatewayUrlPathMap
    from ._models_py3 import AzureAsyncOperationResult
    from ._models_py3 import BackendAddressPool
    from ._models_py3 import BgpSettings
    from ._models_py3 import ConnectionResetSharedKey
    from ._models_py3 import ConnectionSharedKey
    from ._models_py3 import ConnectionSharedKeyResult
    from ._models_py3 import DhcpOptions
    from ._models_py3 import DnsNameAvailabilityResult
    from ._models_py3 import Error
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ExpressRouteCircuit
    from ._models_py3 import ExpressRouteCircuitArpTable
    from ._models_py3 import ExpressRouteCircuitAuthorization
    from ._models_py3 import ExpressRouteCircuitPeering
    from ._models_py3 import ExpressRouteCircuitPeeringConfig
    from ._models_py3 import ExpressRouteCircuitRoutesTable
    from ._models_py3 import ExpressRouteCircuitServiceProviderProperties
    from ._models_py3 import ExpressRouteCircuitSku
    from ._models_py3 import ExpressRouteCircuitStats
    from ._models_py3 import ExpressRouteServiceProvider
    from ._models_py3 import ExpressRouteServiceProviderBandwidthsOffered
    from ._models_py3 import FrontendIPConfiguration
    from ._models_py3 import InboundNatPool
    from ._models_py3 import InboundNatRule
    from ._models_py3 import IPConfiguration
    from ._models_py3 import LoadBalancer
    from ._models_py3 import LoadBalancingRule
    from ._models_py3 import LocalNetworkGateway
    from ._models_py3 import NetworkInterface
    from ._models_py3 import NetworkInterfaceDnsSettings
    from ._models_py3 import NetworkInterfaceIPConfiguration
    from ._models_py3 import NetworkSecurityGroup
    from ._models_py3 import OutboundNatRule
    from ._models_py3 import Probe
    from ._models_py3 import PublicIPAddress
    from ._models_py3 import PublicIPAddressDnsSettings
    from ._models_py3 import Resource
    from ._models_py3 import Route
    from ._models_py3 import RouteTable
    from ._models_py3 import SecurityRule
    from ._models_py3 import Subnet
    from ._models_py3 import SubResource
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import VirtualNetwork
    from ._models_py3 import VirtualNetworkGateway
    from ._models_py3 import VirtualNetworkGatewayConnection
    from ._models_py3 import VirtualNetworkGatewayIPConfiguration
    from ._models_py3 import VirtualNetworkGatewaySku
    from ._models_py3 import VpnClientConfiguration
    from ._models_py3 import VpnClientParameters
    from ._models_py3 import VpnClientRevokedCertificate
    from ._models_py3 import VpnClientRootCertificate
except (SyntaxError, ImportError):
    from ._models import AddressSpace
    from ._models import ApplicationGateway
    from ._models import ApplicationGatewayBackendAddress
    from ._models import ApplicationGatewayBackendAddressPool
    from ._models import ApplicationGatewayBackendHttpSettings
    from ._models import ApplicationGatewayFrontendIPConfiguration
    from ._models import ApplicationGatewayFrontendPort
    from ._models import ApplicationGatewayHttpListener
    from ._models import ApplicationGatewayIPConfiguration
    from ._models import ApplicationGatewayPathRule
    from ._models import ApplicationGatewayProbe
    from ._models import ApplicationGatewayRequestRoutingRule
    from ._models import ApplicationGatewaySku
    from ._models import ApplicationGatewaySslCertificate
    from ._models import ApplicationGatewayUrlPathMap
    from ._models import AzureAsyncOperationResult
    from ._models import BackendAddressPool
    from ._models import BgpSettings
    from ._models import ConnectionResetSharedKey
    from ._models import ConnectionSharedKey
    from ._models import ConnectionSharedKeyResult
    from ._models import DhcpOptions
    from ._models import DnsNameAvailabilityResult
    from ._models import Error
    from ._models import ErrorDetails
    from ._models import ExpressRouteCircuit
    from ._models import ExpressRouteCircuitArpTable
    from ._models import ExpressRouteCircuitAuthorization
    from ._models import ExpressRouteCircuitPeering
    from ._models import ExpressRouteCircuitPeeringConfig
    from ._models import ExpressRouteCircuitRoutesTable
    from ._models import ExpressRouteCircuitServiceProviderProperties
    from ._models import ExpressRouteCircuitSku
    from ._models import ExpressRouteCircuitStats
    from ._models import ExpressRouteServiceProvider
    from ._models import ExpressRouteServiceProviderBandwidthsOffered
    from ._models import FrontendIPConfiguration
    from ._models import InboundNatPool
    from ._models import InboundNatRule
    from ._models import IPConfiguration
    from ._models import LoadBalancer
    from ._models import LoadBalancingRule
    from ._models import LocalNetworkGateway
    from ._models import NetworkInterface
    from ._models import NetworkInterfaceDnsSettings
    from ._models import NetworkInterfaceIPConfiguration
    from ._models import NetworkSecurityGroup
    from ._models import OutboundNatRule
    from ._models import Probe
    from ._models import PublicIPAddress
    from ._models import PublicIPAddressDnsSettings
    from ._models import Resource
    from ._models import Route
    from ._models import RouteTable
    from ._models import SecurityRule
    from ._models import Subnet
    from ._models import SubResource
    from ._models import Usage
    from ._models import UsageName
    from ._models import VirtualNetwork
    from ._models import VirtualNetworkGateway
    from ._models import VirtualNetworkGatewayConnection
    from ._models import VirtualNetworkGatewayIPConfiguration
    from ._models import VirtualNetworkGatewaySku
    from ._models import VpnClientConfiguration
    from ._models import VpnClientParameters
    from ._models import VpnClientRevokedCertificate
    from ._models import VpnClientRootCertificate
from ._paged_models import ApplicationGatewayPaged
from ._paged_models import ExpressRouteCircuitArpTablePaged
from ._paged_models import ExpressRouteCircuitAuthorizationPaged
from ._paged_models import ExpressRouteCircuitPaged
from ._paged_models import ExpressRouteCircuitPeeringPaged
from ._paged_models import ExpressRouteCircuitRoutesTablePaged
from ._paged_models import ExpressRouteCircuitStatsPaged
from ._paged_models import ExpressRouteServiceProviderPaged
from ._paged_models import LoadBalancerPaged
from ._paged_models import LocalNetworkGatewayPaged
from ._paged_models import NetworkInterfacePaged
from ._paged_models import NetworkSecurityGroupPaged
from ._paged_models import PublicIPAddressPaged
from ._paged_models import RoutePaged
from ._paged_models import RouteTablePaged
from ._paged_models import SecurityRulePaged
from ._paged_models import SubnetPaged
from ._paged_models import UsagePaged
from ._paged_models import VirtualNetworkGatewayConnectionPaged
from ._paged_models import VirtualNetworkGatewayPaged
from ._paged_models import VirtualNetworkPaged
from ._network_management_client_enums import (
    ApplicationGatewaySkuName,
    ApplicationGatewayTier,
    IPAllocationMethod,
    TransportProtocol,
    SecurityRuleProtocol,
    SecurityRuleAccess,
    SecurityRuleDirection,
    RouteNextHopType,
    ApplicationGatewayProtocol,
    ApplicationGatewayCookieBasedAffinity,
    ApplicationGatewayRequestRoutingRuleType,
    ApplicationGatewayOperationalState,
    AuthorizationUseStatus,
    ExpressRouteCircuitPeeringAdvertisedPublicPrefixState,
    ExpressRouteCircuitPeeringType,
    ExpressRouteCircuitPeeringState,
    ExpressRouteCircuitSkuTier,
    ExpressRouteCircuitSkuFamily,
    ServiceProviderProvisioningState,
    LoadDistribution,
    ProbeProtocol,
    NetworkOperationStatus,
    VirtualNetworkGatewayType,
    VpnType,
    VirtualNetworkGatewaySkuName,
    VirtualNetworkGatewaySkuTier,
    ProcessorArchitecture,
    VirtualNetworkGatewayConnectionType,
    VirtualNetworkGatewayConnectionStatus,
)

__all__ = [
    'AddressSpace',
    'ApplicationGateway',
    'ApplicationGatewayBackendAddress',
    'ApplicationGatewayBackendAddressPool',
    'ApplicationGatewayBackendHttpSettings',
    'ApplicationGatewayFrontendIPConfiguration',
    'ApplicationGatewayFrontendPort',
    'ApplicationGatewayHttpListener',
    'ApplicationGatewayIPConfiguration',
    'ApplicationGatewayPathRule',
    'ApplicationGatewayProbe',
    'ApplicationGatewayRequestRoutingRule',
    'ApplicationGatewaySku',
    'ApplicationGatewaySslCertificate',
    'ApplicationGatewayUrlPathMap',
    'AzureAsyncOperationResult',
    'BackendAddressPool',
    'BgpSettings',
    'ConnectionResetSharedKey',
    'ConnectionSharedKey',
    'ConnectionSharedKeyResult',
    'DhcpOptions',
    'DnsNameAvailabilityResult',
    'Error',
    'ErrorDetails',
    'ExpressRouteCircuit',
    'ExpressRouteCircuitArpTable',
    'ExpressRouteCircuitAuthorization',
    'ExpressRouteCircuitPeering',
    'ExpressRouteCircuitPeeringConfig',
    'ExpressRouteCircuitRoutesTable',
    'ExpressRouteCircuitServiceProviderProperties',
    'ExpressRouteCircuitSku',
    'ExpressRouteCircuitStats',
    'ExpressRouteServiceProvider',
    'ExpressRouteServiceProviderBandwidthsOffered',
    'FrontendIPConfiguration',
    'InboundNatPool',
    'InboundNatRule',
    'IPConfiguration',
    'LoadBalancer',
    'LoadBalancingRule',
    'LocalNetworkGateway',
    'NetworkInterface',
    'NetworkInterfaceDnsSettings',
    'NetworkInterfaceIPConfiguration',
    'NetworkSecurityGroup',
    'OutboundNatRule',
    'Probe',
    'PublicIPAddress',
    'PublicIPAddressDnsSettings',
    'Resource',
    'Route',
    'RouteTable',
    'SecurityRule',
    'Subnet',
    'SubResource',
    'Usage',
    'UsageName',
    'VirtualNetwork',
    'VirtualNetworkGateway',
    'VirtualNetworkGatewayConnection',
    'VirtualNetworkGatewayIPConfiguration',
    'VirtualNetworkGatewaySku',
    'VpnClientConfiguration',
    'VpnClientParameters',
    'VpnClientRevokedCertificate',
    'VpnClientRootCertificate',
    'ApplicationGatewayPaged',
    'ExpressRouteCircuitAuthorizationPaged',
    'ExpressRouteCircuitPeeringPaged',
    'ExpressRouteCircuitArpTablePaged',
    'ExpressRouteCircuitRoutesTablePaged',
    'ExpressRouteCircuitStatsPaged',
    'ExpressRouteCircuitPaged',
    'ExpressRouteServiceProviderPaged',
    'LoadBalancerPaged',
    'NetworkInterfacePaged',
    'NetworkSecurityGroupPaged',
    'SecurityRulePaged',
    'PublicIPAddressPaged',
    'RouteTablePaged',
    'RoutePaged',
    'UsagePaged',
    'VirtualNetworkPaged',
    'SubnetPaged',
    'VirtualNetworkGatewayPaged',
    'VirtualNetworkGatewayConnectionPaged',
    'LocalNetworkGatewayPaged',
    'ApplicationGatewaySkuName',
    'ApplicationGatewayTier',
    'IPAllocationMethod',
    'TransportProtocol',
    'SecurityRuleProtocol',
    'SecurityRuleAccess',
    'SecurityRuleDirection',
    'RouteNextHopType',
    'ApplicationGatewayProtocol',
    'ApplicationGatewayCookieBasedAffinity',
    'ApplicationGatewayRequestRoutingRuleType',
    'ApplicationGatewayOperationalState',
    'AuthorizationUseStatus',
    'ExpressRouteCircuitPeeringAdvertisedPublicPrefixState',
    'ExpressRouteCircuitPeeringType',
    'ExpressRouteCircuitPeeringState',
    'ExpressRouteCircuitSkuTier',
    'ExpressRouteCircuitSkuFamily',
    'ServiceProviderProvisioningState',
    'LoadDistribution',
    'ProbeProtocol',
    'NetworkOperationStatus',
    'VirtualNetworkGatewayType',
    'VpnType',
    'VirtualNetworkGatewaySkuName',
    'VirtualNetworkGatewaySkuTier',
    'ProcessorArchitecture',
    'VirtualNetworkGatewayConnectionType',
    'VirtualNetworkGatewayConnectionStatus',
]
