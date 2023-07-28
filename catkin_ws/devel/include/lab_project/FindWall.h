// Generated by gencpp from file lab_project/FindWall.msg
// DO NOT EDIT!


#ifndef LAB_PROJECT_MESSAGE_FINDWALL_H
#define LAB_PROJECT_MESSAGE_FINDWALL_H

#include <ros/service_traits.h>


#include <lab_project/FindWallRequest.h>
#include <lab_project/FindWallResponse.h>


namespace lab_project
{

struct FindWall
{

typedef FindWallRequest Request;
typedef FindWallResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct FindWall
} // namespace lab_project


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::lab_project::FindWall > {
  static const char* value()
  {
    return "66229cd821efb4126c80f35757f3c73e";
  }

  static const char* value(const ::lab_project::FindWall&) { return value(); }
};

template<>
struct DataType< ::lab_project::FindWall > {
  static const char* value()
  {
    return "lab_project/FindWall";
  }

  static const char* value(const ::lab_project::FindWall&) { return value(); }
};


// service_traits::MD5Sum< ::lab_project::FindWallRequest> should match
// service_traits::MD5Sum< ::lab_project::FindWall >
template<>
struct MD5Sum< ::lab_project::FindWallRequest>
{
  static const char* value()
  {
    return MD5Sum< ::lab_project::FindWall >::value();
  }
  static const char* value(const ::lab_project::FindWallRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::lab_project::FindWallRequest> should match
// service_traits::DataType< ::lab_project::FindWall >
template<>
struct DataType< ::lab_project::FindWallRequest>
{
  static const char* value()
  {
    return DataType< ::lab_project::FindWall >::value();
  }
  static const char* value(const ::lab_project::FindWallRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::lab_project::FindWallResponse> should match
// service_traits::MD5Sum< ::lab_project::FindWall >
template<>
struct MD5Sum< ::lab_project::FindWallResponse>
{
  static const char* value()
  {
    return MD5Sum< ::lab_project::FindWall >::value();
  }
  static const char* value(const ::lab_project::FindWallResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::lab_project::FindWallResponse> should match
// service_traits::DataType< ::lab_project::FindWall >
template<>
struct DataType< ::lab_project::FindWallResponse>
{
  static const char* value()
  {
    return DataType< ::lab_project::FindWall >::value();
  }
  static const char* value(const ::lab_project::FindWallResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // LAB_PROJECT_MESSAGE_FINDWALL_H