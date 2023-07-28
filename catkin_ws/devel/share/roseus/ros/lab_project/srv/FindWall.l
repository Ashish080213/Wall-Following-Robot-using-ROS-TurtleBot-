;; Auto-generated. Do not edit!


(when (boundp 'lab_project::FindWall)
  (if (not (find-package "LAB_PROJECT"))
    (make-package "LAB_PROJECT"))
  (shadow 'FindWall (find-package "LAB_PROJECT")))
(unless (find-package "LAB_PROJECT::FINDWALL")
  (make-package "LAB_PROJECT::FINDWALL"))
(unless (find-package "LAB_PROJECT::FINDWALLREQUEST")
  (make-package "LAB_PROJECT::FINDWALLREQUEST"))
(unless (find-package "LAB_PROJECT::FINDWALLRESPONSE")
  (make-package "LAB_PROJECT::FINDWALLRESPONSE"))

(in-package "ROS")





(defclass lab_project::FindWallRequest
  :super ros::object
  :slots ())

(defmethod lab_project::FindWallRequest
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

(defclass lab_project::FindWallResponse
  :super ros::object
  :slots (_wallfound ))

(defmethod lab_project::FindWallResponse
  (:init
   (&key
    ((:wallfound __wallfound) nil)
    )
   (send-super :init)
   (setq _wallfound __wallfound)
   self)
  (:wallfound
   (&optional (__wallfound :null))
   (if (not (eq __wallfound :null)) (setq _wallfound __wallfound)) _wallfound)
  (:serialization-length
   ()
   (+
    ;; bool _wallfound
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _wallfound
       (if _wallfound (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _wallfound
     (setq _wallfound (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass lab_project::FindWall
  :super ros::object
  :slots ())

(setf (get lab_project::FindWall :md5sum-) "66229cd821efb4126c80f35757f3c73e")
(setf (get lab_project::FindWall :datatype-) "lab_project/FindWall")
(setf (get lab_project::FindWall :request) lab_project::FindWallRequest)
(setf (get lab_project::FindWall :response) lab_project::FindWallResponse)

(defmethod lab_project::FindWallRequest
  (:response () (instance lab_project::FindWallResponse :init)))

(setf (get lab_project::FindWallRequest :md5sum-) "66229cd821efb4126c80f35757f3c73e")
(setf (get lab_project::FindWallRequest :datatype-) "lab_project/FindWallRequest")
(setf (get lab_project::FindWallRequest :definition-)
      "
---
bool wallfound
")

(setf (get lab_project::FindWallResponse :md5sum-) "66229cd821efb4126c80f35757f3c73e")
(setf (get lab_project::FindWallResponse :datatype-) "lab_project/FindWallResponse")
(setf (get lab_project::FindWallResponse :definition-)
      "
---
bool wallfound
")



(provide :lab_project/FindWall "66229cd821efb4126c80f35757f3c73e")


