[![Build Status](https://travis-ci.com/IBM/eventstreams-python-sdk.svg?&branch=main)](https://travis-ci.com/IBM/eventstreams-python-sdk)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
# IBM Cloud Event Streams Python SDK

## Introduction

IBM Event Streams for IBM Cloud™ is a high-throughput message bus built with Apache Kafka. 
It is optimized for event ingestion into IBM Cloud and event stream distribution between your services and applications.

Event Streams provides a REST API to help connect your existing systems to your Event Streams Kafka cluster. 
Using the API, you can integrate Event Streams with any system that supports RESTful APIs.

Documentation [IBM Cloud Eventstreams Service APIs](https://cloud.ibm.com/apidocs/event-streams).


Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [REST API documentation](#event-streams-administration-rest-api)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Eventstreams SDK Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Imported Class Name
--- | ---
[Admin Rest](https://cloud.ibm.com/apidocs/event-streams) | AdminRest

## Prerequisites

* An [IBM Cloud](https://cloud.ibm.com/registration) account.
* The [IBM Cloud CLI.](https://cloud.ibm.com/docs/cli?topic=cli-getting-started)
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* A IBM Cloud Eventstreams Instance Create one [here](https://cloud.ibm.com/registration?target=/catalog/services/event-streams)
* Python 3.6 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "eventstreams-sdk>=0.0.1"
```

or

```bash
easy_install --upgrade "eventstreams-sdk>=0.0.1"
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/eventstreams-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.com/IBM/eventstreams-python-sdk/blob/main/LICENSE).

# Event Streams Administration REST API

This REST API allows users of the
[IBM Event Streams service](https://cloud.ibm.com/docs/services/EventStreams/index.html)
to administer
[Kafka topics](#using-the-rest-api-to-administer-kafka-topics)
associated with an instance of the service. You can use this API to perform the following
operations:
  - [Create a Kafka topic](#creating-a-kafka-topic)
  - [List Kafka topics](#listing-kafka-topics)
  - [Get a Kafka topic](#getting-a-kafka-topic)
  - [Delete a Kafka topic](#deleting-a-kafka-topic)
  - [Update a Kafka topic configuration](#updating-kafka-topics-configuration)
  - [List which topics are mirrored](#list-current-mirroring-topic-selection)
  - [Replace selection of topics which are mirrored](#replace-mirroring-topic-selection)
  - [List active mirroring topics](#list-active-mirroring-topics)
  
The Admin REST API is also [documented using swagger](./admin-rest-api.yaml).

## Access control
---

All requests support below authorization methods:
 * Basic authorization with user and password. (
  For both standard, enterprise and lite plans, user is 'token', password is the API key from `ibmcloud resource service-keys` for the service instance.)
 * Bearer authorization with bearer token. (This token can be either API key or JWT token obtained from IAM upon login to IBM Cloud. Use `ibmcloud iam oauth-tokens` to retrieve the token after `ibmcloud login`)
 * `X-Auth-Token` header to be set to the API key. This header is deprecated.

##  Administration API endpoint
---
Administration API endpoint is the `kafka_admin_url` property in the service key for the service instance. This command can be used to retrieve this property.
```bash
$ibmcloud resource service-key "${service_instance_key_name}" --output json > jq -r '.[]|.credentials.kafka_admin_url'
```

## Environment Setup
In the examples you must set and export environment variables as follows:
- Either the `API_KEY` or `BEARER_TOKEN` to use for authentication.
- `KAFKA_ADMIN_URL` to point to your Eventstreams admin endpoint.

In addition, the `Content-type` header has to be set to `application/json`.

Common HTTP status codes:
- 200: Request succeeded.
- 202: Request was accepted.
- 400: Invalid request JSON.
- 401: The authentication header is not set or provided information is not valid.
- 403: Not authorized to perform the operation. Usually it means the API key used is missing a certain role. More details on what role can perform what operation refers to this [document](https://cloud.ibm.com/docs/services/EventStreams?topic=eventstreams-security).
- 404: Unable to find the topic with topic name given by user.
- 422: Semantically invalid request.
- 503: An error occurred handling the request.

Error responses carry a JSON body like the following:
```json
{"error_code":50301,"message":"Unknown Kafka Error", "incident_id": "17afe715-0ff5-4c49-9acc-a4204244a331"}
```
Error codes are of the format `HHHKK` where `HHH` is the HTTP Status Code and `KK` is the Kafka protocol error.  

For E2E debugging purposes, the transaction ID of every request is returned in the HTTP header `X-Global-Transaction-Id`.
If the header is set on the request, it will be honored. If not, it will be generated.
In the event of a non-200 error return code, the transaction ID is also returned in the JSON error response as `incident_id`.


## Using the REST API to administer Kafka topics
---

The remainder of this document describes the Python implementation of the Admin Rest SDK 
and we also provide example `example.go` to show all SDK calls in action. 

To run the example :-

Set the required environment variables
```sh
# Set you API KEY.
export API_KEY="abc123456789"

# Set the Admin Endpoint to point to your cluster.
export KAFKA_ADMIN_URL="https://xyzclustername.svc01.region.eventstreams.test.cloud.ibm.com"

```

Run the example
```sh
	python example.py
```

## REST API 
---
The following sections explain how the REST API works with examples.

### Code Setup

```python
	# Code Setup
	from typing import Set
	from ibm_cloud_sdk_core.authenticators import BasicAuthenticator
	from eventstreams_sdk.adminrest_v1 import *
	import os
	from http import HTTPStatus
	
	SERVICE_NAME = 'adminrest_v1'
	KAFKA_ADMIN_URL = os.getenv('KAFKA_ADMIN_URL')
	BEARER_TOKEN= os.getenv('BEARER_TOKEN')
	API_KEY= os.getenv('API_KEY')
	
	# End Code Setup
```


### Authentication
---
Use one of the following methods to authenticate:

- To authenticate using Basic Auth:
  Place these values into the Authorization header of the HTTP request in the form Basic <credentials> 
  where <credentials> is the username and password joined by a single colon `:` base64 encoded. 
  For example:
  ```sh
  echo -n "token:<APIKEY>" | base64
  ```

- To authenticate using a bearer token:
  To obtain your token using the IBM Cloud CLI, first log in to IBM Cloud, then run the following command:
  ```
  ibmcloud iam oauth-tokens
  ```
  Place this token in the Authorization header of the HTTP request in the form Bearer. Both API key or JWT tokens are supported.

- To authenticate directly using the api_key:
  Place the key directly as the value of the X-Auth-Token HTTP header.

#### Example

Here's an example of how to create the authenticator using either an API key or a BEARER_TOKEN

```python
	# Create Authenticator
	if not KAFKA_ADMIN_URL:
	    print("Please set env KAFKA_ADMIN_URL")
	    exit(1)
	
	if not API_KEY and not BEARER_TOKEN:
	    print("Please set either an API_KEY or a BEARER_TOKEN")
	    exit(1)
	
	if API_KEY and BEARER_TOKEN:
	    print("Please set either an API_KEY or a BEARER_TOKEN not both")
	    exit(1)
	
	if API_KEY:
	    # Create an Basic IAM authenticator.
	    authenticator = BasicAuthenticator('token', API_KEY)
	else :
	    # Create an IAM Bearer Token authenticator.
	    authenticator = BasicAuthenticator('token', BEARER_TOKEN)
	
	service = AdminrestV1(
	    authenticator = authenticator
	    )
	# End Authenticator
```


### Creating a client for the Admin REST API.
---
Create a new service object.

```python
	# Create Service
	base_url = KAFKA_ADMIN_URL
	service.set_service_url(base_url)
	# End Create Service
```


### Creating a Kafka topic
---
To create a Kafka topic the admin REST SDK issues a POST request to the /admin/topics path. 
The body of the request contains a JSON document, for example:
```json
{
    "name": "topicname",
    "partitions": 1,
    "configs": {
        "retentionMs": 86400000,
        "cleanupPolicy": "delete"
    }
}
```

The only required field is name. The partitions fields defaults to 1 if not set.

Expected HTTP status codes:

- 202: Topic creation request was accepted.
- 400: Invalid request JSON.
- 403: Not authorized to create topic.
- 422: Semantically invalid request.

If the request to create a Kafka topic succeeds then HTTP status code 202 (Accepted) is returned. If the operation fails then a HTTP status code of 422 (Un-processable Entity) is returned, and a JSON object containing additional information about the failure is returned as the body of the response.




#### Example

```python
	def create_topic(service,topic_name):
	    # Set up parameter values
	    partition_count = 1
	    configs = []
	
	    # Invoke create method.
	    try:
	        response = service.create_topic(
	            name=topic_name,
	            partition_count=partition_count,
	            configs=configs,
	        )
	        if response.status_code == HTTPStatus.ACCEPTED :  
	            print("\ttopic created: " + topic_name)
	    except:
	        print("\tError Creating Topic: " + topic_name)
	    # func.End
```



### Deleting a Kafka topic
---
To delete a Kafka topic, the admin REST SDK issues a DELETE request to the `/admin/topics/TOPICNAME`
path (where `TOPICNAME` is the name of the Kafka topic that you want to delete).

Expected return codes:
- 202: Topic deletion request was accepted.
- 403: Not authorized to delete topic.
- 404: Topic does not exist.
- 422: Semantically invalid request.
  
A 202 (Accepted) status code is returned if the REST API accepts the delete
request or status code 422 (Un-processable Entity) if the delete request is
rejected. If a delete request is rejected then the body of the HTTP response 
will contain a JSON object which provides additional information about why 
the request was rejected.

Kafka deletes topics asynchronously. Deleted topics may still appear in the
response to a [list topics request](#listing-kafka-topics) for a short period
of time after the completion of a REST request to delete the topic.

#### Example

```python
	def delete_topic(service,topic_name):
	    # Lets try to delete it.
	    try:
	        response = service.delete_topic(
	            topic_name,
	            )
	        if response.status_code == HTTPStatus.ACCEPTED: 
	            print("\ttopic deleted: "+topic_name)
	    except:
	        print("\tError Deleting Topic: " + topic_name)
	    # func.End
```


### Listing Kafka topics
---
You can list all of your Kafka topics by issuing a GET request to the
`/admin/topics` path. 

Expected status codes:
- 200: the topic list is returned as JSON in the following format:
```json
[
  {
    "name": "topic1",
    "partitions": 1,
    "retentionMs": 86400000,
    "cleanupPolicy": "delete"
  },
  { "name": "topic2",
    "partitions": 2,
    "retentionMs": 86400000,
    "cleanupPolicy": "delete"
  }
]
```

A successful response will have HTTP status code 200 (OK) and contain an
array of JSON objects, where each object represents a Kafka topic and has the
following properties:

| Property name     | Description                                             |
|-------------------|---------------------------------------------------------|
| name              | The name of the Kafka topic.                            |
| partitions        | The number of partitions of the Kafka topic.            |
| retentionsMs      | The retention period for messages on the topic (in ms). |
| cleanupPolicy     | The cleanup policy of the Kafka topic.                  |

#### Example

```python
	def list_topics(service):
	    # Set up parameter values
	    topic_filter = ''
	    # Invoke list method.
	    try:
	        response = service.list_topics(
	            topic_filter=topic_filter,
	            )
	
	        if response.status_code == HTTPStatus.OK:
	            if not response.result :
	                print("\tnothing to list")
	                return
	            for topic in response.result: 
	                 print("\t" + topic["name"])
	    except:
	        print("\tError Listing Topics")
	    # func.end
```


### Getting a Kafka topic
---
To get a Kafka topic detail information, issue a GET request to the `/admin/topics/TOPICNAME`
path (where `TOPICNAME` is the name of the Kafka topic that you want to get).  

Expected status codes
- 200: Retrieve topic details successfully in following format:
```json
{
  "name": "MYTOPIC",
  "partitions": 1,
  "replicationFactor": 3,
  "retentionMs": 86400000,
  "cleanupPolicy": "delete",
  "configs": {
    "cleanup.policy": "delete",
    "min.insync.replicas": "2",
    "retention.bytes": "1073741824",
    "retention.ms": "86400000",
    "segment.bytes": "536870912"
  },
  "replicaAssignments": [
    {
      "id": 0,
      "brokers": {
        "replicas": [
          3,
          2,
          4
        ]
      }
    }
  ]
}
```
- 403: Not authorized.
- 404: Topic does not exist.

#### Example

```python
	def topic_details(service,topic_name):
	    # Invoke get method.
	    try:
	        response = service.get_topic(
	            topic_name,
	            )
	        if response.status_code == HTTPStatus.OK:  
	            for key, value in response.result.items(): 
	                print("\t" +key + ":" + str(value) )
	    except:
	        print("\tError Getting Topic Details: " + topic_name)
	    # func.End  
```


### Updating Kafka topic's configuration
---
To increase a Kafka topic's partition number or to update a Kafka topic's configuration, issue a
`PATCH` request to `/admin/topics/TOPICNAME` with the following body:
(where TOPICNAME is the name of the Kafka topic that you want to update).
```json
{
  "new_total_partition_count": 4,
  "configs": [
    {
      "name": "cleanup.policy",
      "value": "compact"
    }
  ]
}
```
Supported configuration keys are 'cleanup.policy', 'retention.ms', 'retention.bytes', 'segment.bytes', 'segment.ms', 'segment.index.bytes'.
And partition number can only be increased, not decreased.

Expected status codes
- 202: Update topic request was accepted.
- 400: Invalid request JSON/number of partitions is invalid.
- 404: Topic specified does not exist.
- 422: Semantically invalid request.

#### Example

```python
	def update_topic(service,topic_name):
	    # Set up parameter values.
	    new_total_partition_count = 6
	    configs = []
	
	    # Invoke update method.
	    try:
	        response = service.update_topic(
	            topic_name,
	            new_total_partition_count=new_total_partition_count,
	            configs=configs,
	        )
	        if response.status_code == HTTPStatus.ACCEPTED :
	            print("\ttopic updated: "+topic_name)
	    except:
	        print("\tError Updating Topic Details: " + topic_name)
	    # func.End
```


### List current mirroring topic selection

Mirroring user controls are only available on the target cluster in a mirroring environment.

To get the current topic selection, issue an GET request to /admin/mirroring/topic-selection


Expected status codes
- 200: Retrieved topic selection successfully in following format:
```json
{
  "includes": [
    "^prefix1_.*",
    "^prefix2_.*"
  ]
}
```
- 403: Unauthorized to use mirroring user controls.
- 404: Mirroring not enabled. The mirroring user control APIs are only available on the target cluster of a mirrored pair.
- 503: An error occurred handling the request.

#### Example

```python
	def get_mirroring_topic_selection(service):
	    # Invoke get selection method.
	    try:
	        response = service.get_mirroring_topic_selection()
	        if response.status_code == HTTPStatus.OK :
	            for topic in response.result: 
	                 print("\t" + topic["name"])
	    except:
	        print("\tError Listing Mirroring Topics:")  
	    # func.End
```


### Replace selection of topics which are mirrored

Replace mirroring topic selection

Mirroring user controls are available on the target cluster in a mirroring environment.

To replace the current topic selection, issue a POST request to /admin/mirroring/topic-selection

Expected status codes

- 200: Replaced topic selection successfully. The new selection is returned in following format:
```json
{
  "includes": [
    "^prefix1_.*",
    "^prefix2_.*"
  ]
}
```
- 400: Invalid request. The request data cannot be parsed and used to replace the topic selection.
- 403: Unauthorized to use mirroring user controls.
- 404: Mirroring not enabled. The mirroring user control APIs are only available on the target cluster of a mirrored pair.
- 415: Unsupported media type. Content-Type header with application/json is required.
- 503: An error occurred handling the request.

#### Example

```python
	def replace_mirroring_topic_selection(service,topic_name):
	     # Set up parameter values
	    includes = [topic_name]    
	    # Invoke replace method.
	    try:
	        response = service.replace_mirroring_topic_selection(
	            includes=[topic_name],
	        )
	        if response.status_code == HTTPStatus.OK :
	            print("\tmirroring topic selection updated: "+includes)
	    except:
	        print("\tError Replacing Mirroring Topics:") 
	    # func.End
```


### List active mirroring topics
---
Mirroring user controls are available on the target cluster in a mirroring environment.

To get the list of currently mirrored topics, issue an GET request to /admin/mirroring/active-topics

Expected status codes

- 200: Retrieved active topics successfully in following format:
```json
{
  "active_topics": [
    "topic1",
    "topic2"
  ]
}
```
- 403: Unauthorized to use mirroring user controls.
- 404: Mirroring not enabled. The mirroring user control APIs are only available on the target cluster of a mirrored pair.
- 503: An error occurred handling the request.

#### Example

```python
	def get_list_mirroring_active_topics(service):
	    # Invoke active method.
	    try:
	        response = service.get_list_mirroring_active_topics()
	        if response.status_code == HTTPStatus.OK :
	            for topic in response.result: 
	                 print("\t" + topic["name"])
	        print("\tactive mirroring topics updated:")
	    except:
	        print("\tError Listing Active Mirroring Topics:")  
	    # func.End
```

