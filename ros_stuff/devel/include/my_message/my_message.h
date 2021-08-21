// Generated by gencpp from file my_message/my_message.msg
// DO NOT EDIT!


#ifndef MY_MESSAGE_MESSAGE_MY_MESSAGE_H
#define MY_MESSAGE_MESSAGE_MY_MESSAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace my_message
{
template <class ContainerAllocator>
struct my_message_
{
  typedef my_message_<ContainerAllocator> Type;

  my_message_()
    : some_floats()  {
    }
  my_message_(const ContainerAllocator& _alloc)
    : some_floats(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _some_floats_type;
  _some_floats_type some_floats;





  typedef boost::shared_ptr< ::my_message::my_message_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_message::my_message_<ContainerAllocator> const> ConstPtr;

}; // struct my_message_

typedef ::my_message::my_message_<std::allocator<void> > my_message;

typedef boost::shared_ptr< ::my_message::my_message > my_messagePtr;
typedef boost::shared_ptr< ::my_message::my_message const> my_messageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::my_message::my_message_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::my_message::my_message_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::my_message::my_message_<ContainerAllocator1> & lhs, const ::my_message::my_message_<ContainerAllocator2> & rhs)
{
  return lhs.some_floats == rhs.some_floats;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::my_message::my_message_<ContainerAllocator1> & lhs, const ::my_message::my_message_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace my_message

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::my_message::my_message_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::my_message::my_message_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::my_message::my_message_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::my_message::my_message_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_message::my_message_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_message::my_message_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::my_message::my_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "97ab95377be0b99d91d817753c93dd06";
  }

  static const char* value(const ::my_message::my_message_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x97ab95377be0b99dULL;
  static const uint64_t static_value2 = 0x91d817753c93dd06ULL;
};

template<class ContainerAllocator>
struct DataType< ::my_message::my_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "my_message/my_message";
  }

  static const char* value(const ::my_message::my_message_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::my_message::my_message_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64[] some_floats\n"
;
  }

  static const char* value(const ::my_message::my_message_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::my_message::my_message_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.some_floats);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct my_message_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::my_message::my_message_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::my_message::my_message_<ContainerAllocator>& v)
  {
    s << indent << "some_floats[]" << std::endl;
    for (size_t i = 0; i < v.some_floats.size(); ++i)
    {
      s << indent << "  some_floats[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.some_floats[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // MY_MESSAGE_MESSAGE_MY_MESSAGE_H
