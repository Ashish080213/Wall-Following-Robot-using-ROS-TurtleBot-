; Auto-generated. Do not edit!


(cl:in-package lab_project-msg)


;//! \htmlinclude OdomRecordResult.msg.html

(cl:defclass <OdomRecordResult> (roslisp-msg-protocol:ros-message)
  ((list_of_odoms
    :reader list_of_odoms
    :initarg :list_of_odoms
    :type (cl:vector geometry_msgs-msg:Point32)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Point32 :initial-element (cl:make-instance 'geometry_msgs-msg:Point32))))
)

(cl:defclass OdomRecordResult (<OdomRecordResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OdomRecordResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OdomRecordResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lab_project-msg:<OdomRecordResult> is deprecated: use lab_project-msg:OdomRecordResult instead.")))

(cl:ensure-generic-function 'list_of_odoms-val :lambda-list '(m))
(cl:defmethod list_of_odoms-val ((m <OdomRecordResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lab_project-msg:list_of_odoms-val is deprecated.  Use lab_project-msg:list_of_odoms instead.")
  (list_of_odoms m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OdomRecordResult>) ostream)
  "Serializes a message object of type '<OdomRecordResult>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'list_of_odoms))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'list_of_odoms))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OdomRecordResult>) istream)
  "Deserializes a message object of type '<OdomRecordResult>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'list_of_odoms) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'list_of_odoms)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Point32))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OdomRecordResult>)))
  "Returns string type for a message object of type '<OdomRecordResult>"
  "lab_project/OdomRecordResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OdomRecordResult)))
  "Returns string type for a message object of type 'OdomRecordResult"
  "lab_project/OdomRecordResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OdomRecordResult>)))
  "Returns md5sum for a message object of type '<OdomRecordResult>"
  "a23c25e5b3ba8d526c2e8cee6629770f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OdomRecordResult)))
  "Returns md5sum for a message object of type 'OdomRecordResult"
  "a23c25e5b3ba8d526c2e8cee6629770f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OdomRecordResult>)))
  "Returns full string definition for message of type '<OdomRecordResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%geometry_msgs/Point32[] list_of_odoms~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OdomRecordResult)))
  "Returns full string definition for message of type 'OdomRecordResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%geometry_msgs/Point32[] list_of_odoms~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OdomRecordResult>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'list_of_odoms) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OdomRecordResult>))
  "Converts a ROS message object to a list"
  (cl:list 'OdomRecordResult
    (cl:cons ':list_of_odoms (list_of_odoms msg))
))