;; Auto-generated. Do not edit!


(when (boundp 'lab_project::OdomRecordFeedback)
  (if (not (find-package "LAB_PROJECT"))
    (make-package "LAB_PROJECT"))
  (shadow 'OdomRecordFeedback (find-package "LAB_PROJECT")))
(unless (find-package "LAB_PROJECT::ODOMRECORDFEEDBACK")
  (make-package "LAB_PROJECT::ODOMRECORDFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude OdomRecordFeedback.msg.html


(defclass lab_project::OdomRecordFeedback
  :super ros::object
  :slots (_current_total ))

(defmethod lab_project::OdomRecordFeedback
  (:init
   (&key
    ((:current_total __current_total) 0.0)
    )
   (send-super :init)
   (setq _current_total (float __current_total))
   self)
  (:current_total
   (&optional __current_total)
   (if __current_total (setq _current_total __current_total)) _current_total)
  (:serialization-length
   ()
   (+
    ;; float32 _current_total
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _current_total
       (sys::poke _current_total (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _current_total
     (setq _current_total (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get lab_project::OdomRecordFeedback :md5sum-) "30966342c24c9732e6e891bbe67686ec")
(setf (get lab_project::OdomRecordFeedback :datatype-) "lab_project/OdomRecordFeedback")
(setf (get lab_project::OdomRecordFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
float32 current_total

")



(provide :lab_project/OdomRecordFeedback "30966342c24c9732e6e891bbe67686ec")

