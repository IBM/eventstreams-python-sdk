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
IBM Event Streams schema registry management

API Version: 1.3.0
"""

from enum import Enum
from typing import Dict
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class SchemaregistryV1(BaseService):
    """The schemaregistry V1 service."""

    DEFAULT_SERVICE_URL = None
    DEFAULT_SERVICE_NAME = 'schemaregistry'

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'SchemaregistryV1':
        """
        Return a new client for the schemaregistry service using the specified
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
        Construct a new client for the schemaregistry service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # globalRules
    #########################

    def get_global_rule(
        self,
        rule: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve the configuration for a global rule.

        Retrieves the configuration for the specified global rule. The value of the global
        rule is used as the _default_ when a schema does not have a corresponding schema
        compatibility rule defined.

        :param str rule: The type of the global rule to retrieve. Currently only
               `COMPATIBILITY` is supported.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not rule:
            raise ValueError('rule must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_global_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule']
        path_param_values = self.encode_path_vars(rule)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/rules/{rule}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_global_rule(
        self,
        rule: str,
        type: str,
        config: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the configuration for a global rule.

        Update the configuration for the specified global rule. The value of the global
        rule is used as the _default_ when a schema does not have a corresponding schema
        compatibility rule defined.

        :param str rule: The type of the global rule to update. Currently only
               `COMPATIBILITY` is supported.
        :param str type: The type of the rule. Currently only one type is supported
               (`COMPATIBILITY`).
        :param str config: The configuration value for the rule. Which values are
               valid depends on the value of this object's `type` property.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not rule:
            raise ValueError('rule must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if config is None:
            raise ValueError('config must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_global_rule',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'config': config,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['rule']
        path_param_values = self.encode_path_vars(rule)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/rules/{rule}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # schemaRules
    #########################

    def create_schema_rule(
        self,
        id: str,
        type: str,
        config: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a schema rule.

        Create a new rule that controls compatibility checks for a particular schema.
        Schema rules override the registries global compatibility rule setting.

        :param str id: The ID of the schema that the rule is to be associated with.
        :param str type: The type of the rule. Currently only one type is supported
               (`COMPATIBILITY`).
        :param str config: The configuration value for the rule. Which values are
               valid depends on the value of this object's `type` property.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not id:
            raise ValueError('id must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if config is None:
            raise ValueError('config must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_schema_rule',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'config': config,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/rules'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_schema_rule(
        self,
        id: str,
        rule: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a schema rule configuration.

        Retrieves the current configuration for a schema rule. If a schema rule exists
        then it overrides the corresponding global rule that would otherwise be applied.

        :param str id: The ID of the schema to retrieve the rule for.
        :param str rule: The type of rule to retrieve. Currently only the value
               that can be specified is `COMPATIBILITY`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not id:
            raise ValueError('id must be provided')
        if not rule:
            raise ValueError('rule must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_schema_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'rule']
        path_param_values = self.encode_path_vars(id, rule)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/rules/{rule}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_schema_rule(
        self,
        id: str,
        rule: str,
        type: str,
        config: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update the configuration of a schema rule.

        Updates the configuration of an existing schema rule. The updated rule will be
        applied to the specified schema, overriding the value set for the corresponding
        global rule.

        :param str id: The ID of the schema for which to update the rule
               configuration.
        :param str rule: The type of rule to update. Currently only the value that
               can be specified is `COMPATIBILITY`.
        :param str type: The type of the rule. Currently only one type is supported
               (`COMPATIBILITY`).
        :param str config: The configuration value for the rule. Which values are
               valid depends on the value of this object's `type` property.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Rule` object
        """

        if not id:
            raise ValueError('id must be provided')
        if not rule:
            raise ValueError('rule must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if config is None:
            raise ValueError('config must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_schema_rule',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'config': config,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'rule']
        path_param_values = self.encode_path_vars(id, rule)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/rules/{rule}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_schema_rule(
        self,
        id: str,
        rule: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a schema rule.

        Delete a rule that controls compatibility checks for a particular schema. After
        this operation completes the schema will be subject to compatibility checking
        defined by the global compatibility rule setting for the registry.

        :param str id: The ID of the schema that the rule is to be deleted from.
        :param str rule: The type of rule to delete. Currently only the value that
               can be specified is `COMPATIBILITY`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        if not rule:
            raise ValueError('rule must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_schema_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id', 'rule']
        path_param_values = self.encode_path_vars(id, rule)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/rules/{rule}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # schemaState
    #########################

    def set_schema_state(
        self,
        id: str,
        state: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Set schema state.

        Sets schema state.

        :param str id: The ID of a schema.
        :param str state: The state of the schema or schema version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        if state is None:
            raise ValueError('state must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='set_schema_state',
        )
        headers.update(sdk_headers)

        data = {
            'state': state,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/state'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # schemaVersionState
    #########################

    def set_schema_version_state(
        self,
        id: str,
        version: int,
        state: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Set schema version state.

        Sets schema version state.

        :param str id: The ID of a schema.
        :param int version: The version number that identifies the particular
               schema version to return.
        :param str state: The state of the schema or schema version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        if version is None:
            raise ValueError('version must be provided')
        if state is None:
            raise ValueError('state must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='set_schema_version_state',
        )
        headers.update(sdk_headers)

        data = {
            'state': state,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id', 'version']
        path_param_values = self.encode_path_vars(id, str(version))
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/versions/{version}/state'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # schemaVersions
    #########################

    def list_versions(
        self,
        id: str,
        *,
        jsonformat: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List the versions of a schema.

        Returns an array containing the version numbers of all of the versions of the
        specified schema.

        :param str id: The schema ID for which the list of versions will be
               returned.
        :param str jsonformat: (optional) format of the response to be returned,
               allowed values are 'number' and 'object'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[int]` result
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_versions',
        )
        headers.update(sdk_headers)

        params = {
            'jsonformat': jsonformat,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_version(
        self,
        id: str,
        *,
        schema: dict = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new schema version.

        Creates a new version of a schema using the AVRO schema supplied in the request
        body.

        :param str id: A schema ID. This identifies the schema for which a new
               version will be created.
        :param dict schema: (optional) The AVRO schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchemaMetadata` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_version',
        )
        headers.update(sdk_headers)

        data = {
            'schema': schema,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_version(
        self,
        id: str,
        version: int,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a version of the schema.

        Retrieve a particular version of the schema.

        :param str id: The schema ID identifying which schema to return a version
               from.
        :param int version: The version number that identifies the particular
               schema version to return.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AvroSchema` object
        """

        if not id:
            raise ValueError('id must be provided')
        if version is None:
            raise ValueError('version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'version']
        path_param_values = self.encode_path_vars(id, str(version))
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/versions/{version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_version(
        self,
        id: str,
        version: int,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a version of the schema.

        Delete a version of the schema. If this was the only version of the schema then
        the whole schema will be deleted.

        :param str id: A schema ID that identifies the schema to delete a version
               from.
        :param int version: The schema version number to delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        if version is None:
            raise ValueError('version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id', 'version']
        path_param_values = self.encode_path_vars(id, str(version))
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}/versions/{version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # schemas
    #########################

    def list_schemas(
        self,
        *,
        jsonformat: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List schema IDs.

        Returns an array containing the schema IDs of all of the schemas that are stored
        in the registry.

        :param str jsonformat: (optional) format of the response to be returned,
               allowed values are 'string' and 'object'.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[str]` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_schemas',
        )
        headers.update(sdk_headers)

        params = {
            'jsonformat': jsonformat,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/artifacts'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_schema(
        self,
        *,
        schema: dict = None,
        x_registry_artifact_id: str = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a new schema.

        Create a new schema and populate it with an initial schema version containing the
        AVRO document in the request body.

        :param dict schema: (optional) The AVRO schema.
        :param str x_registry_artifact_id: (optional) The name to assign to the new
               schema. This must be unique. If this value is not specified then a UUID is
               used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchemaMetadata` object
        """

        headers = {
            'X-Registry-ArtifactId': x_registry_artifact_id,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_schema',
        )
        headers.update(sdk_headers)

        data = {
            'schema': schema,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/artifacts'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_latest_schema(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get the latest version of a schema.

        Retrieves the lastest version of the specified schema.

        :param str id: The ID of a schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AvroSchema` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_latest_schema',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_schema(
        self,
        id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a schema.

        Deletes a schema and all of its versions from the schema registry.

        :param str id: The ID of the schema to delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_schema',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_schema(
        self,
        id: str,
        *,
        schema: dict = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a schema.

        Updates a schema.

        :param str id: The ID of the schema to update.
        :param dict schema: (optional) The AVRO schema.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SchemaMetadata` object
        """

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_schema',
        )
        headers.update(sdk_headers)

        data = {
            'schema': schema,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/artifacts/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


class GetGlobalRuleEnums:
    """
    Enums for get_global_rule parameters.
    """

    class Rule(str, Enum):
        """
        The type of the global rule to retrieve. Currently only `COMPATIBILITY` is
        supported.
        """

        COMPATIBILITY = 'COMPATIBILITY'


class UpdateGlobalRuleEnums:
    """
    Enums for update_global_rule parameters.
    """

    class Rule(str, Enum):
        """
        The type of the global rule to update. Currently only `COMPATIBILITY` is
        supported.
        """

        COMPATIBILITY = 'COMPATIBILITY'


class GetSchemaRuleEnums:
    """
    Enums for get_schema_rule parameters.
    """

    class Rule(str, Enum):
        """
        The type of rule to retrieve. Currently only the value that can be specified is
        `COMPATIBILITY`.
        """

        COMPATIBILITY = 'COMPATIBILITY'


class UpdateSchemaRuleEnums:
    """
    Enums for update_schema_rule parameters.
    """

    class Rule(str, Enum):
        """
        The type of rule to update. Currently only the value that can be specified is
        `COMPATIBILITY`.
        """

        COMPATIBILITY = 'COMPATIBILITY'


class DeleteSchemaRuleEnums:
    """
    Enums for delete_schema_rule parameters.
    """

    class Rule(str, Enum):
        """
        The type of rule to delete. Currently only the value that can be specified is
        `COMPATIBILITY`.
        """

        COMPATIBILITY = 'COMPATIBILITY'


##############################################################################
# Models
##############################################################################


class AvroSchema:
    """
    AvroSchema.

    :attr dict schema: (optional) The AVRO schema.
    """

    def __init__(
        self,
        *,
        schema: dict = None,
    ) -> None:
        """
        Initialize a AvroSchema object.

        :param dict schema: (optional) The AVRO schema.
        """
        self.schema = schema

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AvroSchema':
        """Initialize a AvroSchema object from a json dictionary."""
        args = {}
        if 'schema' in _dict:
            args['schema'] = _dict.get('schema')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AvroSchema object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'schema') and self.schema is not None:
            _dict['schema'] = self.schema
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AvroSchema object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AvroSchema') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AvroSchema') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Rule:
    """
    Rules define constraints on whether the schema registry will accept a new version of a
    schema.

    :attr str type: The type of the rule. Currently only one type is supported
          (`COMPATIBILITY`).
    :attr str config: The configuration value for the rule. Which values are valid
          depends on the value of this object's `type` property.
    """

    def __init__(
        self,
        type: str,
        config: str,
    ) -> None:
        """
        Initialize a Rule object.

        :param str type: The type of the rule. Currently only one type is supported
               (`COMPATIBILITY`).
        :param str config: The configuration value for the rule. Which values are
               valid depends on the value of this object's `type` property.
        """
        self.type = type
        self.config = config

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Rule':
        """Initialize a Rule object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in Rule JSON')
        if 'config' in _dict:
            args['config'] = _dict.get('config')
        else:
            raise ValueError('Required property \'config\' not present in Rule JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Rule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'config') and self.config is not None:
            _dict['config'] = self.config
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Rule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Rule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Rule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of the rule. Currently only one type is supported (`COMPATIBILITY`).
        """

        COMPATIBILITY = 'COMPATIBILITY'


    class ConfigEnum(str, Enum):
        """
        The configuration value for the rule. Which values are valid depends on the value
        of this object's `type` property.
        """

        BACKWARD = 'BACKWARD'
        BACKWARD_TRANSITIVE = 'BACKWARD_TRANSITIVE'
        FORWARD = 'FORWARD'
        FORWARD_TRANSITIVE = 'FORWARD_TRANSITIVE'
        FULL = 'FULL'
        FULL_TRANSITIVE = 'FULL_TRANSITIVE'
        NONE = 'NONE'



class SchemaMetadata:
    """
    Information about a schema version.

    :attr int created_on: Creation timestamp of the schema in UNIX epoc format.
    :attr int global_id: Globally unique ID assigned to the initial version of the
          schema.
    :attr str id: The ID of the schema. This is either taken from the
          `X-Registry-ArtifactId` header when the request is made to create the schema or
          is an automatically assigned UUID value.
    :attr int modified_on: Last modification timestamp of the schema in UNIX epoc
          format.
    :attr str type: Type of the schema. Always the string `AVRO`.
    :attr int version: Version number assigned to this version of the schema.
    """

    def __init__(
        self,
        created_on: int,
        global_id: int,
        id: str,
        modified_on: int,
        type: str,
        version: int,
    ) -> None:
        """
        Initialize a SchemaMetadata object.

        :param int created_on: Creation timestamp of the schema in UNIX epoc
               format.
        :param int global_id: Globally unique ID assigned to the initial version of
               the schema.
        :param str id: The ID of the schema. This is either taken from the
               `X-Registry-ArtifactId` header when the request is made to create the
               schema or is an automatically assigned UUID value.
        :param int modified_on: Last modification timestamp of the schema in UNIX
               epoc format.
        :param str type: Type of the schema. Always the string `AVRO`.
        :param int version: Version number assigned to this version of the schema.
        """
        self.created_on = created_on
        self.global_id = global_id
        self.id = id
        self.modified_on = modified_on
        self.type = type
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SchemaMetadata':
        """Initialize a SchemaMetadata object from a json dictionary."""
        args = {}
        if 'createdOn' in _dict:
            args['created_on'] = _dict.get('createdOn')
        else:
            raise ValueError('Required property \'createdOn\' not present in SchemaMetadata JSON')
        if 'globalId' in _dict:
            args['global_id'] = _dict.get('globalId')
        else:
            raise ValueError('Required property \'globalId\' not present in SchemaMetadata JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in SchemaMetadata JSON')
        if 'modifiedOn' in _dict:
            args['modified_on'] = _dict.get('modifiedOn')
        else:
            raise ValueError('Required property \'modifiedOn\' not present in SchemaMetadata JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in SchemaMetadata JSON')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        else:
            raise ValueError('Required property \'version\' not present in SchemaMetadata JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SchemaMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['createdOn'] = self.created_on
        if hasattr(self, 'global_id') and self.global_id is not None:
            _dict['globalId'] = self.global_id
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modifiedOn'] = self.modified_on
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SchemaMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SchemaMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SchemaMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
