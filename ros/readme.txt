run
    #start ros
    roscore

    #load a pcd fiel to serve
    rosrun pcl_ros pcd_to_pointcloud table_scene_lms400.pcd 1

    #empty node for processing 
    source /~/<location>/<of>/<workspace>/devel/setup.bash
    rosrun my_pcl_tutorial example

    #transform to center the pointcloud around
    rosrun tf static_transform_publisher 0 0 0 0 0 0 base_link na 1

    #visualise
    rviz