// Generated by gencpp from file lab_project/FindWallResponse.msg
// DO NOT EDIT!


#ifndef LAB_PROJECT_MESSAGE_FINDWALLRESPONSE_H
#define LAB_PROJECT_MESSAGE_FINDWALLRESPONSE_H


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
struct FindWallResponse_
{
  typedef FindWallResponse_<ContainerAllocator> Type;

  FindWallResponse_()
    : wallfound(false)  {
    }
  FindWallResponse_(const ContainerAllocator& _alloc)
    : wallfound(false)  {
  (void)_alloc;
    }



   typedef uint8_t _wallfound_type;
  _wallfound_type wallfound;





  typedef boost::shared_ptr< ::lab_project::FindWallResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::lab_project::FindWallResponse_<ContainerAllocator> const> ConstPtr;

}; // struct FindWallResponse_

typedef ::lab_project::FindWallResponse_<std::allocator<void> > FindWallResponse;

typedef boost::shared_ptr< ::lab_project::FindWallResponse > FindWallResponsePtr;
typedef boost::shared_ptr< ::lab_project::FindWallResponse const> FindWallResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::lab_project::FindWallResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::lab_project::FindWallResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::lab_project::FindWallResponse_<ContainerAllocator1> & lhs, const ::lab_project::FindWallResponse_<ContainerAllocator2> & rhs)
{
  return lhs.wallfound == rhs.wallfound;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::lab_project::FindWallResponse_<ContainerAllocator1> & lhs, const ::lab_project::FindWallResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace lab_project

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::lab_project::FindWallResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lab_project::FindWallResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lab_project::FindWallResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lab_project::FindWallResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lab_project::FindWallResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lab_project::FindWallResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::lab_project::FindWallResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "66229cd821efb4126c80f35757f3c73e";
  }

  static const char* value(const ::lab_project::FindWallResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x66229cd821efb412ULL;
  static const uint64_t static_value2 = 0x6c80f35757f3c73eULL;
};

template<class ContainerAllocator>
struct DataType< ::lab_project::FindWallResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "lab_project/FindWallResponse";
  }

  static const char* value(const ::lab_project::FindWallResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::lab_project::FindWallResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool wallfound\n"
;
  }

  static const char* value(const ::lab_project::FindWallResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::lab_project::FindWallResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.wallfound);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FindWallResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::lab_project::FindWallResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::lab_project::FindWallResponse_<ContainerAllocator>& v)
  {
    s << indent << "wallfound: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.wallfound);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LAB_PROJECT_MESSAGE_FINDWALLRESPONSE_H
