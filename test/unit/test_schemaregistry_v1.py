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
Unit Tests for SchemaregistryV1
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
from eventstreams_sdk.schemaregistry_v1 import *


_service = SchemaregistryV1(
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
# Start of Service: GlobalRules
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

        service = SchemaregistryV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SchemaregistryV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SchemaregistryV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestGetGlobalRule:
    """
    Test Class for get_global_rule
    """

    @responses.activate
    def test_get_global_rule_all_params(self):
        """
        get_global_rule()
        """
        # Set up mock
        url = preprocess_url('/rules/COMPATIBILITY')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        rule = 'COMPATIBILITY'

        # Invoke method
        response = _service.get_global_rule(
            rule,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_global_rule_all_params_with_retries(self):
        # Enable retries and run test_get_global_rule_all_params.
        _service.enable_retries()
        self.test_get_global_rule_all_params()

        # Disable retries and run test_get_global_rule_all_params.
        _service.disable_retries()
        self.test_get_global_rule_all_params()

    @responses.activate
    def test_get_global_rule_value_error(self):
        """
        test_get_global_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/rules/COMPATIBILITY')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        rule = 'COMPATIBILITY'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule": rule,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_global_rule(**req_copy)

    def test_get_global_rule_value_error_with_retries(self):
        # Enable retries and run test_get_global_rule_value_error.
        _service.enable_retries()
        self.test_get_global_rule_value_error()

        # Disable retries and run test_get_global_rule_value_error.
        _service.disable_retries()
        self.test_get_global_rule_value_error()


class TestUpdateGlobalRule:
    """
    Test Class for update_global_rule
    """

    @responses.activate
    def test_update_global_rule_all_params(self):
        """
        update_global_rule()
        """
        # Set up mock
        url = preprocess_url('/rules/COMPATIBILITY')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        rule = 'COMPATIBILITY'
        type = 'COMPATIBILITY'
        config = 'BACKWARD'

        # Invoke method
        response = _service.update_global_rule(
            rule,
            type,
            config,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'COMPATIBILITY'
        assert req_body['config'] == 'BACKWARD'

    def test_update_global_rule_all_params_with_retries(self):
        # Enable retries and run test_update_global_rule_all_params.
        _service.enable_retries()
        self.test_update_global_rule_all_params()

        # Disable retries and run test_update_global_rule_all_params.
        _service.disable_retries()
        self.test_update_global_rule_all_params()

    @responses.activate
    def test_update_global_rule_value_error(self):
        """
        test_update_global_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/rules/COMPATIBILITY')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        rule = 'COMPATIBILITY'
        type = 'COMPATIBILITY'
        config = 'BACKWARD'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule": rule,
            "type": type,
            "config": config,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_global_rule(**req_copy)

    def test_update_global_rule_value_error_with_retries(self):
        # Enable retries and run test_update_global_rule_value_error.
        _service.enable_retries()
        self.test_update_global_rule_value_error()

        # Disable retries and run test_update_global_rule_value_error.
        _service.disable_retries()
        self.test_update_global_rule_value_error()


# endregion
##############################################################################
# End of Service: GlobalRules
##############################################################################

##############################################################################
# Start of Service: SchemaRules
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

        service = SchemaregistryV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SchemaregistryV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SchemaregistryV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateSchemaRule:
    """
    Test Class for create_schema_rule
    """

    @responses.activate
    def test_create_schema_rule_all_params(self):
        """
        create_schema_rule()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/rules')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        type = 'COMPATIBILITY'
        config = 'BACKWARD'

        # Invoke method
        response = _service.create_schema_rule(
            id,
            type,
            config,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'COMPATIBILITY'
        assert req_body['config'] == 'BACKWARD'

    def test_create_schema_rule_all_params_with_retries(self):
        # Enable retries and run test_create_schema_rule_all_params.
        _service.enable_retries()
        self.test_create_schema_rule_all_params()

        # Disable retries and run test_create_schema_rule_all_params.
        _service.disable_retries()
        self.test_create_schema_rule_all_params()

    @responses.activate
    def test_create_schema_rule_value_error(self):
        """
        test_create_schema_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/rules')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        type = 'COMPATIBILITY'
        config = 'BACKWARD'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "type": type,
            "config": config,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_schema_rule(**req_copy)

    def test_create_schema_rule_value_error_with_retries(self):
        # Enable retries and run test_create_schema_rule_value_error.
        _service.enable_retries()
        self.test_create_schema_rule_value_error()

        # Disable retries and run test_create_schema_rule_value_error.
        _service.disable_retries()
        self.test_create_schema_rule_value_error()


class TestGetSchemaRule:
    """
    Test Class for get_schema_rule
    """

    @responses.activate
    def test_get_schema_rule_all_params(self):
        """
        get_schema_rule()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/rules/COMPATIBILITY')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        rule = 'COMPATIBILITY'

        # Invoke method
        response = _service.get_schema_rule(
            id,
            rule,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_schema_rule_all_params_with_retries(self):
        # Enable retries and run test_get_schema_rule_all_params.
        _service.enable_retries()
        self.test_get_schema_rule_all_params()

        # Disable retries and run test_get_schema_rule_all_params.
        _service.disable_retries()
        self.test_get_schema_rule_all_params()

    @responses.activate
    def test_get_schema_rule_value_error(self):
        """
        test_get_schema_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/rules/COMPATIBILITY')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        rule = 'COMPATIBILITY'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "rule": rule,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_schema_rule(**req_copy)

    def test_get_schema_rule_value_error_with_retries(self):
        # Enable retries and run test_get_schema_rule_value_error.
        _service.enable_retries()
        self.test_get_schema_rule_value_error()

        # Disable retries and run test_get_schema_rule_value_error.
        _service.disable_retries()
        self.test_get_schema_rule_value_error()


class TestUpdateSchemaRule:
    """
    Test Class for update_schema_rule
    """

    @responses.activate
    def test_update_schema_rule_all_params(self):
        """
        update_schema_rule()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/rules/COMPATIBILITY')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        rule = 'COMPATIBILITY'
        type = 'COMPATIBILITY'
        config = 'BACKWARD'

        # Invoke method
        response = _service.update_schema_rule(
            id,
            rule,
            type,
            config,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'COMPATIBILITY'
        assert req_body['config'] == 'BACKWARD'

    def test_update_schema_rule_all_params_with_retries(self):
        # Enable retries and run test_update_schema_rule_all_params.
        _service.enable_retries()
        self.test_update_schema_rule_all_params()

        # Disable retries and run test_update_schema_rule_all_params.
        _service.disable_retries()
        self.test_update_schema_rule_all_params()

    @responses.activate
    def test_update_schema_rule_value_error(self):
        """
        test_update_schema_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/rules/COMPATIBILITY')
        mock_response = '{"type": "COMPATIBILITY", "config": "BACKWARD"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        rule = 'COMPATIBILITY'
        type = 'COMPATIBILITY'
        config = 'BACKWARD'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "rule": rule,
            "type": type,
            "config": config,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_schema_rule(**req_copy)

    def test_update_schema_rule_value_error_with_retries(self):
        # Enable retries and run test_update_schema_rule_value_error.
        _service.enable_retries()
        self.test_update_schema_rule_value_error()

        # Disable retries and run test_update_schema_rule_value_error.
        _service.disable_retries()
        self.test_update_schema_rule_value_error()


class TestDeleteSchemaRule:
    """
    Test Class for delete_schema_rule
    """

    @responses.activate
    def test_delete_schema_rule_all_params(self):
        """
        delete_schema_rule()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/rules/COMPATIBILITY')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'
        rule = 'COMPATIBILITY'

        # Invoke method
        response = _service.delete_schema_rule(
            id,
            rule,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_schema_rule_all_params_with_retries(self):
        # Enable retries and run test_delete_schema_rule_all_params.
        _service.enable_retries()
        self.test_delete_schema_rule_all_params()

        # Disable retries and run test_delete_schema_rule_all_params.
        _service.disable_retries()
        self.test_delete_schema_rule_all_params()

    @responses.activate
    def test_delete_schema_rule_value_error(self):
        """
        test_delete_schema_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/rules/COMPATIBILITY')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'
        rule = 'COMPATIBILITY'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "rule": rule,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_schema_rule(**req_copy)

    def test_delete_schema_rule_value_error_with_retries(self):
        # Enable retries and run test_delete_schema_rule_value_error.
        _service.enable_retries()
        self.test_delete_schema_rule_value_error()

        # Disable retries and run test_delete_schema_rule_value_error.
        _service.disable_retries()
        self.test_delete_schema_rule_value_error()


# endregion
##############################################################################
# End of Service: SchemaRules
##############################################################################

##############################################################################
# Start of Service: SchemaState
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

        service = SchemaregistryV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SchemaregistryV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SchemaregistryV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestSetSchemaState:
    """
    Test Class for set_schema_state
    """

    @responses.activate
    def test_set_schema_state_all_params(self):
        """
        set_schema_state()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/state')
        responses.add(
            responses.PUT,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'
        state = 'ENABLED'

        # Invoke method
        response = _service.set_schema_state(
            id,
            state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['state'] == 'ENABLED'

    def test_set_schema_state_all_params_with_retries(self):
        # Enable retries and run test_set_schema_state_all_params.
        _service.enable_retries()
        self.test_set_schema_state_all_params()

        # Disable retries and run test_set_schema_state_all_params.
        _service.disable_retries()
        self.test_set_schema_state_all_params()

    @responses.activate
    def test_set_schema_state_value_error(self):
        """
        test_set_schema_state_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/state')
        responses.add(
            responses.PUT,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'
        state = 'ENABLED'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "state": state,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_schema_state(**req_copy)

    def test_set_schema_state_value_error_with_retries(self):
        # Enable retries and run test_set_schema_state_value_error.
        _service.enable_retries()
        self.test_set_schema_state_value_error()

        # Disable retries and run test_set_schema_state_value_error.
        _service.disable_retries()
        self.test_set_schema_state_value_error()


# endregion
##############################################################################
# End of Service: SchemaState
##############################################################################

##############################################################################
# Start of Service: SchemaVersionState
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

        service = SchemaregistryV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SchemaregistryV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SchemaregistryV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestSetSchemaVersionState:
    """
    Test Class for set_schema_version_state
    """

    @responses.activate
    def test_set_schema_version_state_all_params(self):
        """
        set_schema_version_state()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions/38/state')
        responses.add(
            responses.PUT,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'
        version = 38
        state = 'ENABLED'

        # Invoke method
        response = _service.set_schema_version_state(
            id,
            version,
            state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['state'] == 'ENABLED'

    def test_set_schema_version_state_all_params_with_retries(self):
        # Enable retries and run test_set_schema_version_state_all_params.
        _service.enable_retries()
        self.test_set_schema_version_state_all_params()

        # Disable retries and run test_set_schema_version_state_all_params.
        _service.disable_retries()
        self.test_set_schema_version_state_all_params()

    @responses.activate
    def test_set_schema_version_state_value_error(self):
        """
        test_set_schema_version_state_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions/38/state')
        responses.add(
            responses.PUT,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'
        version = 38
        state = 'ENABLED'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "version": version,
            "state": state,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_schema_version_state(**req_copy)

    def test_set_schema_version_state_value_error_with_retries(self):
        # Enable retries and run test_set_schema_version_state_value_error.
        _service.enable_retries()
        self.test_set_schema_version_state_value_error()

        # Disable retries and run test_set_schema_version_state_value_error.
        _service.disable_retries()
        self.test_set_schema_version_state_value_error()


# endregion
##############################################################################
# End of Service: SchemaVersionState
##############################################################################

##############################################################################
# Start of Service: SchemaVersions
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

        service = SchemaregistryV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SchemaregistryV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SchemaregistryV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListVersions:
    """
    Test Class for list_versions
    """

    @responses.activate
    def test_list_versions_all_params(self):
        """
        list_versions()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions')
        mock_response = '[18]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        jsonformat = 'testString'

        # Invoke method
        response = _service.list_versions(
            id,
            jsonformat=jsonformat,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'jsonformat={}'.format(jsonformat) in query_string

    def test_list_versions_all_params_with_retries(self):
        # Enable retries and run test_list_versions_all_params.
        _service.enable_retries()
        self.test_list_versions_all_params()

        # Disable retries and run test_list_versions_all_params.
        _service.disable_retries()
        self.test_list_versions_all_params()

    @responses.activate
    def test_list_versions_required_params(self):
        """
        test_list_versions_required_params()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions')
        mock_response = '[18]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.list_versions(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_versions_required_params_with_retries(self):
        # Enable retries and run test_list_versions_required_params.
        _service.enable_retries()
        self.test_list_versions_required_params()

        # Disable retries and run test_list_versions_required_params.
        _service.disable_retries()
        self.test_list_versions_required_params()

    @responses.activate
    def test_list_versions_value_error(self):
        """
        test_list_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions')
        mock_response = '[18]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_versions(**req_copy)

    def test_list_versions_value_error_with_retries(self):
        # Enable retries and run test_list_versions_value_error.
        _service.enable_retries()
        self.test_list_versions_value_error()

        # Disable retries and run test_list_versions_value_error.
        _service.disable_retries()
        self.test_list_versions_value_error()


class TestCreateVersion:
    """
    Test Class for create_version
    """

    @responses.activate
    def test_create_version_all_params(self):
        """
        create_version()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions')
        mock_response = '{"createdOn": 10, "globalId": 9, "id": "id", "modifiedOn": 11, "type": "type", "version": 7}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        schema = {'anyKey': 'anyValue'}

        # Invoke method
        response = _service.create_version(
            id,
            schema=schema,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['schema'] == {'anyKey': 'anyValue'}

    def test_create_version_all_params_with_retries(self):
        # Enable retries and run test_create_version_all_params.
        _service.enable_retries()
        self.test_create_version_all_params()

        # Disable retries and run test_create_version_all_params.
        _service.disable_retries()
        self.test_create_version_all_params()

    @responses.activate
    def test_create_version_value_error(self):
        """
        test_create_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions')
        mock_response = '{"createdOn": 10, "globalId": 9, "id": "id", "modifiedOn": 11, "type": "type", "version": 7}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        schema = {'anyKey': 'anyValue'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_version(**req_copy)

    def test_create_version_value_error_with_retries(self):
        # Enable retries and run test_create_version_value_error.
        _service.enable_retries()
        self.test_create_version_value_error()

        # Disable retries and run test_create_version_value_error.
        _service.disable_retries()
        self.test_create_version_value_error()


class TestGetVersion:
    """
    Test Class for get_version
    """

    @responses.activate
    def test_get_version_all_params(self):
        """
        get_version()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions/38')
        mock_response = '{"schema": {"anyKey": "anyValue"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        version = 38

        # Invoke method
        response = _service.get_version(
            id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_version_all_params_with_retries(self):
        # Enable retries and run test_get_version_all_params.
        _service.enable_retries()
        self.test_get_version_all_params()

        # Disable retries and run test_get_version_all_params.
        _service.disable_retries()
        self.test_get_version_all_params()

    @responses.activate
    def test_get_version_value_error(self):
        """
        test_get_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions/38')
        mock_response = '{"schema": {"anyKey": "anyValue"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        version = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_version(**req_copy)

    def test_get_version_value_error_with_retries(self):
        # Enable retries and run test_get_version_value_error.
        _service.enable_retries()
        self.test_get_version_value_error()

        # Disable retries and run test_get_version_value_error.
        _service.disable_retries()
        self.test_get_version_value_error()


class TestDeleteVersion:
    """
    Test Class for delete_version
    """

    @responses.activate
    def test_delete_version_all_params(self):
        """
        delete_version()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions/38')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'
        version = 38

        # Invoke method
        response = _service.delete_version(
            id,
            version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_version_all_params_with_retries(self):
        # Enable retries and run test_delete_version_all_params.
        _service.enable_retries()
        self.test_delete_version_all_params()

        # Disable retries and run test_delete_version_all_params.
        _service.disable_retries()
        self.test_delete_version_all_params()

    @responses.activate
    def test_delete_version_value_error(self):
        """
        test_delete_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString/versions/38')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'
        version = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "version": version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_version(**req_copy)

    def test_delete_version_value_error_with_retries(self):
        # Enable retries and run test_delete_version_value_error.
        _service.enable_retries()
        self.test_delete_version_value_error()

        # Disable retries and run test_delete_version_value_error.
        _service.disable_retries()
        self.test_delete_version_value_error()


# endregion
##############################################################################
# End of Service: SchemaVersions
##############################################################################

##############################################################################
# Start of Service: Schemas
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

        service = SchemaregistryV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, SchemaregistryV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = SchemaregistryV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListSchemas:
    """
    Test Class for list_schemas
    """

    @responses.activate
    def test_list_schemas_all_params(self):
        """
        list_schemas()
        """
        # Set up mock
        url = preprocess_url('/artifacts')
        mock_response = '["operation_response"]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        jsonformat = 'testString'

        # Invoke method
        response = _service.list_schemas(
            jsonformat=jsonformat,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'jsonformat={}'.format(jsonformat) in query_string

    def test_list_schemas_all_params_with_retries(self):
        # Enable retries and run test_list_schemas_all_params.
        _service.enable_retries()
        self.test_list_schemas_all_params()

        # Disable retries and run test_list_schemas_all_params.
        _service.disable_retries()
        self.test_list_schemas_all_params()

    @responses.activate
    def test_list_schemas_required_params(self):
        """
        test_list_schemas_required_params()
        """
        # Set up mock
        url = preprocess_url('/artifacts')
        mock_response = '["operation_response"]'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_schemas()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_schemas_required_params_with_retries(self):
        # Enable retries and run test_list_schemas_required_params.
        _service.enable_retries()
        self.test_list_schemas_required_params()

        # Disable retries and run test_list_schemas_required_params.
        _service.disable_retries()
        self.test_list_schemas_required_params()


class TestCreateSchema:
    """
    Test Class for create_schema
    """

    @responses.activate
    def test_create_schema_all_params(self):
        """
        create_schema()
        """
        # Set up mock
        url = preprocess_url('/artifacts')
        mock_response = '{"createdOn": 10, "globalId": 9, "id": "id", "modifiedOn": 11, "type": "type", "version": 7}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        schema = {'anyKey': 'anyValue'}
        x_registry_artifact_id = 'testString'

        # Invoke method
        response = _service.create_schema(
            schema=schema,
            x_registry_artifact_id=x_registry_artifact_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['schema'] == {'anyKey': 'anyValue'}

    def test_create_schema_all_params_with_retries(self):
        # Enable retries and run test_create_schema_all_params.
        _service.enable_retries()
        self.test_create_schema_all_params()

        # Disable retries and run test_create_schema_all_params.
        _service.disable_retries()
        self.test_create_schema_all_params()

    @responses.activate
    def test_create_schema_required_params(self):
        """
        test_create_schema_required_params()
        """
        # Set up mock
        url = preprocess_url('/artifacts')
        mock_response = '{"createdOn": 10, "globalId": 9, "id": "id", "modifiedOn": 11, "type": "type", "version": 7}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        schema = {'anyKey': 'anyValue'}

        # Invoke method
        response = _service.create_schema(
            schema=schema,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['schema'] == {'anyKey': 'anyValue'}

    def test_create_schema_required_params_with_retries(self):
        # Enable retries and run test_create_schema_required_params.
        _service.enable_retries()
        self.test_create_schema_required_params()

        # Disable retries and run test_create_schema_required_params.
        _service.disable_retries()
        self.test_create_schema_required_params()


class TestGetLatestSchema:
    """
    Test Class for get_latest_schema
    """

    @responses.activate
    def test_get_latest_schema_all_params(self):
        """
        get_latest_schema()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString')
        mock_response = '{"schema": {"anyKey": "anyValue"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_latest_schema(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_latest_schema_all_params_with_retries(self):
        # Enable retries and run test_get_latest_schema_all_params.
        _service.enable_retries()
        self.test_get_latest_schema_all_params()

        # Disable retries and run test_get_latest_schema_all_params.
        _service.disable_retries()
        self.test_get_latest_schema_all_params()

    @responses.activate
    def test_get_latest_schema_value_error(self):
        """
        test_get_latest_schema_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString')
        mock_response = '{"schema": {"anyKey": "anyValue"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_latest_schema(**req_copy)

    def test_get_latest_schema_value_error_with_retries(self):
        # Enable retries and run test_get_latest_schema_value_error.
        _service.enable_retries()
        self.test_get_latest_schema_value_error()

        # Disable retries and run test_get_latest_schema_value_error.
        _service.disable_retries()
        self.test_get_latest_schema_value_error()


class TestDeleteSchema:
    """
    Test Class for delete_schema
    """

    @responses.activate
    def test_delete_schema_all_params(self):
        """
        delete_schema()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_schema(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_schema_all_params_with_retries(self):
        # Enable retries and run test_delete_schema_all_params.
        _service.enable_retries()
        self.test_delete_schema_all_params()

        # Disable retries and run test_delete_schema_all_params.
        _service.disable_retries()
        self.test_delete_schema_all_params()

    @responses.activate
    def test_delete_schema_value_error(self):
        """
        test_delete_schema_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_schema(**req_copy)

    def test_delete_schema_value_error_with_retries(self):
        # Enable retries and run test_delete_schema_value_error.
        _service.enable_retries()
        self.test_delete_schema_value_error()

        # Disable retries and run test_delete_schema_value_error.
        _service.disable_retries()
        self.test_delete_schema_value_error()


class TestUpdateSchema:
    """
    Test Class for update_schema
    """

    @responses.activate
    def test_update_schema_all_params(self):
        """
        update_schema()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString')
        mock_response = '{"createdOn": 10, "globalId": 9, "id": "id", "modifiedOn": 11, "type": "type", "version": 7}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        schema = {'anyKey': 'anyValue'}

        # Invoke method
        response = _service.update_schema(
            id,
            schema=schema,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['schema'] == {'anyKey': 'anyValue'}

    def test_update_schema_all_params_with_retries(self):
        # Enable retries and run test_update_schema_all_params.
        _service.enable_retries()
        self.test_update_schema_all_params()

        # Disable retries and run test_update_schema_all_params.
        _service.disable_retries()
        self.test_update_schema_all_params()

    @responses.activate
    def test_update_schema_value_error(self):
        """
        test_update_schema_value_error()
        """
        # Set up mock
        url = preprocess_url('/artifacts/testString')
        mock_response = '{"createdOn": 10, "globalId": 9, "id": "id", "modifiedOn": 11, "type": "type", "version": 7}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = 'testString'
        schema = {'anyKey': 'anyValue'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_schema(**req_copy)

    def test_update_schema_value_error_with_retries(self):
        # Enable retries and run test_update_schema_value_error.
        _service.enable_retries()
        self.test_update_schema_value_error()

        # Disable retries and run test_update_schema_value_error.
        _service.disable_retries()
        self.test_update_schema_value_error()


# endregion
##############################################################################
# End of Service: Schemas
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AvroSchema:
    """
    Test Class for AvroSchema
    """

    def test_avro_schema_serialization(self):
        """
        Test serialization/deserialization for AvroSchema
        """

        # Construct a json representation of a AvroSchema model
        avro_schema_model_json = {}
        avro_schema_model_json['schema'] = {'anyKey': 'anyValue'}

        # Construct a model instance of AvroSchema by calling from_dict on the json representation
        avro_schema_model = AvroSchema.from_dict(avro_schema_model_json)
        assert avro_schema_model != False

        # Construct a model instance of AvroSchema by calling from_dict on the json representation
        avro_schema_model_dict = AvroSchema.from_dict(avro_schema_model_json).__dict__
        avro_schema_model2 = AvroSchema(**avro_schema_model_dict)

        # Verify the model instances are equivalent
        assert avro_schema_model == avro_schema_model2

        # Convert model instance back to dict and verify no loss of data
        avro_schema_model_json2 = avro_schema_model.to_dict()
        assert avro_schema_model_json2 == avro_schema_model_json


class TestModel_Rule:
    """
    Test Class for Rule
    """

    def test_rule_serialization(self):
        """
        Test serialization/deserialization for Rule
        """

        # Construct a json representation of a Rule model
        rule_model_json = {}
        rule_model_json['type'] = 'COMPATIBILITY'
        rule_model_json['config'] = 'BACKWARD'

        # Construct a model instance of Rule by calling from_dict on the json representation
        rule_model = Rule.from_dict(rule_model_json)
        assert rule_model != False

        # Construct a model instance of Rule by calling from_dict on the json representation
        rule_model_dict = Rule.from_dict(rule_model_json).__dict__
        rule_model2 = Rule(**rule_model_dict)

        # Verify the model instances are equivalent
        assert rule_model == rule_model2

        # Convert model instance back to dict and verify no loss of data
        rule_model_json2 = rule_model.to_dict()
        assert rule_model_json2 == rule_model_json


class TestModel_SchemaMetadata:
    """
    Test Class for SchemaMetadata
    """

    def test_schema_metadata_serialization(self):
        """
        Test serialization/deserialization for SchemaMetadata
        """

        # Construct a json representation of a SchemaMetadata model
        schema_metadata_model_json = {}
        schema_metadata_model_json['createdOn'] = 38
        schema_metadata_model_json['globalId'] = 38
        schema_metadata_model_json['id'] = 'testString'
        schema_metadata_model_json['modifiedOn'] = 38
        schema_metadata_model_json['type'] = 'testString'
        schema_metadata_model_json['version'] = 38

        # Construct a model instance of SchemaMetadata by calling from_dict on the json representation
        schema_metadata_model = SchemaMetadata.from_dict(schema_metadata_model_json)
        assert schema_metadata_model != False

        # Construct a model instance of SchemaMetadata by calling from_dict on the json representation
        schema_metadata_model_dict = SchemaMetadata.from_dict(schema_metadata_model_json).__dict__
        schema_metadata_model2 = SchemaMetadata(**schema_metadata_model_dict)

        # Verify the model instances are equivalent
        assert schema_metadata_model == schema_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        schema_metadata_model_json2 = schema_metadata_model.to_dict()
        assert schema_metadata_model_json2 == schema_metadata_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
