# coding: utf-8

# (C) Copyright IBM Corp. 2021.
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

# IBM OpenAPI SDK Code Generator Version: 3.25.0-2b3f843a-20210115-164628
 
"""
The administration REST API for IBM Event Streams on Cloud.
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

    DEFAULT_SERVICE_URL = 'https://adminrest.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'adminrest'

    @classmethod
    def new_instance(cls,
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

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the adminrest service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # default
    #########################


    def create_topic(self,
        *,
        name: str = None,
        partitions: int = None,
        partition_count: int = None,
        configs: List['ConfigCreate'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a new topic.

        Create a new topic.

        :param str name: (optional) The name of topic to be created.
        :param int partitions: (optional) The number of partitions.
        :param int partition_count: (optional) The number of partitions, this field
               takes precedence over 'partitions'. Default value is 1 if not specified.
        :param List[ConfigCreate] configs: (optional) The config properties to be
               set for the new topic.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if configs is not None:
            configs = [convert_model(x) for x in configs]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_topic')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'partitions': partitions,
            'partition_count': partition_count,
            'configs': configs
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/admin/topics'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_topics(self,
        *,
        topic_filter: str = None,
        per_page: int = None,
        page: int = None,
        **kwargs
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
        :param int per_page: (optional) The number of topic names to be returns.
        :param int page: (optional) The page number to be returned. The number 1
               represents the first page. The default value is 1.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[TopicDetail]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_topics')
        headers.update(sdk_headers)

        params = {
            'topic_filter': topic_filter,
            'per_page': per_page,
            'page': page
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/admin/topics'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_topic(self,
        topic_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get detailed information on a topic.

        Get detailed information on a topic.

        :param str topic_name: The topic name for the topic to be listed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TopicDetail` object
        """

        if topic_name is None:
            raise ValueError('topic_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_topic')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['topic_name']
        path_param_values = self.encode_path_vars(topic_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/topics/{topic_name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_topic(self,
        topic_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a topic.

        Delete a topic.

        :param str topic_name: The topic name for the topic to be listed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if topic_name is None:
            raise ValueError('topic_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_topic')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['topic_name']
        path_param_values = self.encode_path_vars(topic_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/topics/{topic_name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_topic(self,
        topic_name: str,
        *,
        new_total_partition_count: int = None,
        configs: List['ConfigUpdate'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Increase the number of partitions and/or update one or more topic configuration parameters.

        Increase the number of partitions and/or update one or more topic configuration
        parameters.

        :param str topic_name: The topic name for the topic to be listed.
        :param int new_total_partition_count: (optional) The new partition number
               to be increased.
        :param List[ConfigUpdate] configs: (optional) The config properties to be
               updated for the topic. Valid config keys are 'cleanup.policy',
               'retention.ms', 'retention.bytes', 'segment.bytes', 'segment.ms',
               'segment.index.bytes'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if topic_name is None:
            raise ValueError('topic_name must be provided')
        if configs is not None:
            configs = [convert_model(x) for x in configs]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_topic')
        headers.update(sdk_headers)

        data = {
            'new_total_partition_count': new_total_partition_count,
            'configs': configs
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['topic_name']
        path_param_values = self.encode_path_vars(topic_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/admin/topics/{topic_name}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_mirroring_topic_selection(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get current topic selection for mirroring.

        Get current topic selection for mirroring.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MirroringTopicSelection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_mirroring_topic_selection')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/admin/mirroring/topic-selection'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def replace_mirroring_topic_selection(self,
        *,
        includes: List[str] = None,
        **kwargs
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='replace_mirroring_topic_selection')
        headers.update(sdk_headers)

        data = {
            'includes': includes
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/admin/mirroring/topic-selection'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_mirroring_active_topics(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get topics that are being actively mirrored.

        Get topics that are being actively mirrored.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MirroringActiveTopics` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_mirroring_active_topics')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/admin/mirroring/active-topics'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class ReplicaAssignmentBrokers():
    """
    ReplicaAssignmentBrokers.

    :attr List[int] replicas: (optional)
    """

    def __init__(self,
                 *,
                 replicas: List[int] = None) -> None:
        """
        Initialize a ReplicaAssignmentBrokers object.

        :param List[int] replicas: (optional)
        """
        self.replicas = replicas

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicaAssignmentBrokers':
        """Initialize a ReplicaAssignmentBrokers object from a json dictionary."""
        args = {}
        if 'replicas' in _dict:
            args['replicas'] = _dict.get('replicas')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicaAssignmentBrokers object from a json dictionary."""
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
        """Return a `str` version of this ReplicaAssignmentBrokers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicaAssignmentBrokers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicaAssignmentBrokers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConfigCreate():
    """
    ConfigCreate.

    :attr str name: (optional) The name of the config property.
    :attr str value: (optional) The value for a config property.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 value: str = None) -> None:
        """
        Initialize a ConfigCreate object.

        :param str name: (optional) The name of the config property.
        :param str value: (optional) The value for a config property.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConfigCreate':
        """Initialize a ConfigCreate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConfigCreate object from a json dictionary."""
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
        """Return a `str` version of this ConfigCreate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConfigCreate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConfigCreate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConfigUpdate():
    """
    ConfigUpdate.

    :attr str name: (optional) The name of the config property.
    :attr str value: (optional) The value for a config property.
    :attr bool reset_to_default: (optional) When true, the value of the config
          property is reset to its default value.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 value: str = None,
                 reset_to_default: bool = None) -> None:
        """
        Initialize a ConfigUpdate object.

        :param str name: (optional) The name of the config property.
        :param str value: (optional) The value for a config property.
        :param bool reset_to_default: (optional) When true, the value of the config
               property is reset to its default value.
        """
        self.name = name
        self.value = value
        self.reset_to_default = reset_to_default

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConfigUpdate':
        """Initialize a ConfigUpdate object from a json dictionary."""
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
        """Initialize a ConfigUpdate object from a json dictionary."""
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
        """Return a `str` version of this ConfigUpdate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConfigUpdate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConfigUpdate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MirroringActiveTopics():
    """
    Topics that are being actively mirrored.

    :attr List[str] active_topics: (optional)
    """

    def __init__(self,
                 *,
                 active_topics: List[str] = None) -> None:
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

class MirroringTopicSelection():
    """
    Mirroring topic selection payload.

    :attr List[str] includes: (optional)
    """

    def __init__(self,
                 *,
                 includes: List[str] = None) -> None:
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

class ReplicaAssignment():
    """
    ReplicaAssignment.

    :attr int id: (optional) The ID of the partition.
    :attr ReplicaAssignmentBrokers brokers: (optional)
    """

    def __init__(self,
                 *,
                 id: int = None,
                 brokers: 'ReplicaAssignmentBrokers' = None) -> None:
        """
        Initialize a ReplicaAssignment object.

        :param int id: (optional) The ID of the partition.
        :param ReplicaAssignmentBrokers brokers: (optional)
        """
        self.id = id
        self.brokers = brokers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReplicaAssignment':
        """Initialize a ReplicaAssignment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'brokers' in _dict:
            args['brokers'] = ReplicaAssignmentBrokers.from_dict(_dict.get('brokers'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReplicaAssignment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'brokers') and self.brokers is not None:
            _dict['brokers'] = self.brokers.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReplicaAssignment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReplicaAssignment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReplicaAssignment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TopicConfigs():
    """
    TopicConfigs.

    :attr str cleanup_policy: (optional) The value of config property
          'cleanup.policy'.
    :attr str min_insync_replicas: (optional) The value of config property
          'min.insync.replicas'.
    :attr str retention_bytes: (optional) The value of config property
          'retention.bytes'.
    :attr str retention_ms: (optional) The value of config property 'retention.ms'.
    :attr str segment_bytes: (optional) The value of config property
          'segment.bytes'.
    :attr str segment_index_bytes: (optional) The value of config property
          'segment.index.bytes'.
    :attr str segment_ms: (optional) The value of config property 'segment.ms'.
    """

    def __init__(self,
                 *,
                 cleanup_policy: str = None,
                 min_insync_replicas: str = None,
                 retention_bytes: str = None,
                 retention_ms: str = None,
                 segment_bytes: str = None,
                 segment_index_bytes: str = None,
                 segment_ms: str = None) -> None:
        """
        Initialize a TopicConfigs object.

        :param str cleanup_policy: (optional) The value of config property
               'cleanup.policy'.
        :param str min_insync_replicas: (optional) The value of config property
               'min.insync.replicas'.
        :param str retention_bytes: (optional) The value of config property
               'retention.bytes'.
        :param str retention_ms: (optional) The value of config property
               'retention.ms'.
        :param str segment_bytes: (optional) The value of config property
               'segment.bytes'.
        :param str segment_index_bytes: (optional) The value of config property
               'segment.index.bytes'.
        :param str segment_ms: (optional) The value of config property
               'segment.ms'.
        """
        self.cleanup_policy = cleanup_policy
        self.min_insync_replicas = min_insync_replicas
        self.retention_bytes = retention_bytes
        self.retention_ms = retention_ms
        self.segment_bytes = segment_bytes
        self.segment_index_bytes = segment_index_bytes
        self.segment_ms = segment_ms

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TopicConfigs':
        """Initialize a TopicConfigs object from a json dictionary."""
        args = {}
        if 'cleanup.policy' in _dict:
            args['cleanup_policy'] = _dict.get('cleanup.policy')
        if 'min.insync.replicas' in _dict:
            args['min_insync_replicas'] = _dict.get('min.insync.replicas')
        if 'retention.bytes' in _dict:
            args['retention_bytes'] = _dict.get('retention.bytes')
        if 'retention.ms' in _dict:
            args['retention_ms'] = _dict.get('retention.ms')
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
        if hasattr(self, 'cleanup_policy') and self.cleanup_policy is not None:
            _dict['cleanup.policy'] = self.cleanup_policy
        if hasattr(self, 'min_insync_replicas') and self.min_insync_replicas is not None:
            _dict['min.insync.replicas'] = self.min_insync_replicas
        if hasattr(self, 'retention_bytes') and self.retention_bytes is not None:
            _dict['retention.bytes'] = self.retention_bytes
        if hasattr(self, 'retention_ms') and self.retention_ms is not None:
            _dict['retention.ms'] = self.retention_ms
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

class TopicDetail():
    """
    TopicDetail.

    :attr str name: (optional) The name of the topic.
    :attr int partitions: (optional) The number of partitions.
    :attr int replication_factor: (optional) The number of replication factor.
    :attr int retention_ms: (optional) The value of config property 'retention.ms'.
    :attr str cleanup_policy: (optional) The value of config property
          'cleanup.policy'.
    :attr TopicConfigs configs: (optional)
    :attr List[ReplicaAssignment] replica_assignments: (optional) The replia
          assignment of the topic.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 partitions: int = None,
                 replication_factor: int = None,
                 retention_ms: int = None,
                 cleanup_policy: str = None,
                 configs: 'TopicConfigs' = None,
                 replica_assignments: List['ReplicaAssignment'] = None) -> None:
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
        :param List[ReplicaAssignment] replica_assignments: (optional) The replia
               assignment of the topic.
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
            args['replica_assignments'] = [ReplicaAssignment.from_dict(x) for x in _dict.get('replicaAssignments')]
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
            _dict['configs'] = self.configs.to_dict()
        if hasattr(self, 'replica_assignments') and self.replica_assignments is not None:
            _dict['replicaAssignments'] = [x.to_dict() for x in self.replica_assignments]
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
