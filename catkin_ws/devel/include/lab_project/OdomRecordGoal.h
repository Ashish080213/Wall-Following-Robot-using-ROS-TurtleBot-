// Generated by gencpp from file lab_project/OdomRecordGoal.msg
// DO NOT EDIT!


#ifndef LAB_PROJECT_MESSAGE_ODOMRECORDGOAL_H
#define LAB_PROJECT_MESSAGE_ODOMRECORDGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace lab_project
{
template <class ContainerAllocator>
struct OdomRecordGoal_
{
  typedef OdomRecordGoal_<ContainerAllocator> Type;

  OdomRecordGoal_()
    {
    }
  OdomRecordGoal_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::lab_project::OdomRecordGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::lab_project::OdomRecordGoal_<ContainerAllocator> const> ConstPtr;

}; // struct OdomRecordGoal_

typedef ::lab_project::OdomRecordGoal_<std::allocator<void> > OdomRecordGoal;

typedef boost::shared_ptr< ::lab_project::OdomRecordGoal > OdomRecordGoalPtr;
typedef boost::shared_ptr< ::lab_project::OdomRecordGoal const> OdomRecordGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::lab_project::OdomRecordGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::lab_project::OdomRecordGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace lab_project

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::lab_project::OdomRecordGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lab_project::OdomRecordGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lab_project::OdomRecordGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lab_project::OdomRecordGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lab_project::OdomRecordGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lab_project::OdomRecordGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::lab_project::OdomRecordGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::lab_project::OdomRecordGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::lab_project::OdomRecordGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "lab_project/OdomRecordGoal";
  }

  static const char* value(const ::lab_project::OdomRecordGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::lab_project::OdomRecordGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"\n"
;
  }

  static const char* value(const ::lab_project::OdomRecordGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::lab_project::OdomRecordGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct OdomRecordGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::lab_project::OdomRecordGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::lab_project::OdomRecordGoal_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // LAB_PROJECT_MESSAGE_ODOMRECORDGOAL_H
