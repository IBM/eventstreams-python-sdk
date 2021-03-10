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
Example client using IBM Event Streams SDK for Python.
"""

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

# Create Service
base_url = KAFKA_ADMIN_URL
service.set_service_url(base_url)
# End Create Service

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

# Start examples.
print("List Topics")
list_topics(service)

print("Create Topic")
create_topic(service,"test-topic")

print("Print Topic Details")
topic_details(service,"test-topic")

print("List Topics")
list_topics(service)

print("Update Topic Details")
update_topic(service,"test-topic")

print("Print Topic Details")
topic_details(service,"test-topic")

# Uncomment these examples if you are running against a Event Streams Mirrored Target Cluster.
# print("List Active Mirroring Topics\n")
# get_list_mirroring_active_topics(service)

# print("Replace Mirroring Topics\n")
# replace_mirroring_topic_selection(service,"test-topic")

# print("List Mirroring Topic Selection\n")
# get_mirroring_topic_selection(service)

print("Delete Topic")
delete_topic(service,"test-topic")

print("List Topics")
list_topics(service)

