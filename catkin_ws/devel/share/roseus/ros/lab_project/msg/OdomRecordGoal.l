;; Auto-generated. Do not edit!


(when (boundp 'lab_project::OdomRecordGoal)
  (if (not (find-package "LAB_PROJECT"))
    (make-package "LAB_PROJECT"))
  (shadow 'OdomRecordGoal (find-package "LAB_PROJECT")))
(unless (find-package "LAB_PROJECT::ODOMRECORDGOAL")
  (make-package "LAB_PROJECT::ODOMRECORDGOAL"))

(in-package "ROS")
;;//! \htmlinclude OdomRecordGoal.msg.html


(defclass lab_project::OdomRecordGoal
  :super ros::object
  :slots ())

(defmethod lab_project::OdomRecordGoal
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(setf (get lab_project::OdomRecordGoal :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get lab_project::OdomRecordGoal :datatype-) "lab_project/OdomRecordGoal")
(setf (get lab_project::OdomRecordGoal :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======


")



(provide :lab_project/OdomRecordGoal "d41d8cd98f00b204e9800998ecf8427e")

