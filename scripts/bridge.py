#!/usr/bin/env python
import rospy
import os
import sys
from neuro_cloud.srv import call
import clientlib as bridge_client

if "CLOUD_IP" not in os.environ:
    print "Can't find environment variable CLOUD_IP."
    sys.exit(1)


cloud_ip = os.environ['CLOUD_IP']
cloud_service_port = 'http://'+ cloud_ip + ':5566'


def handle(data):
    service = data.service_name
    action = data.action_name
    url = cloud_service_port + '/cloud_service/' + service + '/' + action
    return bridge_client.cloud_service_request(url)


def bridge_server():
    rospy.init_node('bridge_server')
    rospy.Service('bridge_service', call, handle)
    print "bridge_server ready for client."
    rospy.spin()


if __name__ == "__main__":
    bridge_server()
