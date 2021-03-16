# -*- coding: utf-8 -*-
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

"""
Unit Tests for AdminrestV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ../eventstreams_sdk.adminrest_v1 import *


service = AdminrestV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://adminrest.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Default
##############################################################################
# region

class TestCreateTopic():
    """
    Test Class for create_topic
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_topic_all_params(self):
        """
        create_topic()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics')
        responses.add(responses.POST,
                      url,
                      status=202)

        # Construct a dict representation of a ConfigCreate model
        config_create_model = {}
        config_create_model['name'] = 'testString'
        config_create_model['value'] = 'testString'

        # Set up parameter values
        name = 'testString'
        partitions = 26
        partition_count = 1
        configs = [config_create_model]

        # Invoke method
        response = service.create_topic(
            name=name,
            partitions=partitions,
            partition_count=partition_count,
            configs=configs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['partitions'] == 26
        assert req_body['partition_count'] == 1
        assert req_body['configs'] == [config_create_model]


class TestListTopics():
    """
    Test Class for list_topics
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_topics_all_params(self):
        """
        list_topics()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics')
        mock_response = '[{"name": "name", "partitions": 10, "replicationFactor": 18, "retentionMs": 12, "cleanupPolicy": "cleanup_policy", "configs": {"cleanup.policy": "cleanup_policy", "min.insync.replicas": "min_insync_replicas", "retention.bytes": "retention_bytes", "retention.ms": "retention_ms", "segment.bytes": "segment_bytes", "segment.index.bytes": "segment_index_bytes", "segment.ms": "segment_ms"}, "replicaAssignments": [{"id": 2, "brokers": {"replicas": [8]}}]}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        topic_filter = 'testString'
        per_page = 38
        page = 38

        # Invoke method
        response = service.list_topics(
            topic_filter=topic_filter,
            per_page=per_page,
            page=page,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'topic_filter={}'.format(topic_filter) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'page={}'.format(page) in query_string


    @responses.activate
    def test_list_topics_required_params(self):
        """
        test_list_topics_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics')
        mock_response = '[{"name": "name", "partitions": 10, "replicationFactor": 18, "retentionMs": 12, "cleanupPolicy": "cleanup_policy", "configs": {"cleanup.policy": "cleanup_policy", "min.insync.replicas": "min_insync_replicas", "retention.bytes": "retention_bytes", "retention.ms": "retention_ms", "segment.bytes": "segment_bytes", "segment.index.bytes": "segment_index_bytes", "segment.ms": "segment_ms"}, "replicaAssignments": [{"id": 2, "brokers": {"replicas": [8]}}]}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_topics()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetTopic():
    """
    Test Class for get_topic
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_topic_all_params(self):
        """
        get_topic()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics/testString')
        mock_response = '{"name": "name", "partitions": 10, "replicationFactor": 18, "retentionMs": 12, "cleanupPolicy": "cleanup_policy", "configs": {"cleanup.policy": "cleanup_policy", "min.insync.replicas": "min_insync_replicas", "retention.bytes": "retention_bytes", "retention.ms": "retention_ms", "segment.bytes": "segment_bytes", "segment.index.bytes": "segment_index_bytes", "segment.ms": "segment_ms"}, "replicaAssignments": [{"id": 2, "brokers": {"replicas": [8]}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        topic_name = 'testString'

        # Invoke method
        response = service.get_topic(
            topic_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_topic_value_error(self):
        """
        test_get_topic_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics/testString')
        mock_response = '{"name": "name", "partitions": 10, "replicationFactor": 18, "retentionMs": 12, "cleanupPolicy": "cleanup_policy", "configs": {"cleanup.policy": "cleanup_policy", "min.insync.replicas": "min_insync_replicas", "retention.bytes": "retention_bytes", "retention.ms": "retention_ms", "segment.bytes": "segment_bytes", "segment.index.bytes": "segment_index_bytes", "segment.ms": "segment_ms"}, "replicaAssignments": [{"id": 2, "brokers": {"replicas": [8]}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        topic_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "topic_name": topic_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_topic(**req_copy)



class TestDeleteTopic():
    """
    Test Class for delete_topic
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_topic_all_params(self):
        """
        delete_topic()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics/testString')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        topic_name = 'testString'

        # Invoke method
        response = service.delete_topic(
            topic_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_delete_topic_value_error(self):
        """
        test_delete_topic_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics/testString')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        topic_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "topic_name": topic_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_topic(**req_copy)



class TestUpdateTopic():
    """
    Test Class for update_topic
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_topic_all_params(self):
        """
        update_topic()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics/testString')
        responses.add(responses.PATCH,
                      url,
                      status=202)

        # Construct a dict representation of a ConfigUpdate model
        config_update_model = {}
        config_update_model['name'] = 'testString'
        config_update_model['value'] = 'testString'
        config_update_model['reset_to_default'] = True

        # Set up parameter values
        topic_name = 'testString'
        new_total_partition_count = 38
        configs = [config_update_model]

        # Invoke method
        response = service.update_topic(
            topic_name,
            new_total_partition_count=new_total_partition_count,
            configs=configs,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['new_total_partition_count'] == 38
        assert req_body['configs'] == [config_update_model]


    @responses.activate
    def test_update_topic_value_error(self):
        """
        test_update_topic_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/topics/testString')
        responses.add(responses.PATCH,
                      url,
                      status=202)

        # Construct a dict representation of a ConfigUpdate model
        config_update_model = {}
        config_update_model['name'] = 'testString'
        config_update_model['value'] = 'testString'
        config_update_model['reset_to_default'] = True

        # Set up parameter values
        topic_name = 'testString'
        new_total_partition_count = 38
        configs = [config_update_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "topic_name": topic_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_topic(**req_copy)



class TestGetMirroringTopicSelection():
    """
    Test Class for get_mirroring_topic_selection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_mirroring_topic_selection_all_params(self):
        """
        get_mirroring_topic_selection()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/mirroring/topic-selection')
        mock_response = '{"includes": ["includes"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_mirroring_topic_selection()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestReplaceMirroringTopicSelection():
    """
    Test Class for replace_mirroring_topic_selection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_mirroring_topic_selection_all_params(self):
        """
        replace_mirroring_topic_selection()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/mirroring/topic-selection')
        mock_response = '{"includes": ["includes"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        includes = ['testString']

        # Invoke method
        response = service.replace_mirroring_topic_selection(
            includes=includes,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['includes'] == ['testString']


class TestGetMirroringActiveTopics():
    """
    Test Class for get_mirroring_active_topics
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_mirroring_active_topics_all_params(self):
        """
        get_mirroring_active_topics()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/admin/mirroring/active-topics')
        mock_response = '{"active_topics": ["active_topics"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_mirroring_active_topics()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Default
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestReplicaAssignmentBrokers():
    """
    Test Class for ReplicaAssignmentBrokers
    """

    def test_replica_assignment_brokers_serialization(self):
        """
        Test serialization/deserialization for ReplicaAssignmentBrokers
        """

        # Construct a json representation of a ReplicaAssignmentBrokers model
        replica_assignment_brokers_model_json = {}
        replica_assignment_brokers_model_json['replicas'] = [38]

        # Construct a model instance of ReplicaAssignmentBrokers by calling from_dict on the json representation
        replica_assignment_brokers_model = ReplicaAssignmentBrokers.from_dict(replica_assignment_brokers_model_json)
        assert replica_assignment_brokers_model != False

        # Construct a model instance of ReplicaAssignmentBrokers by calling from_dict on the json representation
        replica_assignment_brokers_model_dict = ReplicaAssignmentBrokers.from_dict(replica_assignment_brokers_model_json).__dict__
        replica_assignment_brokers_model2 = ReplicaAssignmentBrokers(**replica_assignment_brokers_model_dict)

        # Verify the model instances are equivalent
        assert replica_assignment_brokers_model == replica_assignment_brokers_model2

        # Convert model instance back to dict and verify no loss of data
        replica_assignment_brokers_model_json2 = replica_assignment_brokers_model.to_dict()
        assert replica_assignment_brokers_model_json2 == replica_assignment_brokers_model_json

class TestConfigCreate():
    """
    Test Class for ConfigCreate
    """

    def test_config_create_serialization(self):
        """
        Test serialization/deserialization for ConfigCreate
        """

        # Construct a json representation of a ConfigCreate model
        config_create_model_json = {}
        config_create_model_json['name'] = 'testString'
        config_create_model_json['value'] = 'testString'

        # Construct a model instance of ConfigCreate by calling from_dict on the json representation
        config_create_model = ConfigCreate.from_dict(config_create_model_json)
        assert config_create_model != False

        # Construct a model instance of ConfigCreate by calling from_dict on the json representation
        config_create_model_dict = ConfigCreate.from_dict(config_create_model_json).__dict__
        config_create_model2 = ConfigCreate(**config_create_model_dict)

        # Verify the model instances are equivalent
        assert config_create_model == config_create_model2

        # Convert model instance back to dict and verify no loss of data
        config_create_model_json2 = config_create_model.to_dict()
        assert config_create_model_json2 == config_create_model_json

class TestConfigUpdate():
    """
    Test Class for ConfigUpdate
    """

    def test_config_update_serialization(self):
        """
        Test serialization/deserialization for ConfigUpdate
        """

        # Construct a json representation of a ConfigUpdate model
        config_update_model_json = {}
        config_update_model_json['name'] = 'testString'
        config_update_model_json['value'] = 'testString'
        config_update_model_json['reset_to_default'] = True

        # Construct a model instance of ConfigUpdate by calling from_dict on the json representation
        config_update_model = ConfigUpdate.from_dict(config_update_model_json)
        assert config_update_model != False

        # Construct a model instance of ConfigUpdate by calling from_dict on the json representation
        config_update_model_dict = ConfigUpdate.from_dict(config_update_model_json).__dict__
        config_update_model2 = ConfigUpdate(**config_update_model_dict)

        # Verify the model instances are equivalent
        assert config_update_model == config_update_model2

        # Convert model instance back to dict and verify no loss of data
        config_update_model_json2 = config_update_model.to_dict()
        assert config_update_model_json2 == config_update_model_json

class TestMirroringActiveTopics():
    """
    Test Class for MirroringActiveTopics
    """

    def test_mirroring_active_topics_serialization(self):
        """
        Test serialization/deserialization for MirroringActiveTopics
        """

        # Construct a json representation of a MirroringActiveTopics model
        mirroring_active_topics_model_json = {}
        mirroring_active_topics_model_json['active_topics'] = ['testString']

        # Construct a model instance of MirroringActiveTopics by calling from_dict on the json representation
        mirroring_active_topics_model = MirroringActiveTopics.from_dict(mirroring_active_topics_model_json)
        assert mirroring_active_topics_model != False

        # Construct a model instance of MirroringActiveTopics by calling from_dict on the json representation
        mirroring_active_topics_model_dict = MirroringActiveTopics.from_dict(mirroring_active_topics_model_json).__dict__
        mirroring_active_topics_model2 = MirroringActiveTopics(**mirroring_active_topics_model_dict)

        # Verify the model instances are equivalent
        assert mirroring_active_topics_model == mirroring_active_topics_model2

        # Convert model instance back to dict and verify no loss of data
        mirroring_active_topics_model_json2 = mirroring_active_topics_model.to_dict()
        assert mirroring_active_topics_model_json2 == mirroring_active_topics_model_json

class TestMirroringTopicSelection():
    """
    Test Class for MirroringTopicSelection
    """

    def test_mirroring_topic_selection_serialization(self):
        """
        Test serialization/deserialization for MirroringTopicSelection
        """

        # Construct a json representation of a MirroringTopicSelection model
        mirroring_topic_selection_model_json = {}
        mirroring_topic_selection_model_json['includes'] = ['testString']

        # Construct a model instance of MirroringTopicSelection by calling from_dict on the json representation
        mirroring_topic_selection_model = MirroringTopicSelection.from_dict(mirroring_topic_selection_model_json)
        assert mirroring_topic_selection_model != False

        # Construct a model instance of MirroringTopicSelection by calling from_dict on the json representation
        mirroring_topic_selection_model_dict = MirroringTopicSelection.from_dict(mirroring_topic_selection_model_json).__dict__
        mirroring_topic_selection_model2 = MirroringTopicSelection(**mirroring_topic_selection_model_dict)

        # Verify the model instances are equivalent
        assert mirroring_topic_selection_model == mirroring_topic_selection_model2

        # Convert model instance back to dict and verify no loss of data
        mirroring_topic_selection_model_json2 = mirroring_topic_selection_model.to_dict()
        assert mirroring_topic_selection_model_json2 == mirroring_topic_selection_model_json

class TestReplicaAssignment():
    """
    Test Class for ReplicaAssignment
    """

    def test_replica_assignment_serialization(self):
        """
        Test serialization/deserialization for ReplicaAssignment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        replica_assignment_brokers_model = {} # ReplicaAssignmentBrokers
        replica_assignment_brokers_model['replicas'] = [38]

        # Construct a json representation of a ReplicaAssignment model
        replica_assignment_model_json = {}
        replica_assignment_model_json['id'] = 38
        replica_assignment_model_json['brokers'] = replica_assignment_brokers_model

        # Construct a model instance of ReplicaAssignment by calling from_dict on the json representation
        replica_assignment_model = ReplicaAssignment.from_dict(replica_assignment_model_json)
        assert replica_assignment_model != False

        # Construct a model instance of ReplicaAssignment by calling from_dict on the json representation
        replica_assignment_model_dict = ReplicaAssignment.from_dict(replica_assignment_model_json).__dict__
        replica_assignment_model2 = ReplicaAssignment(**replica_assignment_model_dict)

        # Verify the model instances are equivalent
        assert replica_assignment_model == replica_assignment_model2

        # Convert model instance back to dict and verify no loss of data
        replica_assignment_model_json2 = replica_assignment_model.to_dict()
        assert replica_assignment_model_json2 == replica_assignment_model_json

class TestTopicConfigs():
    """
    Test Class for TopicConfigs
    """

    def test_topic_configs_serialization(self):
        """
        Test serialization/deserialization for TopicConfigs
        """

        # Construct a json representation of a TopicConfigs model
        topic_configs_model_json = {}
        topic_configs_model_json['cleanup.policy'] = 'testString'
        topic_configs_model_json['min.insync.replicas'] = 'testString'
        topic_configs_model_json['retention.bytes'] = 'testString'
        topic_configs_model_json['retention.ms'] = 'testString'
        topic_configs_model_json['segment.bytes'] = 'testString'
        topic_configs_model_json['segment.index.bytes'] = 'testString'
        topic_configs_model_json['segment.ms'] = 'testString'

        # Construct a model instance of TopicConfigs by calling from_dict on the json representation
        topic_configs_model = TopicConfigs.from_dict(topic_configs_model_json)
        assert topic_configs_model != False

        # Construct a model instance of TopicConfigs by calling from_dict on the json representation
        topic_configs_model_dict = TopicConfigs.from_dict(topic_configs_model_json).__dict__
        topic_configs_model2 = TopicConfigs(**topic_configs_model_dict)

        # Verify the model instances are equivalent
        assert topic_configs_model == topic_configs_model2

        # Convert model instance back to dict and verify no loss of data
        topic_configs_model_json2 = topic_configs_model.to_dict()
        assert topic_configs_model_json2 == topic_configs_model_json

class TestTopicDetail():
    """
    Test Class for TopicDetail
    """

    def test_topic_detail_serialization(self):
        """
        Test serialization/deserialization for TopicDetail
        """

        # Construct dict forms of any model objects needed in order to build this model.

        topic_configs_model = {} # TopicConfigs
        topic_configs_model['cleanup.policy'] = 'testString'
        topic_configs_model['min.insync.replicas'] = 'testString'
        topic_configs_model['retention.bytes'] = 'testString'
        topic_configs_model['retention.ms'] = 'testString'
        topic_configs_model['segment.bytes'] = 'testString'
        topic_configs_model['segment.index.bytes'] = 'testString'
        topic_configs_model['segment.ms'] = 'testString'

        replica_assignment_brokers_model = {} # ReplicaAssignmentBrokers
        replica_assignment_brokers_model['replicas'] = [38]

        replica_assignment_model = {} # ReplicaAssignment
        replica_assignment_model['id'] = 38
        replica_assignment_model['brokers'] = replica_assignment_brokers_model

        # Construct a json representation of a TopicDetail model
        topic_detail_model_json = {}
        topic_detail_model_json['name'] = 'testString'
        topic_detail_model_json['partitions'] = 38
        topic_detail_model_json['replicationFactor'] = 38
        topic_detail_model_json['retentionMs'] = 38
        topic_detail_model_json['cleanupPolicy'] = 'testString'
        topic_detail_model_json['configs'] = topic_configs_model
        topic_detail_model_json['replicaAssignments'] = [replica_assignment_model]

        # Construct a model instance of TopicDetail by calling from_dict on the json representation
        topic_detail_model = TopicDetail.from_dict(topic_detail_model_json)
        assert topic_detail_model != False

        # Construct a model instance of TopicDetail by calling from_dict on the json representation
        topic_detail_model_dict = TopicDetail.from_dict(topic_detail_model_json).__dict__
        topic_detail_model2 = TopicDetail(**topic_detail_model_dict)

        # Verify the model instances are equivalent
        assert topic_detail_model == topic_detail_model2

        # Convert model instance back to dict and verify no loss of data
        topic_detail_model_json2 = topic_detail_model.to_dict()
        assert topic_detail_model_json2 == topic_detail_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
