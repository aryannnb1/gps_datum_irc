import rospy
from robot_localization.srv import SetDatum
from geographic_msgs.msg import GeoPose

def set_datum_time(req):
    try:
        latitude = req.geo_pose.position.latitude
        longitude = req.geo_pose.position.longitude
        yaw = req.geo_pose.orientation.z
        current_time = rospy.Time.now()
        new_datum_time = current_time + rospy.Duration(5.0)
        rospy.loginfo("Setting datum time for GPS to: %s", new_datum_time)
        rospy.set_param('/robot_localization/datum_time', new_datum_time.to_sec())
        rospy.loginfo("Setting datum time for GPS based on GeoPose data")

    except Exception as e:
        rospy.logerr("Error setting datum time: %s", str(e))

    return None

if __name__ == "__main__":
    rospy.init_node("set_datum_time_server")
    rospy.Service("set_datum_time", SetDatum, set_datum_time)
    rospy.spin()
