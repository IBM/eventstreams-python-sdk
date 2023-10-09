# -*- coding: utf-8 -*-
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

"""
Unit Tests for AdminrestV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from eventstreams_sdk.adminrest_v1 import *


_service = AdminrestV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://fake'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: CreateTopic
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = AdminrestV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AdminrestV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AdminrestV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateTopic:
    """
    Test Class for create_topic
    """

    @responses.activate
    def test_create_topic_all_params(self):
        """
        create_topic()
        """
        # Set up mock
        url = preprocess_url('/admin/topics')
        responses.add(
            responses.POST,
            url,
            status=202,
        )

        # Construct a dict representation of a TopicCreateRequestConfigsItem model
        topic_create_request_configs_item_model = {}
        topic_create_request_configs_item_model['name'] = 'testString'
        topic_create_request_configs_item_model['value'] = 'testString'

        # Set up parameter values
        name = 'testString'
        partitions = 26
        partition_count = 1
        configs = [topic_create_request_configs_item_model]

        # Invoke method
        response = _service.create_topic(
            name=name,
            partitions=partitions,
            partition_count=partition_count,
            configs=configs,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['partitions'] == 26
        assert req_body['partition_count'] == 1
        assert req_body['configs'] == [topic_create_request_configs_item_model]

    def test_create_topic_all_params_with_retries(self):
        # Enable retries and run test_create_topic_all_params.
        _service.enable_retries()
        self.test_create_topic_all_params()

        # Disable retries and run test_create_topic_all_params.
        _service.disable_retries()
        self.test_create_topic_all_params()


# endregion
##############################################################################
# End of Service: CreateTopic
##############################################################################

##############################################################################
# Start of Service: Default
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = AdminrestV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AdminrestV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AdminrestV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestAlive:
    """
    Test Class for alive
    """

    @responses.activate
    def test_alive_all_params(self):
        """
        alive()
        """
        # Set up mock
        url = preprocess_url('/alive')
        responses.add(
            responses.GET,
            url,
            status=200,
        )

        # Invoke method
        response = _service.alive()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_alive_all_params_with_retries(self):
        # Enable retries and run test_alive_all_params.
        _service.enable_retries()
        self.test_alive_all_params()

        # Disable retries and run test_alive_all_params.
        _service.disable_retries()
        self.test_alive_all_params()


class TestListTopics:
    """
    Test Class for list_topics
    """

    @responses.activate
    def test_list_topics_all_params(self):
        """
        list_topics()
        """
        # Set up mock
        url = preprocess_url('/admin/topics')
        mock_response = '[{"name": "name", "partitions": 10, "replicationFactor": 18, "retentionMs": 12, "cleanupPolicy": "cleanup_policy", "configs": {"retention.bytes": "retention_bytes", "segment.bytes": "segment_bytes", "segment.index.bytes": "segment_index_bytes", "segment.ms": "segment_ms"}, "replicaAssignments": [{"id": 2, "brokers": {"replicas": [8]}}]}]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        topic_filter = 'testString'
        per_page = 38
        page = 38

        # Invoke method
        response = _service.list_topics(
            topic_filter=topic_filter,
            per_page=per_page,
            page=page,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'topic_filter={}'.format(topic_filter) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'page={}'.format(page) in query_string

    def test_list_topics_all_params_with_retries(self):
        # Enable retries and run test_list_topics_all_params.
        _service.enable_retries()
        self.test_list_topics_all_params()

        # Disable retries and run test_list_topics_all_params.
        _service.disable_retries()
        self.test_list_topics_all_params()

    @responses.activate
    def test_list_topics_required_params(self):
        """
        test_list_topics_required_params()
        """
        # Set up mock
        url = preprocess_url('/admin/topics')
        mock_response = '[{"name": "name", "partitions": 10, "replicationFactor": 18, "retentionMs": 12, "cleanupPolicy": "cleanup_policy", "configs": {"retention.bytes": "retention_bytes", "segment.bytes": "segment_bytes", "segment.index.bytes": "segment_index_bytes", "segment.ms": "segment_ms"}, "replicaAssignments": [{"id": 2, "brokers": {"replicas": [8]}}]}]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_topics()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_topics_required_params_with_retries(self):
        # Enable retries and run test_list_topics_required_params.
        _service.enable_retries()
        self.test_list_topics_required_params()

        # Disable retries and run test_list_topics_required_params.
        _service.disable_retries()
        self.test_list_topics_required_params()


class TestGetTopic:
    """
    Test Class for get_topic
    """

    @responses.activate
    def test_get_topic_all_params(self):
        """
        get_topic()
        """
        # Set up mock
        url = preprocess_url('/admin/topics/testString')
        mock_response = '{"name": "name", "partitions": 10, "replicationFactor": 18, "retentionMs": 12, "cleanupPolicy": "cleanup_policy", "configs": {"retention.bytes": "retention_bytes", "segment.bytes": "segment_bytes", "segment.index.bytes": "segment_index_bytes", "segment.ms": "segment_ms"}, "replicaAssignments": [{"id": 2, "brokers": {"replicas": [8]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        topic_name = 'testString'

        # Invoke method
        response = _service.get_topic(
            topic_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_topic_all_params_with_retries(self):
        # Enable retries and run test_get_topic_all_params.
        _service.enable_retries()
        self.test_get_topic_all_params()

        # Disable retries and run test_get_topic_all_params.
        _service.disable_retries()
        self.test_get_topic_all_params()

    @responses.activate
    def test_get_topic_value_error(self):
        """
        test_get_topic_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/topics/testString')
        mock_response = '{"name": "name", "partitions": 10, "replicationFactor": 18, "retentionMs": 12, "cleanupPolicy": "cleanup_policy", "configs": {"retention.bytes": "retention_bytes", "segment.bytes": "segment_bytes", "segment.index.bytes": "segment_index_bytes", "segment.ms": "segment_ms"}, "replicaAssignments": [{"id": 2, "brokers": {"replicas": [8]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        topic_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "topic_name": topic_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_topic(**req_copy)

    def test_get_topic_value_error_with_retries(self):
        # Enable retries and run test_get_topic_value_error.
        _service.enable_retries()
        self.test_get_topic_value_error()

        # Disable retries and run test_get_topic_value_error.
        _service.disable_retries()
        self.test_get_topic_value_error()


