
(cl:in-package :asdf)

(defsystem "lab_project-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "FindWall" :depends-on ("_package_FindWall"))
    (:file "_package_FindWall" :depends-on ("_package"))
  ))