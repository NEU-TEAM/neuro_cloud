#!/usr/bin/env python
import sys
import rospy
from neuro_cloud.srv import call


def local_client(srv, act):
    rospy.wait_for_service('bridge_service')
    try:
        client = rospy.ServiceProxy('bridge_service', call)
        resp = client(srv, act)
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


if __name__ == "__main__":
    rospy.init_node('client')
    service=rospy.get_param('~service')
    action=rospy.get_param('~action')
    # srv_list = local_client('list_service', 'list')
    srv_list = ['vision', 'stereo_proc']
    if service in srv_list:
        print " %s" % (local_client(service, action))
    else:
        print "Unknown service: %s." % service
