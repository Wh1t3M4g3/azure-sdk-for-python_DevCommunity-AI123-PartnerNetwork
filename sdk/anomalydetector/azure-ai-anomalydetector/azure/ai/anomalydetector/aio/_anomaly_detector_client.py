# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from azure.core import AsyncPipelineClient
from azure.core.credentials import AzureKeyCredential
from azure.core.rest import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

from .. import models
from ._configuration import AnomalyDetectorClientConfiguration
from .operations import AnomalyDetectorClientOperationsMixin

class AnomalyDetectorClient(AnomalyDetectorClientOperationsMixin):
    """The Anomaly Detector API detects anomalies automatically in time series data. It supports two kinds of mode, one is for stateless using, another is for stateful using. In stateless mode, there are three functionalities. Entire Detect is for detecting the whole series with model trained by the time series, Last Detect is detecting last point with model trained by points before. ChangePoint Detect is for detecting trend changes in time series. In stateful mode, user can store time series, the stored time series will be used for detection anomalies. Under this mode, user can still use the above three functionalities by only giving a time range without preparing time series in client side. Besides the above three functionalities, stateful model also provide group based detection and labeling service. By leveraging labeling service user can provide labels for each detection result, these labels will be used for retuning or regenerating detection models. Inconsistency detection is a kind of group based detection, this detection will find inconsistency ones in a set of time series. By using anomaly detector service, business customers can discover incidents and establish a logic flow for root cause analysis.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://westus2.api.cognitive.microsoft.com).
    :type endpoint: str
    :keyword api_version: Anomaly Detector API version (for example, v1.0). The default value is
     "v1.1-preview.1". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: AzureKeyCredential,
        endpoint: str,
        **kwargs: Any
    ) -> None:
        _base_url = '{Endpoint}/anomalydetector/{ApiVersion}'
        self._config = AnomalyDetectorClientConfiguration(credential=credential, endpoint=endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=_base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AnomalyDetectorClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)