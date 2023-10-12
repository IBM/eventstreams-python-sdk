# coding: utf-8

# (C) Copyright IBM Corp. 2023.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# IBM OpenAPI SDK Code Generator Version: 3.76.0-ad3e6f96-20230724-172814

"""
The administration REST API for IBM Event Streams on Cloud.

API Version: 1.3.0
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class AdminrestV1(BaseService):
    """The adminrest V1 service."""

    DEFAULT_SERVICE_URL = None
    DEFAULT_SERVICE_NAME = 'adminrest'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'AdminrestV1':
        """
        Return a new client for the adminrest service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the adminrest service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # createTopic
    #########################

    def create_topic(
        self,
        *,
        name: str = None,
        partitions: int = None,
        partition_count: int = None,
        configs: List['TopicCreateRequestConfigsItem'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new topic.

        Create a new topic.

        :param str name: (optional) The name of topic to be created.
        :param int partitions: (optional) The number of partitions.
        :param int partition_count: (optional) The number of partitions, this field
               takes precedence over 'partitions'. Default value is 1 if not specified.
        :param List[TopicCreateRequestConfigsItem] configs: (optional) The config
               properties to be set for the new topic.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if configs is not None:
            configs = [convert_model(x) for x in configs]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_topic',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'partitions': partitions,
            'partition_count': partition_count,
            'configs': configs,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/admin/topics'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # default
    #########################

    def alive(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Basic health check for Admin REST API.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='alive',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        url = '/alive'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_topics(
        self,
        *,
        topic_filter: str = None,
        per_page: int = None,
        page: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of topics.

        Returns a list containing information about all of the Kafka topics that are
        defined for an instance of the Event Streams service. If there are currently no
        topics defined then an empty list is returned.

        :param str topic_filter: (optional) A filter to be applied to the topic
               names. A simple filter can be specified as a string with asterisk (`*`)
               wildcards representing 0 or more characters, e.g. `topic-name*` will filter
               all topic names that begin with the string `topic-name` followed by any
               character sequence. A more complex filter pattern can be used by
               surrounding a regular expression in forward slash (`/`) delimiters, e.g.
               `/topic-name.* /`.
        :param int per_page: (optional) The number of topic names to be returned.
        :param int page: (optional) The page number to be returned. The number 1
               represents the first page. The default value is 1.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[TopicDetail]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_topics',
        )
        headers.update(sdk_headers)

        params = {
            'topic_filter': topic_filter,
            'per_page': per_page,
            'page': page,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/admin/topics'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_topic(
        self,
        topic_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get detailed information on a topic.

        Get detailed information on a topic.

        :param str topic_name: The topic name for the topic to be described.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TopicDetail` object
        """

        if not topic_name:
            raise ValueError('topic_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_topic',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['topic_name']
        path_param_values = self.encode_path_vars(topic_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/topics/{topic_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_topic(
        self,
        topic_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a topic.

        Delete a topic.

        :param str topic_name: The topic name for the topic to be deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not topic_name:
            raise ValueError('topic_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_topic',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['topic_name']
        path_param_values = self.encode_path_vars(topic_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/topics/{topic_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_topic(
        self,
        topic_name: str,
        *,
        new_total_partition_count: int = None,
        configs: List['TopicUpdateRequestConfigsItem'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Increase the number of partitions and/or update one or more topic configuration parameters.

        Increase the number of partitions and/or update one or more topic configuration
        parameters.

        :param str topic_name: The topic name for the topic to be updated.
        :param int new_total_partition_count: (optional) The new partition number
               to be increased to.
        :param List[TopicUpdateRequestConfigsItem] configs: (optional) The config
               properties to be updated for the topic. Valid config names are
               'cleanup.policy', 'retention.ms', 'retention.bytes', 'segment.bytes',
               'segment.ms', 'segment.index.bytes'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not topic_name:
            raise ValueError('topic_name must be provided')
        if configs is not None:
            configs = [convert_model(x) for x in configs]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_topic',
        )
        headers.update(sdk_headers)

        data = {
            'new_total_partition_count': new_total_partition_count,
            'configs': configs,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['topic_name']
        path_param_values = self.encode_path_vars(topic_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/topics/{topic_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_topic_records(
        self,
        topic_name: str,
        *,
        records_to_delete: List['RecordDeleteRequestRecordsToDeleteItem'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete records before the given offset on a topic.

        Delete records before the given offset on a topic.

        :param str topic_name: The topic name of the records to be deleted.
        :param List[RecordDeleteRequestRecordsToDeleteItem] records_to_delete:
               (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not topic_name:
            raise ValueError('topic_name must be provided')
        if records_to_delete is not None:
            records_to_delete = [convert_model(x) for x in records_to_delete]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_topic_records',
        )
        headers.update(sdk_headers)

        data = {
            'records_to_delete': records_to_delete,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['topic_name']
        path_param_values = self.encode_path_vars(topic_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/topics/{topic_name}/records'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_quota(
        self,
        entity_name: str,
        *,
        producer_byte_rate: int = None,
        consumer_byte_rate: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new quota.

        Create a new quota.

        :param str entity_name: The entity name of the quotas can be `default` or
               an IAM Service ID that starts with an `iam-ServiceId` prefix.
        :param int producer_byte_rate: (optional) The producer byte rate quota
               value.
        :param int consumer_byte_rate: (optional) The consumer byte rate quota
               value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not entity_name:
            raise ValueError('entity_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_quota',
        )
        headers.update(sdk_headers)

        data = {
            'producer_byte_rate': producer_byte_rate,
            'consumer_byte_rate': consumer_byte_rate,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['entity_name']
        path_param_values = self.encode_path_vars(entity_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/quotas/{entity_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def update_quota(
        self,
        entity_name: str,
        *,
        producer_byte_rate: int = None,
        consumer_byte_rate: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a quota.

        Update an entity's quota.

        :param str entity_name: The entity name of the quotas can be `default` or
               an IAM Service ID that starts with an `iam-ServiceId` prefix.
        :param int producer_byte_rate: (optional) The producer byte rate quota
               value.
        :param int consumer_byte_rate: (optional) The consumer byte rate quota
               value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not entity_name:
            raise ValueError('entity_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_quota',
        )
        headers.update(sdk_headers)

        data = {
            'producer_byte_rate': producer_byte_rate,
            'consumer_byte_rate': consumer_byte_rate,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['entity_name']
        path_param_values = self.encode_path_vars(entity_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/quotas/{entity_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_quota(
        self,
        entity_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a quota.

        Delete an entity's quota.

        :param str entity_name: The entity name of the quotas can be `default` or
               an IAM Service ID that starts with an `iam-ServiceId` prefix.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not entity_name:
            raise ValueError('entity_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_quota',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['entity_name']
        path_param_values = self.encode_path_vars(entity_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/quotas/{entity_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_quota(
        self,
        entity_name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get quota information for an entity.

        Get quota information for an entity.

        :param str entity_name: The entity name of the quotas can be `default` or
               an IAM Service ID that starts with an `iam-ServiceId` prefix.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `QuotaDetail` object
        """

        if not entity_name:
            raise ValueError('entity_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_quota',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['entity_name']
        path_param_values = self.encode_path_vars(entity_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/quotas/{entity_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_quotas(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List each entity's quota information.

        List each entity's quota information.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `QuotaList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_quotas',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/admin/quotas'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_brokers(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of brokers in the cluster.

        Get a list of brokers in the cluster.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[BrokerSummary]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_brokers',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/admin/brokers'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_broker(
        self,
        broker_id: int,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get detailed information for a single broker.

        Get detailed information for a single broker.

        :param int broker_id: The broker ID of the broker to be described.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrokerDetail` object
        """

        if broker_id is None:
            raise ValueError('broker_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_broker',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['broker_id']
        path_param_values = self.encode_path_vars(str(broker_id))
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/brokers/{broker_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_broker_config(
        self,
        broker_id: int,
        *,
        config_filter: str = None,
        verbose: bool = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get all configuration parameters for a single broker.

        Get all configuration parameters for a single broker.

        :param int broker_id: The broker ID of the broker to be described.
        :param str config_filter: (optional) A filter to be applied to the config
               names. A simple filter can be specified as a string with asterisk (`*`)
               wildcards representing 0 or more characters, e.g. `file*` will filter all
               config names that begin with the string `file` followed by any character
               sequence. A more complex filter pattern can be used by surrounding a
               regular expression in forward slash (`/`) delimiters, e.g. `/file.* /`.
        :param bool verbose: (optional) When true, all information about the config
               properties is returned including the source of the configuration indicating
               its scope and whether it's dynamic.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrokerDetail` object
        """

        if broker_id is None:
            raise ValueError('broker_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_broker_config',
        )
        headers.update(sdk_headers)

        params = {
            'config_filter': config_filter,
            'verbose': verbose,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['broker_id']
        path_param_values = self.encode_path_vars(str(broker_id))
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/brokers/{broker_id}/configs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_cluster(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get information about the cluster.

        Get information about the cluster.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Cluster` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_cluster',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/admin/cluster'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def list_consumer_groups(
        self,
        *,
        group_filter: str = None,
        per_page: int = None,
        page: int = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a list of consumer group IDs.

        Get a list of consumer group IDs.

        :param str group_filter: (optional) A filter to be applied to the consumer
               group IDs. A simple filter can be specified as a string with asterisk (`*`)
               wildcards representing 0 or more characters, e.g. `group_id*` will filter
               all group IDs that begin with the string `group_id` followed by any
               character sequence. A more complex filter pattern can be used by
               surrounding a regular expression in forward slash (`/`) delimiters, e.g.
               `/group_id.* /`.
        :param int per_page: (optional) The number of consumer groups to be
               returned.
        :param int page: (optional) The page number to be returned. The number 1
               represents the first page. The default value is 1.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[str]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_consumer_groups',
        )
        headers.update(sdk_headers)

        params = {
            'group_filter': group_filter,
            'per_page': per_page,
            'page': page,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/admin/consumergroups'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_consumer_group(
        self,
        group_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get detailed information on a consumer group.

        Get detailed information on a consumer group.

        :param str group_id: The group ID for the consumer group to be described.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GroupDetail` object
        """

        if not group_id:
            raise ValueError('group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_consumer_group',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['group_id']
        path_param_values = self.encode_path_vars(group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/consumergroups/{group_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_consumer_group(
        self,
        group_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a consumer group.

        Delete a consumer group.

        :param str group_id: The group ID for the consumer group to be deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not group_id:
            raise ValueError('group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_consumer_group',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['group_id']
        path_param_values = self.encode_path_vars(group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/consumergroups/{group_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_consumer_group(
        self,
        group_id: str,
        *,
        topic: str = None,
        mode: str = None,
        value: str = None,
        execute: bool = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the offsets of a consumer group.

        Update the offsets of a consumer group using various modes, eg. latest, earliest,
        datetime,etc.

        :param str group_id: The group ID for the consumer group to be updated.
        :param str topic: (optional) The name of the topic to be reset.  If missing
               or blank, the operation applies to all topics read by the consumer group.
        :param str mode: (optional) Mode of shift operation.  Valid values are
               'earliest', 'latest', 'datetime'.
        :param str value: (optional) Value for resetting offsets, based on
               'mode=datetime', omit for 'earliest' and 'latest'.
        :param bool execute: (optional) Whether to execute the operation of
               resetting the offsets.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[GroupResetResultsItem]` result
        """

        if not group_id:
            raise ValueError('group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_consumer_group',
        )
        headers.update(sdk_headers)

        data = {
            'topic': topic,
            'mode': mode,
            'value': value,
            'execute': execute,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['group_id']
        path_param_values = self.encode_path_vars(group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/consumergroups/{group_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_mirroring_topic_selection(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get current topic selection for mirroring.

        Get current topic selection for mirroring.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MirroringTopicSelection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_mirroring_topic_selection',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/admin/mirroring/topic-selection'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_mirroring_topic_selection(
        self,
        *,
        includes: List[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Replace topic selection for mirroring.

        Replace topic selection for mirroring. This operation replaces the complete set of
        mirroring topic selections.

        :param List[str] includes: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MirroringTopicSelection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='replace_mirroring_topic_selection',
        )
        headers.update(sdk_headers)

        data = {
            'includes': includes,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/admin/mirroring/topic-selection'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_mirroring_active_topics(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get topics that are being actively mirrored.

        Get topics that are being actively mirrored.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MirroringActiveTopics` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_mirroring_active_topics',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/admin/mirroring/active-topics'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class BrokerDetailConfigsItem:
    """
    BrokerDetailConfigsItem.

    :attr str name: (optional) The name of the config property.
    :attr str value: (optional) The value for a config property.
    :attr bool is_sensitive: (optional) When true, the value cannot be displayed and
          will be returned with a null value.
    """

    def __init__(
        self,
        *,
        name: str = None,
        value: str = None,
        is_sensitive: bool = None,
    ) -> None:
        """
        Initialize a BrokerDetailConfigsItem object.

        :param str name: (optional) The name of the config property.
        :param str value: (optional) The value for a config property.
        :param bool is_sensitive: (optional) When true, the value cannot be
               displayed and will be returned with a null value.
        """
        self.name = name
        self.value = value
        self.is_sensitive = is_sensitive

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BrokerDetailConfigsItem':
        """Initialize a BrokerDetailConfigsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'is_sensitive' in _dict:
            args['is_sensitive'] = _dict.get('is_sensitive')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BrokerDetailConfigsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'is_sensitive') and self.is_sensitive is not None:
            _dict['is_sensitive'] = self.is_sensitive
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BrokerDetailConfigsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BrokerDetailConfigsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BrokerDetailConfigsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GroupResetResultsItem:
    """
    The new offset for one partition of one topic after resetting consumer group's offset.

    :attr str topic: (optional)
    :attr int partition: (optional)
    :attr int offset: (optional)
    """

    def __init__(
        self,
        *,
        topic: str = None,
        partition: int = None,
        offset: int = None,
    ) -> None:
        """
        Initialize a GroupResetResultsItem object.

        :param str topic: (optional)
        :param int partition: (optional)
        :param int offset: (optional)
        """
        self.topic = topic
        self.partition = partition
        self.offset = offset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GroupResetResultsItem':
        """Initialize a GroupResetResultsItem object from a json dictionary."""
        args = {}
        if 'topic' in _dict:
            args['topic'] = _dict.get('topic')
        if 'partition' in _dict:
            args['partition'] = _dict.get('partition')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GroupResetResultsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'topic') and self.topic is not None:
            _dict['topic'] = self.topic
        if hasattr(self, 'partition') and self.partition is not None:
            _dict['partition'] = self.partition
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GroupResetResultsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GroupResetResultsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GroupResetResultsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MemberAssignmentsItem:
    """
    The topic partitions assigned for the consumer group member.

    :attr str topic: (optional) The name of the topic.
    :attr int partition: (optional) The ID of the partition.
    """

    def __init__(
        self,
        *,
        topic: str = None,
        partition: int = None,
    ) -> None:
        """
        Initialize a MemberAssignmentsItem object.

        :param str topic: (optional) The name of the topic.
        :param int partition: (optional) The ID of the partition.
        """
        self.topic = topic
        self.partition = partition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MemberAssignmentsItem':
        """Initialize a MemberAssignmentsItem object from a json dictionary."""
        args = {}
        if 'topic' in _dict:
            args['topic'] = _dict.get('topic')
        if 'partition' in _dict:
            args['partition'] = _dict.get('partition')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MemberAssignmentsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'topic') and self.topic is not None:
            _dict['topic'] = self.topic
        if hasattr(self, 'partition') and self.partition is not None:
            _dict['partition'] = self.partition
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MemberAssignmentsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MemberAssignmentsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MemberAssignmentsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RecordDeleteRequestRecordsToDeleteItem:
    """
    RecordDeleteRequestRecordsToDeleteItem.

    :attr int partition: (optional) The number of partitions.
    :attr int before_offset: (optional) The offset number before which records to be
          deleted.
    """

    def __init__(
        self,
        *,
        partition: int = None,
        before_offset: int = None,
    ) -> None:
        """
        Initialize a RecordDeleteRequestRecordsToDeleteItem object.

        :param int partition: (optional) The number of partitions.
        :param int before_offset: (optional) The offset number before which records
               to be deleted.
        """
        self.partition = partition
        self.before_offset = before_offset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecordDeleteRequestRecordsToDeleteItem':
        """Initialize a RecordDeleteRequestRecordsToDeleteItem object from a json dictionary."""
        args = {}
        if 'partition' in _dict:
            args['partition'] = _dict.get('partition')
        if 'before_offset' in _dict:
            args['before_offset'] = _dict.get('before_offset')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecordDeleteRequestRecordsToDeleteItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'partition') and self.partition is not None:
            _dict['partition'] = self.partition
        if hasattr(self, 'before_offset') and self.before_offset is not None:
            _dict['before_offset'] = self.before_offset
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RecordDeleteRequestRecordsToDeleteItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecordDeleteRequestRecordsToDeleteItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecordDeleteRequestRecordsToDeleteItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TopicCreateRequestConfigsItem:
    """
    TopicCreateRequestConfigsItem.

    :attr str name: (optional) The name of the config property.
    :attr str value: (optional) The value for a config property.
    """

    def __init__(
        self,
        *,
        name: str = None,
        value: str = None,
    ) -> None:
        """
        Initialize a TopicCreateRequestConfigsItem object.

        :param str name: (optional) The name of the config property.
        :param str value: (optional) The value for a config property.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopicCreateRequestConfigsItem':
        """Initialize a TopicCreateRequestConfigsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopicCreateRequestConfigsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopicCreateRequestConfigsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TopicCreateRequestConfigsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopicCreateRequestConfigsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TopicDetailReplicaAssignmentsItem:
    """
    TopicDetailReplicaAssignmentsItem.

    :attr int id: (optional) The ID of the partition.
    :attr TopicDetailReplicaAssignmentsItemBrokers brokers: (optional)
    """

    def __init__(
        self,
        *,
        id: int = None,
        brokers: 'TopicDetailReplicaAssignmentsItemBrokers' = None,
    ) -> None:
        """
        Initialize a TopicDetailReplicaAssignmentsItem object.

        :param int id: (optional) The ID of the partition.
        :param TopicDetailReplicaAssignmentsItemBrokers brokers: (optional)
        """
        self.id = id
        self.brokers = brokers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopicDetailReplicaAssignmentsItem':
        """Initialize a TopicDetailReplicaAssignmentsItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'brokers' in _dict:
            args['brokers'] = TopicDetailReplicaAssignmentsItemBrokers.from_dict(_dict.get('brokers'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopicDetailReplicaAssignmentsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'brokers') and self.brokers is not None:
            if isinstance(self.brokers, dict):
                _dict['brokers'] = self.brokers
            else:
                _dict['brokers'] = self.brokers.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopicDetailReplicaAssignmentsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TopicDetailReplicaAssignmentsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopicDetailReplicaAssignmentsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TopicDetailReplicaAssignmentsItemBrokers:
    """
    TopicDetailReplicaAssignmentsItemBrokers.

    :attr List[int] replicas: (optional)
    """

    def __init__(
        self,
        *,
        replicas: List[int] = None,
    ) -> None:
        """
        Initialize a TopicDetailReplicaAssignmentsItemBrokers object.

        :param List[int] replicas: (optional)
        """
        self.replicas = replicas

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopicDetailReplicaAssignmentsItemBrokers':
        """Initialize a TopicDetailReplicaAssignmentsItemBrokers object from a json dictionary."""
        args = {}
        if 'replicas' in _dict:
            args['replicas'] = _dict.get('replicas')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopicDetailReplicaAssignmentsItemBrokers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'replicas') and self.replicas is not None:
            _dict['replicas'] = self.replicas
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopicDetailReplicaAssignmentsItemBrokers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TopicDetailReplicaAssignmentsItemBrokers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopicDetailReplicaAssignmentsItemBrokers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TopicUpdateRequestConfigsItem:
    """
    TopicUpdateRequestConfigsItem.

    :attr str name: (optional) The name of the config property.
    :attr str value: (optional) The value of a config property.
    :attr bool reset_to_default: (optional) When true, the value of the config
          property is reset to its default value.
    """

    def __init__(
        self,
        *,
        name: str = None,
        value: str = None,
        reset_to_default: bool = None,
    ) -> None:
        """
        Initialize a TopicUpdateRequestConfigsItem object.

        :param str name: (optional) The name of the config property.
        :param str value: (optional) The value of a config property.
        :param bool reset_to_default: (optional) When true, the value of the config
               property is reset to its default value.
        """
        self.name = name
        self.value = value
        self.reset_to_default = reset_to_default

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopicUpdateRequestConfigsItem':
        """Initialize a TopicUpdateRequestConfigsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'reset_to_default' in _dict:
            args['reset_to_default'] = _dict.get('reset_to_default')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopicUpdateRequestConfigsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'reset_to_default') and self.reset_to_default is not None:
            _dict['reset_to_default'] = self.reset_to_default
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopicUpdateRequestConfigsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TopicUpdateRequestConfigsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopicUpdateRequestConfigsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BrokerDetail:
    """
    BrokerDetail.

    :attr int id: (optional) The ID of the broker configured in the 'broker.id'
          broker config property.
    :attr str host: (optional) The hostname that the broker is listening on and
          which is configured in the 'advertised.listeners' broker config property.
    :attr int port: (optional) The port that the broker is listening on and which is
          configured in the 'advertised.listeners' broker config property.
    :attr str rack: (optional) The rack of the broker used in rack aware replication
          assignment for fault tolerance. It is configure in the 'broker.rack' broker
          config property.
    :attr List[BrokerDetailConfigsItem] configs: (optional)
    """

    def __init__(
        self,
        *,
        id: int = None,
        host: str = None,
        port: int = None,
        rack: str = None,
        configs: List['BrokerDetailConfigsItem'] = None,
    ) -> None:
        """
        Initialize a BrokerDetail object.

        :param int id: (optional) The ID of the broker configured in the
               'broker.id' broker config property.
        :param str host: (optional) The hostname that the broker is listening on
               and which is configured in the 'advertised.listeners' broker config
               property.
        :param int port: (optional) The port that the broker is listening on and
               which is configured in the 'advertised.listeners' broker config property.
        :param str rack: (optional) The rack of the broker used in rack aware
               replication assignment for fault tolerance. It is configure in the
               'broker.rack' broker config property.
        :param List[BrokerDetailConfigsItem] configs: (optional)
        """
        self.id = id
        self.host = host
        self.port = port
        self.rack = rack
        self.configs = configs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BrokerDetail':
        """Initialize a BrokerDetail object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        if 'rack' in _dict:
            args['rack'] = _dict.get('rack')
        if 'configs' in _dict:
            args['configs'] = [BrokerDetailConfigsItem.from_dict(v) for v in _dict.get('configs')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BrokerDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'rack') and self.rack is not None:
            _dict['rack'] = self.rack
        if hasattr(self, 'configs') and self.configs is not None:
            configs_list = []
            for v in self.configs:
                if isinstance(v, dict):
                    configs_list.append(v)
                else:
                    configs_list.append(v.to_dict())
            _dict['configs'] = configs_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BrokerDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BrokerDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BrokerDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BrokerSummary:
    """
    BrokerSummary.

    :attr int id: (optional) The ID of the broker configured in the 'broker.id'
          broker config property.
    :attr str host: (optional) The hostname that the broker is listening on and
          which is configured in the 'advertised.listeners' broker config property.
    :attr int port: (optional) The port that the broker is listening on and which is
          configured in the 'advertised.listeners' broker config property.
    :attr str rack: (optional) The rack of the broker used in rack aware replication
          assignment for fault tolerance. It is configure in the 'broker.rack' broker
          config property.
    """

    def __init__(
        self,
        *,
        id: int = None,
        host: str = None,
        port: int = None,
        rack: str = None,
    ) -> None:
        """
        Initialize a BrokerSummary object.

        :param int id: (optional) The ID of the broker configured in the
               'broker.id' broker config property.
        :param str host: (optional) The hostname that the broker is listening on
               and which is configured in the 'advertised.listeners' broker config
               property.
        :param int port: (optional) The port that the broker is listening on and
               which is configured in the 'advertised.listeners' broker config property.
        :param str rack: (optional) The rack of the broker used in rack aware
               replication assignment for fault tolerance. It is configure in the
               'broker.rack' broker config property.
        """
        self.id = id
        self.host = host
        self.port = port
        self.rack = rack

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BrokerSummary':
        """Initialize a BrokerSummary object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        if 'rack' in _dict:
            args['rack'] = _dict.get('rack')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BrokerSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'rack') and self.rack is not None:
            _dict['rack'] = self.rack
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BrokerSummary object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BrokerSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BrokerSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Cluster:
    """
    Cluster.

    :attr str id: (optional) The ID of the cluster.
    :attr BrokerSummary controller: (optional)
    :attr List[BrokerSummary] brokers: (optional) List of brokers in the cluster.
    """

    def __init__(
        self,
        *,
        id: str = None,
        controller: 'BrokerSummary' = None,
        brokers: List['BrokerSummary'] = None,
    ) -> None:
        """
        Initialize a Cluster object.

        :param str id: (optional) The ID of the cluster.
        :param BrokerSummary controller: (optional)
        :param List[BrokerSummary] brokers: (optional) List of brokers in the
               cluster.
        """
        self.id = id
        self.controller = controller
        self.brokers = brokers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Cluster':
        """Initialize a Cluster object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'controller' in _dict:
            args['controller'] = BrokerSummary.from_dict(_dict.get('controller'))
        if 'brokers' in _dict:
            args['brokers'] = [BrokerSummary.from_dict(v) for v in _dict.get('brokers')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Cluster object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'controller') and self.controller is not None:
            if isinstance(self.controller, dict):
                _dict['controller'] = self.controller
            else:
                _dict['controller'] = self.controller.to_dict()
        if hasattr(self, 'brokers') and self.brokers is not None:
            brokers_list = []
            for v in self.brokers:
                if isinstance(v, dict):
                    brokers_list.append(v)
                else:
                    brokers_list.append(v.to_dict())
            _dict['brokers'] = brokers_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Cluster object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Cluster') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Cluster') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityQuotaDetail:
    """
    EntityQuotaDetail.

    :attr str entity_name: The name of the entity.
    :attr int producer_byte_rate: (optional) The producer byte rate quota value.
    :attr int consumer_byte_rate: (optional) The consumer byte rate quota value.
    """

    def __init__(
        self,
        entity_name: str,
        *,
        producer_byte_rate: int = None,
        consumer_byte_rate: int = None,
    ) -> None:
        """
        Initialize a EntityQuotaDetail object.

        :param str entity_name: The name of the entity.
        :param int producer_byte_rate: (optional) The producer byte rate quota
               value.
        :param int consumer_byte_rate: (optional) The consumer byte rate quota
               value.
        """
        self.entity_name = entity_name
        self.producer_byte_rate = producer_byte_rate
        self.consumer_byte_rate = consumer_byte_rate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntityQuotaDetail':
        """Initialize a EntityQuotaDetail object from a json dictionary."""
        args = {}
        if 'entity_name' in _dict:
            args['entity_name'] = _dict.get('entity_name')
        else:
            raise ValueError('Required property \'entity_name\' not present in EntityQuotaDetail JSON')
        if 'producer_byte_rate' in _dict:
            args['producer_byte_rate'] = _dict.get('producer_byte_rate')
        if 'consumer_byte_rate' in _dict:
            args['consumer_byte_rate'] = _dict.get('consumer_byte_rate')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityQuotaDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity_name') and self.entity_name is not None:
            _dict['entity_name'] = self.entity_name
        if hasattr(self, 'producer_byte_rate') and self.producer_byte_rate is not None:
            _dict['producer_byte_rate'] = self.producer_byte_rate
        if hasattr(self, 'consumer_byte_rate') and self.consumer_byte_rate is not None:
            _dict['consumer_byte_rate'] = self.consumer_byte_rate
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntityQuotaDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EntityQuotaDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntityQuotaDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class GroupDetail:
    """
    GroupDetail.

    :attr str group_id: (optional) The ID of the consumer group.
    :attr str state: (optional) THe state of the consumer group.
    :attr List[Member] members: (optional) Members in the consumer group.
    :attr List[TopicPartitionOffset] offsets: (optional) The offsets of the consumer
          group.
    """

    def __init__(
        self,
        *,
        group_id: str = None,
        state: str = None,
        members: List['Member'] = None,
        offsets: List['TopicPartitionOffset'] = None,
    ) -> None:
        """
        Initialize a GroupDetail object.

        :param str group_id: (optional) The ID of the consumer group.
        :param str state: (optional) THe state of the consumer group.
        :param List[Member] members: (optional) Members in the consumer group.
        :param List[TopicPartitionOffset] offsets: (optional) The offsets of the
               consumer group.
        """
        self.group_id = group_id
        self.state = state
        self.members = members
        self.offsets = offsets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GroupDetail':
        """Initialize a GroupDetail object from a json dictionary."""
        args = {}
        if 'group_id' in _dict:
            args['group_id'] = _dict.get('group_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'members' in _dict:
            args['members'] = [Member.from_dict(v) for v in _dict.get('members')]
        if 'offsets' in _dict:
            args['offsets'] = [TopicPartitionOffset.from_dict(v) for v in _dict.get('offsets')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GroupDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'group_id') and self.group_id is not None:
            _dict['group_id'] = self.group_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'members') and self.members is not None:
            members_list = []
            for v in self.members:
                if isinstance(v, dict):
                    members_list.append(v)
                else:
                    members_list.append(v.to_dict())
            _dict['members'] = members_list
        if hasattr(self, 'offsets') and self.offsets is not None:
            offsets_list = []
            for v in self.offsets:
                if isinstance(v, dict):
                    offsets_list.append(v)
                else:
                    offsets_list.append(v.to_dict())
            _dict['offsets'] = offsets_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GroupDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GroupDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GroupDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Member:
    """
    Member.

    :attr str consumer_id: (optional) The consumer ID of the consumer group member.
    :attr str client_id: (optional) The client ID of the consumer group member.
    :attr str host: (optional) The hostname of the machine where the consumer group
          member is running.
    :attr List[MemberAssignmentsItem] assignments: (optional) The assignments of the
          group member.
    """

    def __init__(
        self,
        *,
        consumer_id: str = None,
        client_id: str = None,
        host: str = None,
        assignments: List['MemberAssignmentsItem'] = None,
    ) -> None:
        """
        Initialize a Member object.

        :param str consumer_id: (optional) The consumer ID of the consumer group
               member.
        :param str client_id: (optional) The client ID of the consumer group
               member.
        :param str host: (optional) The hostname of the machine where the consumer
               group member is running.
        :param List[MemberAssignmentsItem] assignments: (optional) The assignments
               of the group member.
        """
        self.consumer_id = consumer_id
        self.client_id = client_id
        self.host = host
        self.assignments = assignments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Member':
        """Initialize a Member object from a json dictionary."""
        args = {}
        if 'consumer_id' in _dict:
            args['consumer_id'] = _dict.get('consumer_id')
        if 'client_id' in _dict:
            args['client_id'] = _dict.get('client_id')
        if 'host' in _dict:
            args['host'] = _dict.get('host')
        if 'assignments' in _dict:
            args['assignments'] = [MemberAssignmentsItem.from_dict(v) for v in _dict.get('assignments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Member object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'consumer_id') and self.consumer_id is not None:
            _dict['consumer_id'] = self.consumer_id
        if hasattr(self, 'client_id') and self.client_id is not None:
            _dict['client_id'] = self.client_id
        if hasattr(self, 'host') and self.host is not None:
            _dict['host'] = self.host
        if hasattr(self, 'assignments') and self.assignments is not None:
            assignments_list = []
            for v in self.assignments:
                if isinstance(v, dict):
                    assignments_list.append(v)
                else:
                    assignments_list.append(v.to_dict())
            _dict['assignments'] = assignments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Member object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Member') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Member') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MirroringActiveTopics:
    """
    Topics that are being actively mirrored.

    :attr List[str] active_topics: (optional)
    """

    def __init__(
        self,
        *,
        active_topics: List[str] = None,
    ) -> None:
        """
        Initialize a MirroringActiveTopics object.

        :param List[str] active_topics: (optional)
        """
        self.active_topics = active_topics

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MirroringActiveTopics':
        """Initialize a MirroringActiveTopics object from a json dictionary."""
        args = {}
        if 'active_topics' in _dict:
            args['active_topics'] = _dict.get('active_topics')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MirroringActiveTopics object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'active_topics') and self.active_topics is not None:
            _dict['active_topics'] = self.active_topics
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MirroringActiveTopics object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MirroringActiveTopics') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MirroringActiveTopics') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MirroringTopicSelection:
    """
    Mirroring topic selection payload.

    :attr List[str] includes: (optional)
    """

    def __init__(
        self,
        *,
        includes: List[str] = None,
    ) -> None:
        """
        Initialize a MirroringTopicSelection object.

        :param List[str] includes: (optional)
        """
        self.includes = includes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MirroringTopicSelection':
        """Initialize a MirroringTopicSelection object from a json dictionary."""
        args = {}
        if 'includes' in _dict:
            args['includes'] = _dict.get('includes')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MirroringTopicSelection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'includes') and self.includes is not None:
            _dict['includes'] = self.includes
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MirroringTopicSelection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MirroringTopicSelection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MirroringTopicSelection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QuotaDetail:
    """
    QuotaDetail.

    :attr int producer_byte_rate: (optional) The producer byte rate quota value.
    :attr int consumer_byte_rate: (optional) The consumer byte rate quota value.
    """

    def __init__(
        self,
        *,
        producer_byte_rate: int = None,
        consumer_byte_rate: int = None,
    ) -> None:
        """
        Initialize a QuotaDetail object.

        :param int producer_byte_rate: (optional) The producer byte rate quota
               value.
        :param int consumer_byte_rate: (optional) The consumer byte rate quota
               value.
        """
        self.producer_byte_rate = producer_byte_rate
        self.consumer_byte_rate = consumer_byte_rate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QuotaDetail':
        """Initialize a QuotaDetail object from a json dictionary."""
        args = {}
        if 'producer_byte_rate' in _dict:
            args['producer_byte_rate'] = _dict.get('producer_byte_rate')
        if 'consumer_byte_rate' in _dict:
            args['consumer_byte_rate'] = _dict.get('consumer_byte_rate')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QuotaDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'producer_byte_rate') and self.producer_byte_rate is not None:
            _dict['producer_byte_rate'] = self.producer_byte_rate
        if hasattr(self, 'consumer_byte_rate') and self.consumer_byte_rate is not None:
            _dict['consumer_byte_rate'] = self.consumer_byte_rate
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QuotaDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QuotaDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QuotaDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class QuotaList:
    """
    A list of 'quota_detail' is returned.

    :attr List[EntityQuotaDetail] data: (optional)
    """

    def __init__(
        self,
        *,
        data: List['EntityQuotaDetail'] = None,
    ) -> None:
        """
        Initialize a QuotaList object.

        :param List[EntityQuotaDetail] data: (optional)
        """
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'QuotaList':
        """Initialize a QuotaList object from a json dictionary."""
        args = {}
        if 'data' in _dict:
            args['data'] = [EntityQuotaDetail.from_dict(v) for v in _dict.get('data')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a QuotaList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data') and self.data is not None:
            data_list = []
            for v in self.data:
                if isinstance(v, dict):
                    data_list.append(v)
                else:
                    data_list.append(v.to_dict())
            _dict['data'] = data_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this QuotaList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'QuotaList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'QuotaList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TopicConfigs:
    """
    TopicConfigs.

    :attr str retention_bytes: (optional) The value of config property
          'retention.bytes'.
    :attr str segment_bytes: (optional) The value of config property
          'segment.bytes'.
    :attr str segment_index_bytes: (optional) The value of config property
          'segment.index.bytes'.
    :attr str segment_ms: (optional) The value of config property 'segment.ms'.
    """

    def __init__(
        self,
        *,
        retention_bytes: str = None,
        segment_bytes: str = None,
        segment_index_bytes: str = None,
        segment_ms: str = None,
    ) -> None:
        """
        Initialize a TopicConfigs object.

        :param str retention_bytes: (optional) The value of config property
               'retention.bytes'.
        :param str segment_bytes: (optional) The value of config property
               'segment.bytes'.
        :param str segment_index_bytes: (optional) The value of config property
               'segment.index.bytes'.
        :param str segment_ms: (optional) The value of config property
               'segment.ms'.
        """
        self.retention_bytes = retention_bytes
        self.segment_bytes = segment_bytes
        self.segment_index_bytes = segment_index_bytes
        self.segment_ms = segment_ms

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopicConfigs':
        """Initialize a TopicConfigs object from a json dictionary."""
        args = {}
        if 'retention.bytes' in _dict:
            args['retention_bytes'] = _dict.get('retention.bytes')
        if 'segment.bytes' in _dict:
            args['segment_bytes'] = _dict.get('segment.bytes')
        if 'segment.index.bytes' in _dict:
            args['segment_index_bytes'] = _dict.get('segment.index.bytes')
        if 'segment.ms' in _dict:
            args['segment_ms'] = _dict.get('segment.ms')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopicConfigs object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'retention_bytes') and self.retention_bytes is not None:
            _dict['retention.bytes'] = self.retention_bytes
        if hasattr(self, 'segment_bytes') and self.segment_bytes is not None:
            _dict['segment.bytes'] = self.segment_bytes
        if hasattr(self, 'segment_index_bytes') and self.segment_index_bytes is not None:
            _dict['segment.index.bytes'] = self.segment_index_bytes
        if hasattr(self, 'segment_ms') and self.segment_ms is not None:
            _dict['segment.ms'] = self.segment_ms
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopicConfigs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TopicConfigs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopicConfigs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TopicDetail:
    """
    TopicDetail.

    :attr str name: (optional) The name of the topic.
    :attr int partitions: (optional) The number of partitions.
    :attr int replication_factor: (optional) The number of replication factor.
    :attr int retention_ms: (optional) The value of config property 'retention.ms'.
    :attr str cleanup_policy: (optional) The value of config property
          'cleanup.policy'.
    :attr TopicConfigs configs: (optional)
    :attr List[TopicDetailReplicaAssignmentsItem] replica_assignments: (optional)
          The replia assignment of the topic.
    """

    def __init__(
        self,
        *,
        name: str = None,
        partitions: int = None,
        replication_factor: int = None,
        retention_ms: int = None,
        cleanup_policy: str = None,
        configs: 'TopicConfigs' = None,
        replica_assignments: List['TopicDetailReplicaAssignmentsItem'] = None,
    ) -> None:
        """
        Initialize a TopicDetail object.

        :param str name: (optional) The name of the topic.
        :param int partitions: (optional) The number of partitions.
        :param int replication_factor: (optional) The number of replication factor.
        :param int retention_ms: (optional) The value of config property
               'retention.ms'.
        :param str cleanup_policy: (optional) The value of config property
               'cleanup.policy'.
        :param TopicConfigs configs: (optional)
        :param List[TopicDetailReplicaAssignmentsItem] replica_assignments:
               (optional) The replia assignment of the topic.
        """
        self.name = name
        self.partitions = partitions
        self.replication_factor = replication_factor
        self.retention_ms = retention_ms
        self.cleanup_policy = cleanup_policy
        self.configs = configs
        self.replica_assignments = replica_assignments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopicDetail':
        """Initialize a TopicDetail object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'partitions' in _dict:
            args['partitions'] = _dict.get('partitions')
        if 'replicationFactor' in _dict:
            args['replication_factor'] = _dict.get('replicationFactor')
        if 'retentionMs' in _dict:
            args['retention_ms'] = _dict.get('retentionMs')
        if 'cleanupPolicy' in _dict:
            args['cleanup_policy'] = _dict.get('cleanupPolicy')
        if 'configs' in _dict:
            args['configs'] = TopicConfigs.from_dict(_dict.get('configs'))
        if 'replicaAssignments' in _dict:
            args['replica_assignments'] = [TopicDetailReplicaAssignmentsItem.from_dict(v) for v in _dict.get('replicaAssignments')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopicDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'partitions') and self.partitions is not None:
            _dict['partitions'] = self.partitions
        if hasattr(self, 'replication_factor') and self.replication_factor is not None:
            _dict['replicationFactor'] = self.replication_factor
        if hasattr(self, 'retention_ms') and self.retention_ms is not None:
            _dict['retentionMs'] = self.retention_ms
        if hasattr(self, 'cleanup_policy') and self.cleanup_policy is not None:
            _dict['cleanupPolicy'] = self.cleanup_policy
        if hasattr(self, 'configs') and self.configs is not None:
            if isinstance(self.configs, dict):
                _dict['configs'] = self.configs
            else:
                _dict['configs'] = self.configs.to_dict()
        if hasattr(self, 'replica_assignments') and self.replica_assignments is not None:
            replicaAssignments_list = []
            for v in self.replica_assignments:
                if isinstance(v, dict):
                    replicaAssignments_list.append(v)
                else:
                    replicaAssignments_list.append(v.to_dict())
            _dict['replicaAssignments'] = replicaAssignments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopicDetail object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TopicDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopicDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TopicPartitionOffset:
    """
    The offsets of a topic partition.

    :attr str topic: (optional) The name of the topic.
    :attr int partition: (optional) The ID of the partition.
    :attr int current_offset: (optional) Current offset of the partition.
    :attr int end_offset: (optional) End offset of the partition.
    """

    def __init__(
        self,
        *,
        topic: str = None,
        partition: int = None,
        current_offset: int = None,
        end_offset: int = None,
    ) -> None:
        """
        Initialize a TopicPartitionOffset object.

        :param str topic: (optional) The name of the topic.
        :param int partition: (optional) The ID of the partition.
        :param int current_offset: (optional) Current offset of the partition.
        :param int end_offset: (optional) End offset of the partition.
        """
        self.topic = topic
        self.partition = partition
        self.current_offset = current_offset
        self.end_offset = end_offset

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopicPartitionOffset':
        """Initialize a TopicPartitionOffset object from a json dictionary."""
        args = {}
        if 'topic' in _dict:
            args['topic'] = _dict.get('topic')
        if 'partition' in _dict:
            args['partition'] = _dict.get('partition')
        if 'current_offset' in _dict:
            args['current_offset'] = _dict.get('current_offset')
        if 'end_offset' in _dict:
            args['end_offset'] = _dict.get('end_offset')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TopicPartitionOffset object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'topic') and self.topic is not None:
            _dict['topic'] = self.topic
        if hasattr(self, 'partition') and self.partition is not None:
            _dict['partition'] = self.partition
        if hasattr(self, 'current_offset') and self.current_offset is not None:
            _dict['current_offset'] = self.current_offset
        if hasattr(self, 'end_offset') and self.end_offset is not None:
            _dict['end_offset'] = self.end_offset
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TopicPartitionOffset object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TopicPartitionOffset') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TopicPartitionOffset') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