class TestDeleteTopic:
    """
    Test Class for delete_topic
    """

    @responses.activate
    def test_delete_topic_all_params(self):
        """
        delete_topic()
        """
        # Set up mock
        url = preprocess_url('/admin/topics/testString')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        topic_name = 'testString'

        # Invoke method
        response = _service.delete_topic(
            topic_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_topic_all_params_with_retries(self):
        # Enable retries and run test_delete_topic_all_params.
        _service.enable_retries()
        self.test_delete_topic_all_params()

        # Disable retries and run test_delete_topic_all_params.
        _service.disable_retries()
        self.test_delete_topic_all_params()

    @responses.activate
    def test_delete_topic_value_error(self):
        """
        test_delete_topic_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/topics/testString')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        topic_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "topic_name": topic_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_topic(**req_copy)

    def test_delete_topic_value_error_with_retries(self):
        # Enable retries and run test_delete_topic_value_error.
        _service.enable_retries()
        self.test_delete_topic_value_error()

        # Disable retries and run test_delete_topic_value_error.
        _service.disable_retries()
        self.test_delete_topic_value_error()


class TestUpdateTopic:
    """
    Test Class for update_topic
    """

    @responses.activate
    def test_update_topic_all_params(self):
        """
        update_topic()
        """
        # Set up mock
        url = preprocess_url('/admin/topics/testString')
        responses.add(
            responses.PATCH,
            url,
            status=202,
        )

        # Construct a dict representation of a TopicUpdateRequestConfigsItem model
        topic_update_request_configs_item_model = {}
        topic_update_request_configs_item_model['name'] = 'testString'
        topic_update_request_configs_item_model['value'] = 'testString'
        topic_update_request_configs_item_model['reset_to_default'] = True

        # Set up parameter values
        topic_name = 'testString'
        new_total_partition_count = 38
        configs = [topic_update_request_configs_item_model]

        # Invoke method
        response = _service.update_topic(
            topic_name,
            new_total_partition_count=new_total_partition_count,
            configs=configs,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['new_total_partition_count'] == 38
        assert req_body['configs'] == [topic_update_request_configs_item_model]

    def test_update_topic_all_params_with_retries(self):
        # Enable retries and run test_update_topic_all_params.
        _service.enable_retries()
        self.test_update_topic_all_params()

        # Disable retries and run test_update_topic_all_params.
        _service.disable_retries()
        self.test_update_topic_all_params()

    @responses.activate
    def test_update_topic_value_error(self):
        """
        test_update_topic_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/topics/testString')
        responses.add(
            responses.PATCH,
            url,
            status=202,
        )

        # Construct a dict representation of a TopicUpdateRequestConfigsItem model
        topic_update_request_configs_item_model = {}
        topic_update_request_configs_item_model['name'] = 'testString'
        topic_update_request_configs_item_model['value'] = 'testString'
        topic_update_request_configs_item_model['reset_to_default'] = True

        # Set up parameter values
        topic_name = 'testString'
        new_total_partition_count = 38
        configs = [topic_update_request_configs_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "topic_name": topic_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_topic(**req_copy)

    def test_update_topic_value_error_with_retries(self):
        # Enable retries and run test_update_topic_value_error.
        _service.enable_retries()
        self.test_update_topic_value_error()

        # Disable retries and run test_update_topic_value_error.
        _service.disable_retries()
        self.test_update_topic_value_error()


class TestDeleteTopicRecords:
    """
    Test Class for delete_topic_records
    """

    @responses.activate
    def test_delete_topic_records_all_params(self):
        """
        delete_topic_records()
        """
        # Set up mock
        url = preprocess_url('/admin/topics/testString/records')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Construct a dict representation of a RecordDeleteRequestRecordsToDeleteItem model
        record_delete_request_records_to_delete_item_model = {}
        record_delete_request_records_to_delete_item_model['partition'] = 38
        record_delete_request_records_to_delete_item_model['before_offset'] = 26

        # Set up parameter values
        topic_name = 'testString'
        records_to_delete = [record_delete_request_records_to_delete_item_model]

        # Invoke method
        response = _service.delete_topic_records(
            topic_name,
            records_to_delete=records_to_delete,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['records_to_delete'] == [record_delete_request_records_to_delete_item_model]

    def test_delete_topic_records_all_params_with_retries(self):
        # Enable retries and run test_delete_topic_records_all_params.
        _service.enable_retries()
        self.test_delete_topic_records_all_params()

        # Disable retries and run test_delete_topic_records_all_params.
        _service.disable_retries()
        self.test_delete_topic_records_all_params()

    @responses.activate
    def test_delete_topic_records_value_error(self):
        """
        test_delete_topic_records_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/topics/testString/records')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Construct a dict representation of a RecordDeleteRequestRecordsToDeleteItem model
        record_delete_request_records_to_delete_item_model = {}
        record_delete_request_records_to_delete_item_model['partition'] = 38
        record_delete_request_records_to_delete_item_model['before_offset'] = 26

        # Set up parameter values
        topic_name = 'testString'
        records_to_delete = [record_delete_request_records_to_delete_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "topic_name": topic_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_topic_records(**req_copy)

    def test_delete_topic_records_value_error_with_retries(self):
        # Enable retries and run test_delete_topic_records_value_error.
        _service.enable_retries()
        self.test_delete_topic_records_value_error()

        # Disable retries and run test_delete_topic_records_value_error.
        _service.disable_retries()
        self.test_delete_topic_records_value_error()


class TestCreateQuota:
    """
    Test Class for create_quota
    """

    @responses.activate
    def test_create_quota_all_params(self):
        """
        create_quota()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas/testString')
        responses.add(
            responses.POST,
            url,
            status=202,
        )

        # Set up parameter values
        entity_name = 'testString'
        producer_byte_rate = 1024
        consumer_byte_rate = 1024

        # Invoke method
        response = _service.create_quota(
            entity_name,
            producer_byte_rate=producer_byte_rate,
            consumer_byte_rate=consumer_byte_rate,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['producer_byte_rate'] == 1024
        assert req_body['consumer_byte_rate'] == 1024

    def test_create_quota_all_params_with_retries(self):
        # Enable retries and run test_create_quota_all_params.
        _service.enable_retries()
        self.test_create_quota_all_params()

        # Disable retries and run test_create_quota_all_params.
        _service.disable_retries()
        self.test_create_quota_all_params()

    @responses.activate
    def test_create_quota_value_error(self):
        """
        test_create_quota_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas/testString')
        responses.add(
            responses.POST,
            url,
            status=202,
        )

        # Set up parameter values
        entity_name = 'testString'
        producer_byte_rate = 1024
        consumer_byte_rate = 1024

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "entity_name": entity_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_quota(**req_copy)

    def test_create_quota_value_error_with_retries(self):
        # Enable retries and run test_create_quota_value_error.
        _service.enable_retries()
        self.test_create_quota_value_error()

        # Disable retries and run test_create_quota_value_error.
        _service.disable_retries()
        self.test_create_quota_value_error()


class TestUpdateQuota:
    """
    Test Class for update_quota
    """

    @responses.activate
    def test_update_quota_all_params(self):
        """
        update_quota()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas/testString')
        responses.add(
            responses.PATCH,
            url,
            status=202,
        )

        # Set up parameter values
        entity_name = 'testString'
        producer_byte_rate = 1024
        consumer_byte_rate = 1024

        # Invoke method
        response = _service.update_quota(
            entity_name,
            producer_byte_rate=producer_byte_rate,
            consumer_byte_rate=consumer_byte_rate,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['producer_byte_rate'] == 1024
        assert req_body['consumer_byte_rate'] == 1024

    def test_update_quota_all_params_with_retries(self):
        # Enable retries and run test_update_quota_all_params.
        _service.enable_retries()
        self.test_update_quota_all_params()

        # Disable retries and run test_update_quota_all_params.
        _service.disable_retries()
        self.test_update_quota_all_params()

    @responses.activate
    def test_update_quota_value_error(self):
        """
        test_update_quota_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas/testString')
        responses.add(
            responses.PATCH,
            url,
            status=202,
        )

        # Set up parameter values
        entity_name = 'testString'
        producer_byte_rate = 1024
        consumer_byte_rate = 1024

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "entity_name": entity_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_quota(**req_copy)

    def test_update_quota_value_error_with_retries(self):
        # Enable retries and run test_update_quota_value_error.
        _service.enable_retries()
        self.test_update_quota_value_error()

        # Disable retries and run test_update_quota_value_error.
        _service.disable_retries()
        self.test_update_quota_value_error()


class TestDeleteQuota:
    """
    Test Class for delete_quota
    """

    @responses.activate
    def test_delete_quota_all_params(self):
        """
        delete_quota()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas/testString')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        entity_name = 'testString'

        # Invoke method
        response = _service.delete_quota(
            entity_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_quota_all_params_with_retries(self):
        # Enable retries and run test_delete_quota_all_params.
        _service.enable_retries()
        self.test_delete_quota_all_params()

        # Disable retries and run test_delete_quota_all_params.
        _service.disable_retries()
        self.test_delete_quota_all_params()

    @responses.activate
    def test_delete_quota_value_error(self):
        """
        test_delete_quota_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas/testString')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        entity_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "entity_name": entity_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_quota(**req_copy)

    def test_delete_quota_value_error_with_retries(self):
        # Enable retries and run test_delete_quota_value_error.
        _service.enable_retries()
        self.test_delete_quota_value_error()

        # Disable retries and run test_delete_quota_value_error.
        _service.disable_retries()
        self.test_delete_quota_value_error()


class TestGetQuota:
    """
    Test Class for get_quota
    """

    @responses.activate
    def test_get_quota_all_params(self):
        """
        get_quota()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas/testString')
        mock_response = '{"producer_byte_rate": 1024, "consumer_byte_rate": 1024}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        entity_name = 'testString'

        # Invoke method
        response = _service.get_quota(
            entity_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_quota_all_params_with_retries(self):
        # Enable retries and run test_get_quota_all_params.
        _service.enable_retries()
        self.test_get_quota_all_params()

        # Disable retries and run test_get_quota_all_params.
        _service.disable_retries()
        self.test_get_quota_all_params()

    @responses.activate
    def test_get_quota_value_error(self):
        """
        test_get_quota_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas/testString')
        mock_response = '{"producer_byte_rate": 1024, "consumer_byte_rate": 1024}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        entity_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "entity_name": entity_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_quota(**req_copy)

    def test_get_quota_value_error_with_retries(self):
        # Enable retries and run test_get_quota_value_error.
        _service.enable_retries()
        self.test_get_quota_value_error()

        # Disable retries and run test_get_quota_value_error.
        _service.disable_retries()
        self.test_get_quota_value_error()


class TestListQuotas:
    """
    Test Class for list_quotas
    """

    @responses.activate
    def test_list_quotas_all_params(self):
        """
        list_quotas()
        """
        # Set up mock
        url = preprocess_url('/admin/quotas')
        mock_response = '{"data": [{"entity_name": "entity_name", "producer_byte_rate": 18, "consumer_byte_rate": 18}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_quotas()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_quotas_all_params_with_retries(self):
        # Enable retries and run test_list_quotas_all_params.
        _service.enable_retries()
        self.test_list_quotas_all_params()

        # Disable retries and run test_list_quotas_all_params.
        _service.disable_retries()
        self.test_list_quotas_all_params()


class TestListBrokers:
    """
    Test Class for list_brokers
    """

    @responses.activate
    def test_list_brokers_all_params(self):
        """
        list_brokers()
        """
        # Set up mock
        url = preprocess_url('/admin/brokers')
        mock_response = '[{"id": 2, "host": "host", "port": 4, "rack": "rack"}]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_brokers()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_brokers_all_params_with_retries(self):
        # Enable retries and run test_list_brokers_all_params.
        _service.enable_retries()
        self.test_list_brokers_all_params()

        # Disable retries and run test_list_brokers_all_params.
        _service.disable_retries()
        self.test_list_brokers_all_params()


class TestGetBroker:
    """
    Test Class for get_broker
    """

    @responses.activate
    def test_get_broker_all_params(self):
        """
        get_broker()
        """
        # Set up mock
        url = preprocess_url('/admin/brokers/38')
        mock_response = '{"id": 2, "host": "host", "port": 4, "rack": "rack", "configs": [{"name": "name", "value": "value", "is_sensitive": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        broker_id = 38

        # Invoke method
        response = _service.get_broker(
            broker_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_broker_all_params_with_retries(self):
        # Enable retries and run test_get_broker_all_params.
        _service.enable_retries()
        self.test_get_broker_all_params()

        # Disable retries and run test_get_broker_all_params.
        _service.disable_retries()
        self.test_get_broker_all_params()

    @responses.activate
    def test_get_broker_value_error(self):
        """
        test_get_broker_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/brokers/38')
        mock_response = '{"id": 2, "host": "host", "port": 4, "rack": "rack", "configs": [{"name": "name", "value": "value", "is_sensitive": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        broker_id = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "broker_id": broker_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_broker(**req_copy)

    def test_get_broker_value_error_with_retries(self):
        # Enable retries and run test_get_broker_value_error.
        _service.enable_retries()
        self.test_get_broker_value_error()

        # Disable retries and run test_get_broker_value_error.
        _service.disable_retries()
        self.test_get_broker_value_error()


class TestGetBrokerConfig:
    """
    Test Class for get_broker_config
    """

    @responses.activate
    def test_get_broker_config_all_params(self):
        """
        get_broker_config()
        """
        # Set up mock
        url = preprocess_url('/admin/brokers/38/configs')
        mock_response = '{"id": 2, "host": "host", "port": 4, "rack": "rack", "configs": [{"name": "name", "value": "value", "is_sensitive": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        broker_id = 38
        config_filter = 'testString'
        verbose = True

        # Invoke method
        response = _service.get_broker_config(
            broker_id,
            config_filter=config_filter,
            verbose=verbose,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'config_filter={}'.format(config_filter) in query_string
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string

    def test_get_broker_config_all_params_with_retries(self):
        # Enable retries and run test_get_broker_config_all_params.
        _service.enable_retries()
        self.test_get_broker_config_all_params()

        # Disable retries and run test_get_broker_config_all_params.
        _service.disable_retries()
        self.test_get_broker_config_all_params()

    @responses.activate
    def test_get_broker_config_required_params(self):
        """
        test_get_broker_config_required_params()
        """
        # Set up mock
        url = preprocess_url('/admin/brokers/38/configs')
        mock_response = '{"id": 2, "host": "host", "port": 4, "rack": "rack", "configs": [{"name": "name", "value": "value", "is_sensitive": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        broker_id = 38

        # Invoke method
        response = _service.get_broker_config(
            broker_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_broker_config_required_params_with_retries(self):
        # Enable retries and run test_get_broker_config_required_params.
        _service.enable_retries()
        self.test_get_broker_config_required_params()

        # Disable retries and run test_get_broker_config_required_params.
        _service.disable_retries()
        self.test_get_broker_config_required_params()

    @responses.activate
    def test_get_broker_config_value_error(self):
        """
        test_get_broker_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/brokers/38/configs')
        mock_response = '{"id": 2, "host": "host", "port": 4, "rack": "rack", "configs": [{"name": "name", "value": "value", "is_sensitive": true}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        broker_id = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "broker_id": broker_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_broker_config(**req_copy)

    def test_get_broker_config_value_error_with_retries(self):
        # Enable retries and run test_get_broker_config_value_error.
        _service.enable_retries()
        self.test_get_broker_config_value_error()

        # Disable retries and run test_get_broker_config_value_error.
        _service.disable_retries()
        self.test_get_broker_config_value_error()


class TestGetCluster:
    """
    Test Class for get_cluster
    """

    @responses.activate
    def test_get_cluster_all_params(self):
        """
        get_cluster()
        """
        # Set up mock
        url = preprocess_url('/admin/cluster')
        mock_response = '{"id": "id", "controller": {"id": 2, "host": "host", "port": 4, "rack": "rack"}, "brokers": [{"id": 2, "host": "host", "port": 4, "rack": "rack"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_cluster()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_cluster_all_params_with_retries(self):
        # Enable retries and run test_get_cluster_all_params.
        _service.enable_retries()
        self.test_get_cluster_all_params()

        # Disable retries and run test_get_cluster_all_params.
        _service.disable_retries()
        self.test_get_cluster_all_params()


class TestListConsumerGroups:
    """
    Test Class for list_consumer_groups
    """

    @responses.activate
    def test_list_consumer_groups_all_params(self):
        """
        list_consumer_groups()
        """
        # Set up mock
        url = preprocess_url('/admin/consumergroups')
        mock_response = '["operation_response"]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        group_filter = 'testString'
        per_page = 38
        page = 38

        # Invoke method
        response = _service.list_consumer_groups(
            group_filter=group_filter,
            per_page=per_page,
            page=page,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'group_filter={}'.format(group_filter) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'page={}'.format(page) in query_string

    def test_list_consumer_groups_all_params_with_retries(self):
        # Enable retries and run test_list_consumer_groups_all_params.
        _service.enable_retries()
        self.test_list_consumer_groups_all_params()

        # Disable retries and run test_list_consumer_groups_all_params.
        _service.disable_retries()
        self.test_list_consumer_groups_all_params()

    @responses.activate
    def test_list_consumer_groups_required_params(self):
        """
        test_list_consumer_groups_required_params()
        """
        # Set up mock
        url = preprocess_url('/admin/consumergroups')
        mock_response = '["operation_response"]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_consumer_groups()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_consumer_groups_required_params_with_retries(self):
        # Enable retries and run test_list_consumer_groups_required_params.
        _service.enable_retries()
        self.test_list_consumer_groups_required_params()

        # Disable retries and run test_list_consumer_groups_required_params.
        _service.disable_retries()
        self.test_list_consumer_groups_required_params()


class TestGetConsumerGroup:
    """
    Test Class for get_consumer_group
    """

    @responses.activate
    def test_get_consumer_group_all_params(self):
        """
        get_consumer_group()
        """
        # Set up mock
        url = preprocess_url('/admin/consumergroups/testString')
        mock_response = '{"group_id": "group_id", "state": "state", "members": [{"consumer_id": "consumer_id", "client_id": "client_id", "host": "host", "assignments": [{"topic": "topic", "partition": 9}]}], "offsets": [{"topic": "topic", "partition": 9, "current_offset": 14, "end_offset": 10}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        group_id = 'testString'

        # Invoke method
        response = _service.get_consumer_group(
            group_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_consumer_group_all_params_with_retries(self):
        # Enable retries and run test_get_consumer_group_all_params.
        _service.enable_retries()
        self.test_get_consumer_group_all_params()

        # Disable retries and run test_get_consumer_group_all_params.
        _service.disable_retries()
        self.test_get_consumer_group_all_params()

    @responses.activate
    def test_get_consumer_group_value_error(self):
        """
        test_get_consumer_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/consumergroups/testString')
        mock_response = '{"group_id": "group_id", "state": "state", "members": [{"consumer_id": "consumer_id", "client_id": "client_id", "host": "host", "assignments": [{"topic": "topic", "partition": 9}]}], "offsets": [{"topic": "topic", "partition": 9, "current_offset": 14, "end_offset": 10}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "group_id": group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_consumer_group(**req_copy)

    def test_get_consumer_group_value_error_with_retries(self):
        # Enable retries and run test_get_consumer_group_value_error.
        _service.enable_retries()
        self.test_get_consumer_group_value_error()

        # Disable retries and run test_get_consumer_group_value_error.
        _service.disable_retries()
        self.test_get_consumer_group_value_error()


class TestDeleteConsumerGroup:
    """
    Test Class for delete_consumer_group
    """

    @responses.activate
    def test_delete_consumer_group_all_params(self):
        """
        delete_consumer_group()
        """
        # Set up mock
        url = preprocess_url('/admin/consumergroups/testString')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        group_id = 'testString'

        # Invoke method
        response = _service.delete_consumer_group(
            group_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_consumer_group_all_params_with_retries(self):
        # Enable retries and run test_delete_consumer_group_all_params.
        _service.enable_retries()
        self.test_delete_consumer_group_all_params()

        # Disable retries and run test_delete_consumer_group_all_params.
        _service.disable_retries()
        self.test_delete_consumer_group_all_params()

    @responses.activate
    def test_delete_consumer_group_value_error(self):
        """
        test_delete_consumer_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/consumergroups/testString')
        responses.add(
            responses.DELETE,
            url,
            status=202,
        )

        # Set up parameter values
        group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "group_id": group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_consumer_group(**req_copy)

    def test_delete_consumer_group_value_error_with_retries(self):
        # Enable retries and run test_delete_consumer_group_value_error.
        _service.enable_retries()
        self.test_delete_consumer_group_value_error()

        # Disable retries and run test_delete_consumer_group_value_error.
        _service.disable_retries()
        self.test_delete_consumer_group_value_error()


class TestUpdateConsumerGroup:
    """
    Test Class for update_consumer_group
    """

    @responses.activate
    def test_update_consumer_group_all_params(self):
        """
        update_consumer_group()
        """
        # Set up mock
        url = preprocess_url('/admin/consumergroups/testString')
        mock_response = '[{"topic": "topic", "partition": 9, "offset": 6}]'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        group_id = 'testString'
        topic = 'testString'
        mode = 'testString'
        value = 'testString'
        execute = True

        # Invoke method
        response = _service.update_consumer_group(
            group_id,
            topic=topic,
            mode=mode,
            value=value,
            execute=execute,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['topic'] == 'testString'
        assert req_body['mode'] == 'testString'
        assert req_body['value'] == 'testString'
        assert req_body['execute'] == True

    def test_update_consumer_group_all_params_with_retries(self):
        # Enable retries and run test_update_consumer_group_all_params.
        _service.enable_retries()
        self.test_update_consumer_group_all_params()

        # Disable retries and run test_update_consumer_group_all_params.
        _service.disable_retries()
        self.test_update_consumer_group_all_params()

    @responses.activate
    def test_update_consumer_group_value_error(self):
        """
        test_update_consumer_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/admin/consumergroups/testString')
        mock_response = '[{"topic": "topic", "partition": 9, "offset": 6}]'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        group_id = 'testString'
        topic = 'testString'
        mode = 'testString'
        value = 'testString'
        execute = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "group_id": group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_consumer_group(**req_copy)

    def test_update_consumer_group_value_error_with_retries(self):
        # Enable retries and run test_update_consumer_group_value_error.
        _service.enable_retries()
        self.test_update_consumer_group_value_error()

        # Disable retries and run test_update_consumer_group_value_error.
        _service.disable_retries()
        self.test_update_consumer_group_value_error()


class TestGetMirroringTopicSelection:
    """
    Test Class for get_mirroring_topic_selection
    """

    @responses.activate
    def test_get_mirroring_topic_selection_all_params(self):
        """
        get_mirroring_topic_selection()
        """
        # Set up mock
        url = preprocess_url('/admin/mirroring/topic-selection')
        mock_response = '{"includes": ["includes"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_mirroring_topic_selection()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_mirroring_topic_selection_all_params_with_retries(self):
        # Enable retries and run test_get_mirroring_topic_selection_all_params.
        _service.enable_retries()
        self.test_get_mirroring_topic_selection_all_params()

        # Disable retries and run test_get_mirroring_topic_selection_all_params.
        _service.disable_retries()
        self.test_get_mirroring_topic_selection_all_params()


class TestReplaceMirroringTopicSelection:
    """
    Test Class for replace_mirroring_topic_selection
    """

    @responses.activate
    def test_replace_mirroring_topic_selection_all_params(self):
        """
        replace_mirroring_topic_selection()
        """
        # Set up mock
        url = preprocess_url('/admin/mirroring/topic-selection')
        mock_response = '{"includes": ["includes"]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        includes = ['testString']

        # Invoke method
        response = _service.replace_mirroring_topic_selection(
            includes=includes,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['includes'] == ['testString']

    def test_replace_mirroring_topic_selection_all_params_with_retries(self):
        # Enable retries and run test_replace_mirroring_topic_selection_all_params.
        _service.enable_retries()
        self.test_replace_mirroring_topic_selection_all_params()

        # Disable retries and run test_replace_mirroring_topic_selection_all_params.
        _service.disable_retries()
        self.test_replace_mirroring_topic_selection_all_params()


class TestGetMirroringActiveTopics:
    """
    Test Class for get_mirroring_active_topics
    """

    @responses.activate
    def test_get_mirroring_active_topics_all_params(self):
        """
        get_mirroring_active_topics()
        """
        # Set up mock
        url = preprocess_url('/admin/mirroring/active-topics')
        mock_response = '{"active_topics": ["active_topics"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_mirroring_active_topics()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_mirroring_active_topics_all_params_with_retries(self):
        # Enable retries and run test_get_mirroring_active_topics_all_params.
        _service.enable_retries()
        self.test_get_mirroring_active_topics_all_params()

        # Disable retries and run test_get_mirroring_active_topics_all_params.
        _service.disable_retries()
        self.test_get_mirroring_active_topics_all_params()


# endregion
##############################################################################
# End of Service: Default
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_BrokerDetailConfigsItem:
    """
    Test Class for BrokerDetailConfigsItem
    """

    def test_broker_detail_configs_item_serialization(self):
        """
        Test serialization/deserialization for BrokerDetailConfigsItem
        """

        # Construct a json representation of a BrokerDetailConfigsItem model
        broker_detail_configs_item_model_json = {}
        broker_detail_configs_item_model_json['name'] = 'testString'
        broker_detail_configs_item_model_json['value'] = 'testString'
        broker_detail_configs_item_model_json['is_sensitive'] = True

        # Construct a model instance of BrokerDetailConfigsItem by calling from_dict on the json representation
        broker_detail_configs_item_model = BrokerDetailConfigsItem.from_dict(broker_detail_configs_item_model_json)
        assert broker_detail_configs_item_model != False

        # Construct a model instance of BrokerDetailConfigsItem by calling from_dict on the json representation
        broker_detail_configs_item_model_dict = BrokerDetailConfigsItem.from_dict(broker_detail_configs_item_model_json).__dict__
        broker_detail_configs_item_model2 = BrokerDetailConfigsItem(**broker_detail_configs_item_model_dict)

        # Verify the model instances are equivalent
        assert broker_detail_configs_item_model == broker_detail_configs_item_model2

        # Convert model instance back to dict and verify no loss of data
        broker_detail_configs_item_model_json2 = broker_detail_configs_item_model.to_dict()
        assert broker_detail_configs_item_model_json2 == broker_detail_configs_item_model_json


class TestModel_GroupResetResultsItem:
    """
    Test Class for GroupResetResultsItem
    """

    def test_group_reset_results_item_serialization(self):
        """
        Test serialization/deserialization for GroupResetResultsItem
        """

        # Construct a json representation of a GroupResetResultsItem model
        group_reset_results_item_model_json = {}
        group_reset_results_item_model_json['topic'] = 'testString'
        group_reset_results_item_model_json['partition'] = 38
        group_reset_results_item_model_json['offset'] = 38

        # Construct a model instance of GroupResetResultsItem by calling from_dict on the json representation
        group_reset_results_item_model = GroupResetResultsItem.from_dict(group_reset_results_item_model_json)
        assert group_reset_results_item_model != False

        # Construct a model instance of GroupResetResultsItem by calling from_dict on the json representation
        group_reset_results_item_model_dict = GroupResetResultsItem.from_dict(group_reset_results_item_model_json).__dict__
        group_reset_results_item_model2 = GroupResetResultsItem(**group_reset_results_item_model_dict)

        # Verify the model instances are equivalent
        assert group_reset_results_item_model == group_reset_results_item_model2

        # Convert model instance back to dict and verify no loss of data
        group_reset_results_item_model_json2 = group_reset_results_item_model.to_dict()
        assert group_reset_results_item_model_json2 == group_reset_results_item_model_json


class TestModel_MemberAssignmentsItem:
    """
    Test Class for MemberAssignmentsItem
    """

    def test_member_assignments_item_serialization(self):
        """
        Test serialization/deserialization for MemberAssignmentsItem
        """

        # Construct a json representation of a MemberAssignmentsItem model
        member_assignments_item_model_json = {}
        member_assignments_item_model_json['topic'] = 'testString'
        member_assignments_item_model_json['partition'] = 38

        # Construct a model instance of MemberAssignmentsItem by calling from_dict on the json representation
        member_assignments_item_model = MemberAssignmentsItem.from_dict(member_assignments_item_model_json)
        assert member_assignments_item_model != False

        # Construct a model instance of MemberAssignmentsItem by calling from_dict on the json representation
        member_assignments_item_model_dict = MemberAssignmentsItem.from_dict(member_assignments_item_model_json).__dict__
        member_assignments_item_model2 = MemberAssignmentsItem(**member_assignments_item_model_dict)

        # Verify the model instances are equivalent
        assert member_assignments_item_model == member_assignments_item_model2

        # Convert model instance back to dict and verify no loss of data
        member_assignments_item_model_json2 = member_assignments_item_model.to_dict()
        assert member_assignments_item_model_json2 == member_assignments_item_model_json


class TestModel_RecordDeleteRequestRecordsToDeleteItem:
    """
    Test Class for RecordDeleteRequestRecordsToDeleteItem
    """

    def test_record_delete_request_records_to_delete_item_serialization(self):
        """
        Test serialization/deserialization for RecordDeleteRequestRecordsToDeleteItem
        """

        # Construct a json representation of a RecordDeleteRequestRecordsToDeleteItem model
        record_delete_request_records_to_delete_item_model_json = {}
        record_delete_request_records_to_delete_item_model_json['partition'] = 38
        record_delete_request_records_to_delete_item_model_json['before_offset'] = 26

        # Construct a model instance of RecordDeleteRequestRecordsToDeleteItem by calling from_dict on the json representation
        record_delete_request_records_to_delete_item_model = RecordDeleteRequestRecordsToDeleteItem.from_dict(record_delete_request_records_to_delete_item_model_json)
        assert record_delete_request_records_to_delete_item_model != False

        # Construct a model instance of RecordDeleteRequestRecordsToDeleteItem by calling from_dict on the json representation
        record_delete_request_records_to_delete_item_model_dict = RecordDeleteRequestRecordsToDeleteItem.from_dict(record_delete_request_records_to_delete_item_model_json).__dict__
        record_delete_request_records_to_delete_item_model2 = RecordDeleteRequestRecordsToDeleteItem(**record_delete_request_records_to_delete_item_model_dict)

        # Verify the model instances are equivalent
        assert record_delete_request_records_to_delete_item_model == record_delete_request_records_to_delete_item_model2

        # Convert model instance back to dict and verify no loss of data
        record_delete_request_records_to_delete_item_model_json2 = record_delete_request_records_to_delete_item_model.to_dict()
        assert record_delete_request_records_to_delete_item_model_json2 == record_delete_request_records_to_delete_item_model_json


class TestModel_TopicCreateRequestConfigsItem:
    """
    Test Class for TopicCreateRequestConfigsItem
    """

    def test_topic_create_request_configs_item_serialization(self):
        """
        Test serialization/deserialization for TopicCreateRequestConfigsItem
        """

        # Construct a json representation of a TopicCreateRequestConfigsItem model
        topic_create_request_configs_item_model_json = {}
        topic_create_request_configs_item_model_json['name'] = 'testString'
        topic_create_request_configs_item_model_json['value'] = 'testString'

        # Construct a model instance of TopicCreateRequestConfigsItem by calling from_dict on the json representation
        topic_create_request_configs_item_model = TopicCreateRequestConfigsItem.from_dict(topic_create_request_configs_item_model_json)
        assert topic_create_request_configs_item_model != False

        # Construct a model instance of TopicCreateRequestConfigsItem by calling from_dict on the json representation
        topic_create_request_configs_item_model_dict = TopicCreateRequestConfigsItem.from_dict(topic_create_request_configs_item_model_json).__dict__
        topic_create_request_configs_item_model2 = TopicCreateRequestConfigsItem(**topic_create_request_configs_item_model_dict)

        # Verify the model instances are equivalent
        assert topic_create_request_configs_item_model == topic_create_request_configs_item_model2

        # Convert model instance back to dict and verify no loss of data
        topic_create_request_configs_item_model_json2 = topic_create_request_configs_item_model.to_dict()
        assert topic_create_request_configs_item_model_json2 == topic_create_request_configs_item_model_json


class TestModel_TopicDetailReplicaAssignmentsItem:
    """
    Test Class for TopicDetailReplicaAssignmentsItem
    """

    def test_topic_detail_replica_assignments_item_serialization(self):
        """
        Test serialization/deserialization for TopicDetailReplicaAssignmentsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        topic_detail_replica_assignments_item_brokers_model = {}  # TopicDetailReplicaAssignmentsItemBrokers
        topic_detail_replica_assignments_item_brokers_model['replicas'] = [38]

        # Construct a json representation of a TopicDetailReplicaAssignmentsItem model
        topic_detail_replica_assignments_item_model_json = {}
        topic_detail_replica_assignments_item_model_json['id'] = 38
        topic_detail_replica_assignments_item_model_json['brokers'] = topic_detail_replica_assignments_item_brokers_model

        # Construct a model instance of TopicDetailReplicaAssignmentsItem by calling from_dict on the json representation
        topic_detail_replica_assignments_item_model = TopicDetailReplicaAssignmentsItem.from_dict(topic_detail_replica_assignments_item_model_json)
        assert topic_detail_replica_assignments_item_model != False

        # Construct a model instance of TopicDetailReplicaAssignmentsItem by calling from_dict on the json representation
        topic_detail_replica_assignments_item_model_dict = TopicDetailReplicaAssignmentsItem.from_dict(topic_detail_replica_assignments_item_model_json).__dict__
        topic_detail_replica_assignments_item_model2 = TopicDetailReplicaAssignmentsItem(**topic_detail_replica_assignments_item_model_dict)

        # Verify the model instances are equivalent
        assert topic_detail_replica_assignments_item_model == topic_detail_replica_assignments_item_model2

        # Convert model instance back to dict and verify no loss of data
        topic_detail_replica_assignments_item_model_json2 = topic_detail_replica_assignments_item_model.to_dict()
        assert topic_detail_replica_assignments_item_model_json2 == topic_detail_replica_assignments_item_model_json


class TestModel_TopicDetailReplicaAssignmentsItemBrokers:
    """
    Test Class for TopicDetailReplicaAssignmentsItemBrokers
    """

    def test_topic_detail_replica_assignments_item_brokers_serialization(self):
        """
        Test serialization/deserialization for TopicDetailReplicaAssignmentsItemBrokers
        """

        # Construct a json representation of a TopicDetailReplicaAssignmentsItemBrokers model
        topic_detail_replica_assignments_item_brokers_model_json = {}
        topic_detail_replica_assignments_item_brokers_model_json['replicas'] = [38]

        # Construct a model instance of TopicDetailReplicaAssignmentsItemBrokers by calling from_dict on the json representation
        topic_detail_replica_assignments_item_brokers_model = TopicDetailReplicaAssignmentsItemBrokers.from_dict(topic_detail_replica_assignments_item_brokers_model_json)
        assert topic_detail_replica_assignments_item_brokers_model != False

        # Construct a model instance of TopicDetailReplicaAssignmentsItemBrokers by calling from_dict on the json representation
        topic_detail_replica_assignments_item_brokers_model_dict = TopicDetailReplicaAssignmentsItemBrokers.from_dict(topic_detail_replica_assignments_item_brokers_model_json).__dict__
        topic_detail_replica_assignments_item_brokers_model2 = TopicDetailReplicaAssignmentsItemBrokers(**topic_detail_replica_assignments_item_brokers_model_dict)

        # Verify the model instances are equivalent
        assert topic_detail_replica_assignments_item_brokers_model == topic_detail_replica_assignments_item_brokers_model2

        # Convert model instance back to dict and verify no loss of data
        topic_detail_replica_assignments_item_brokers_model_json2 = topic_detail_replica_assignments_item_brokers_model.to_dict()
        assert topic_detail_replica_assignments_item_brokers_model_json2 == topic_detail_replica_assignments_item_brokers_model_json


class TestModel_TopicUpdateRequestConfigsItem:
    """
    Test Class for TopicUpdateRequestConfigsItem
    """

    def test_topic_update_request_configs_item_serialization(self):
        """
        Test serialization/deserialization for TopicUpdateRequestConfigsItem
        """

        # Construct a json representation of a TopicUpdateRequestConfigsItem model
        topic_update_request_configs_item_model_json = {}
        topic_update_request_configs_item_model_json['name'] = 'testString'
        topic_update_request_configs_item_model_json['value'] = 'testString'
        topic_update_request_configs_item_model_json['reset_to_default'] = True

        # Construct a model instance of TopicUpdateRequestConfigsItem by calling from_dict on the json representation
        topic_update_request_configs_item_model = TopicUpdateRequestConfigsItem.from_dict(topic_update_request_configs_item_model_json)
        assert topic_update_request_configs_item_model != False

        # Construct a model instance of TopicUpdateRequestConfigsItem by calling from_dict on the json representation
        topic_update_request_configs_item_model_dict = TopicUpdateRequestConfigsItem.from_dict(topic_update_request_configs_item_model_json).__dict__
        topic_update_request_configs_item_model2 = TopicUpdateRequestConfigsItem(**topic_update_request_configs_item_model_dict)

        # Verify the model instances are equivalent
        assert topic_update_request_configs_item_model == topic_update_request_configs_item_model2

        # Convert model instance back to dict and verify no loss of data
        topic_update_request_configs_item_model_json2 = topic_update_request_configs_item_model.to_dict()
        assert topic_update_request_configs_item_model_json2 == topic_update_request_configs_item_model_json


class TestModel_BrokerDetail:
    """
    Test Class for BrokerDetail
    """

    def test_broker_detail_serialization(self):
        """
        Test serialization/deserialization for BrokerDetail
        """

        # Construct dict forms of any model objects needed in order to build this model.

        broker_detail_configs_item_model = {}  # BrokerDetailConfigsItem
        broker_detail_configs_item_model['name'] = 'testString'
        broker_detail_configs_item_model['value'] = 'testString'
        broker_detail_configs_item_model['is_sensitive'] = True

        # Construct a json representation of a BrokerDetail model
        broker_detail_model_json = {}
        broker_detail_model_json['id'] = 38
        broker_detail_model_json['host'] = 'testString'
        broker_detail_model_json['port'] = 38
        broker_detail_model_json['rack'] = 'testString'
        broker_detail_model_json['configs'] = [broker_detail_configs_item_model]

        # Construct a model instance of BrokerDetail by calling from_dict on the json representation
        broker_detail_model = BrokerDetail.from_dict(broker_detail_model_json)
        assert broker_detail_model != False

        # Construct a model instance of BrokerDetail by calling from_dict on the json representation
        broker_detail_model_dict = BrokerDetail.from_dict(broker_detail_model_json).__dict__
        broker_detail_model2 = BrokerDetail(**broker_detail_model_dict)

        # Verify the model instances are equivalent
        assert broker_detail_model == broker_detail_model2

        # Convert model instance back to dict and verify no loss of data
        broker_detail_model_json2 = broker_detail_model.to_dict()
        assert broker_detail_model_json2 == broker_detail_model_json


class TestModel_BrokerSummary:
    """
    Test Class for BrokerSummary
    """

    def test_broker_summary_serialization(self):
        """
        Test serialization/deserialization for BrokerSummary
        """

        # Construct a json representation of a BrokerSummary model
        broker_summary_model_json = {}
        broker_summary_model_json['id'] = 38
        broker_summary_model_json['host'] = 'testString'
        broker_summary_model_json['port'] = 38
        broker_summary_model_json['rack'] = 'testString'

        # Construct a model instance of BrokerSummary by calling from_dict on the json representation
        broker_summary_model = BrokerSummary.from_dict(broker_summary_model_json)
        assert broker_summary_model != False

        # Construct a model instance of BrokerSummary by calling from_dict on the json representation
        broker_summary_model_dict = BrokerSummary.from_dict(broker_summary_model_json).__dict__
        broker_summary_model2 = BrokerSummary(**broker_summary_model_dict)

        # Verify the model instances are equivalent
        assert broker_summary_model == broker_summary_model2

        # Convert model instance back to dict and verify no loss of data
        broker_summary_model_json2 = broker_summary_model.to_dict()
        assert broker_summary_model_json2 == broker_summary_model_json


class TestModel_Cluster:
    """
    Test Class for Cluster
    """

    def test_cluster_serialization(self):
        """
        Test serialization/deserialization for Cluster
        """

        # Construct dict forms of any model objects needed in order to build this model.

        broker_summary_model = {}  # BrokerSummary
        broker_summary_model['id'] = 38
        broker_summary_model['host'] = 'testString'
        broker_summary_model['port'] = 38
        broker_summary_model['rack'] = 'testString'

        # Construct a json representation of a Cluster model
        cluster_model_json = {}
        cluster_model_json['id'] = 'testString'
        cluster_model_json['controller'] = broker_summary_model
        cluster_model_json['brokers'] = [broker_summary_model]

        # Construct a model instance of Cluster by calling from_dict on the json representation
        cluster_model = Cluster.from_dict(cluster_model_json)
        assert cluster_model != False

        # Construct a model instance of Cluster by calling from_dict on the json representation
        cluster_model_dict = Cluster.from_dict(cluster_model_json).__dict__
        cluster_model2 = Cluster(**cluster_model_dict)

        # Verify the model instances are equivalent
        assert cluster_model == cluster_model2

        # Convert model instance back to dict and verify no loss of data
        cluster_model_json2 = cluster_model.to_dict()
        assert cluster_model_json2 == cluster_model_json


class TestModel_EntityQuotaDetail:
    """
    Test Class for EntityQuotaDetail
    """

    def test_entity_quota_detail_serialization(self):
        """
        Test serialization/deserialization for EntityQuotaDetail
        """

        # Construct a json representation of a EntityQuotaDetail model
        entity_quota_detail_model_json = {}
        entity_quota_detail_model_json['entity_name'] = 'testString'
        entity_quota_detail_model_json['producer_byte_rate'] = 26
        entity_quota_detail_model_json['consumer_byte_rate'] = 26

        # Construct a model instance of EntityQuotaDetail by calling from_dict on the json representation
        entity_quota_detail_model = EntityQuotaDetail.from_dict(entity_quota_detail_model_json)
        assert entity_quota_detail_model != False

        # Construct a model instance of EntityQuotaDetail by calling from_dict on the json representation
        entity_quota_detail_model_dict = EntityQuotaDetail.from_dict(entity_quota_detail_model_json).__dict__
        entity_quota_detail_model2 = EntityQuotaDetail(**entity_quota_detail_model_dict)

        # Verify the model instances are equivalent
        assert entity_quota_detail_model == entity_quota_detail_model2

        # Convert model instance back to dict and verify no loss of data
        entity_quota_detail_model_json2 = entity_quota_detail_model.to_dict()
        assert entity_quota_detail_model_json2 == entity_quota_detail_model_json


class TestModel_GroupDetail:
    """
    Test Class for GroupDetail
    """

    def test_group_detail_serialization(self):
        """
        Test serialization/deserialization for GroupDetail
        """

        # Construct dict forms of any model objects needed in order to build this model.

        member_assignments_item_model = {}  # MemberAssignmentsItem
        member_assignments_item_model['topic'] = 'testString'
        member_assignments_item_model['partition'] = 38

        member_model = {}  # Member
        member_model['consumer_id'] = 'testString'
        member_model['client_id'] = 'testString'
        member_model['host'] = 'testString'
        member_model['assignments'] = [member_assignments_item_model]

        topic_partition_offset_model = {}  # TopicPartitionOffset
        topic_partition_offset_model['topic'] = 'testString'
        topic_partition_offset_model['partition'] = 38
        topic_partition_offset_model['current_offset'] = 26
        topic_partition_offset_model['end_offset'] = 26

        # Construct a json representation of a GroupDetail model
        group_detail_model_json = {}
        group_detail_model_json['group_id'] = 'testString'
        group_detail_model_json['state'] = 'testString'
        group_detail_model_json['members'] = [member_model]
        group_detail_model_json['offsets'] = [topic_partition_offset_model]

        # Construct a model instance of GroupDetail by calling from_dict on the json representation
        group_detail_model = GroupDetail.from_dict(group_detail_model_json)
        assert group_detail_model != False

        # Construct a model instance of GroupDetail by calling from_dict on the json representation
        group_detail_model_dict = GroupDetail.from_dict(group_detail_model_json).__dict__
        group_detail_model2 = GroupDetail(**group_detail_model_dict)

        # Verify the model instances are equivalent
        assert group_detail_model == group_detail_model2

        # Convert model instance back to dict and verify no loss of data
        group_detail_model_json2 = group_detail_model.to_dict()
        assert group_detail_model_json2 == group_detail_model_json


class TestModel_Member:
    """
    Test Class for Member
    """

    def test_member_serialization(self):
        """
        Test serialization/deserialization for Member
        """

        # Construct dict forms of any model objects needed in order to build this model.

        member_assignments_item_model = {}  # MemberAssignmentsItem
        member_assignments_item_model['topic'] = 'testString'
        member_assignments_item_model['partition'] = 38

        # Construct a json representation of a Member model
        member_model_json = {}
        member_model_json['consumer_id'] = 'testString'
        member_model_json['client_id'] = 'testString'
        member_model_json['host'] = 'testString'
        member_model_json['assignments'] = [member_assignments_item_model]

        # Construct a model instance of Member by calling from_dict on the json representation
        member_model = Member.from_dict(member_model_json)
        assert member_model != False

        # Construct a model instance of Member by calling from_dict on the json representation
        member_model_dict = Member.from_dict(member_model_json).__dict__
        member_model2 = Member(**member_model_dict)

        # Verify the model instances are equivalent
        assert member_model == member_model2

        # Convert model instance back to dict and verify no loss of data
        member_model_json2 = member_model.to_dict()
        assert member_model_json2 == member_model_json


class TestModel_MirroringActiveTopics:
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


class TestModel_MirroringTopicSelection:
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


class TestModel_QuotaDetail:
    """
    Test Class for QuotaDetail
    """

    def test_quota_detail_serialization(self):
        """
        Test serialization/deserialization for QuotaDetail
        """

        # Construct a json representation of a QuotaDetail model
        quota_detail_model_json = {}
        quota_detail_model_json['producer_byte_rate'] = 1024
        quota_detail_model_json['consumer_byte_rate'] = 1024

        # Construct a model instance of QuotaDetail by calling from_dict on the json representation
        quota_detail_model = QuotaDetail.from_dict(quota_detail_model_json)
        assert quota_detail_model != False

        # Construct a model instance of QuotaDetail by calling from_dict on the json representation
        quota_detail_model_dict = QuotaDetail.from_dict(quota_detail_model_json).__dict__
        quota_detail_model2 = QuotaDetail(**quota_detail_model_dict)

        # Verify the model instances are equivalent
        assert quota_detail_model == quota_detail_model2

        # Convert model instance back to dict and verify no loss of data
        quota_detail_model_json2 = quota_detail_model.to_dict()
        assert quota_detail_model_json2 == quota_detail_model_json


class TestModel_QuotaList:
    """
    Test Class for QuotaList
    """

    def test_quota_list_serialization(self):
        """
        Test serialization/deserialization for QuotaList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        entity_quota_detail_model = {}  # EntityQuotaDetail
        entity_quota_detail_model['entity_name'] = 'default'
        entity_quota_detail_model['producer_byte_rate'] = 1024
        entity_quota_detail_model['consumer_byte_rate'] = 1024

        # Construct a json representation of a QuotaList model
        quota_list_model_json = {}
        quota_list_model_json['data'] = [entity_quota_detail_model]

        # Construct a model instance of QuotaList by calling from_dict on the json representation
        quota_list_model = QuotaList.from_dict(quota_list_model_json)
        assert quota_list_model != False

        # Construct a model instance of QuotaList by calling from_dict on the json representation
        quota_list_model_dict = QuotaList.from_dict(quota_list_model_json).__dict__
        quota_list_model2 = QuotaList(**quota_list_model_dict)

        # Verify the model instances are equivalent
        assert quota_list_model == quota_list_model2

        # Convert model instance back to dict and verify no loss of data
        quota_list_model_json2 = quota_list_model.to_dict()
        assert quota_list_model_json2 == quota_list_model_json


class TestModel_TopicConfigs:
    """
    Test Class for TopicConfigs
    """

    def test_topic_configs_serialization(self):
        """
        Test serialization/deserialization for TopicConfigs
        """

        # Construct a json representation of a TopicConfigs model
        topic_configs_model_json = {}
        topic_configs_model_json['retention.bytes'] = 'testString'
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


class TestModel_TopicDetail:
    """
    Test Class for TopicDetail
    """

    def test_topic_detail_serialization(self):
        """
        Test serialization/deserialization for TopicDetail
        """

        # Construct dict forms of any model objects needed in order to build this model.

        topic_configs_model = {}  # TopicConfigs
        topic_configs_model['retention.bytes'] = 'testString'
        topic_configs_model['segment.bytes'] = 'testString'
        topic_configs_model['segment.index.bytes'] = 'testString'
        topic_configs_model['segment.ms'] = 'testString'

        topic_detail_replica_assignments_item_brokers_model = {}  # TopicDetailReplicaAssignmentsItemBrokers
        topic_detail_replica_assignments_item_brokers_model['replicas'] = [38]

        topic_detail_replica_assignments_item_model = {}  # TopicDetailReplicaAssignmentsItem
        topic_detail_replica_assignments_item_model['id'] = 38
        topic_detail_replica_assignments_item_model['brokers'] = topic_detail_replica_assignments_item_brokers_model

        # Construct a json representation of a TopicDetail model
        topic_detail_model_json = {}
        topic_detail_model_json['name'] = 'testString'
        topic_detail_model_json['partitions'] = 38
        topic_detail_model_json['replicationFactor'] = 38
        topic_detail_model_json['retentionMs'] = 38
        topic_detail_model_json['cleanupPolicy'] = 'testString'
        topic_detail_model_json['configs'] = topic_configs_model
        topic_detail_model_json['replicaAssignments'] = [topic_detail_replica_assignments_item_model]

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


class TestModel_TopicPartitionOffset:
    """
    Test Class for TopicPartitionOffset
    """

    def test_topic_partition_offset_serialization(self):
        """
        Test serialization/deserialization for TopicPartitionOffset
        """

        # Construct a json representation of a TopicPartitionOffset model
        topic_partition_offset_model_json = {}
        topic_partition_offset_model_json['topic'] = 'testString'
        topic_partition_offset_model_json['partition'] = 38
        topic_partition_offset_model_json['current_offset'] = 26
        topic_partition_offset_model_json['end_offset'] = 26

        # Construct a model instance of TopicPartitionOffset by calling from_dict on the json representation
        topic_partition_offset_model = TopicPartitionOffset.from_dict(topic_partition_offset_model_json)
        assert topic_partition_offset_model != False

        # Construct a model instance of TopicPartitionOffset by calling from_dict on the json representation
        topic_partition_offset_model_dict = TopicPartitionOffset.from_dict(topic_partition_offset_model_json).__dict__
        topic_partition_offset_model2 = TopicPartitionOffset(**topic_partition_offset_model_dict)

        # Verify the model instances are equivalent
        assert topic_partition_offset_model == topic_partition_offset_model2

        # Convert model instance back to dict and verify no loss of data
        topic_partition_offset_model_json2 = topic_partition_offset_model.to_dict()
        assert topic_partition_offset_model_json2 == topic_partition_offset_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
