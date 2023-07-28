// Auto-generated. Do not edit!

// (in-package lab_project.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class OdomRecordResult {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.list_of_odoms = null;
    }
    else {
      if (initObj.hasOwnProperty('list_of_odoms')) {
        this.list_of_odoms = initObj.list_of_odoms
      }
      else {
        this.list_of_odoms = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type OdomRecordResult
    // Serialize message field [list_of_odoms]
    // Serialize the length for message field [list_of_odoms]
    bufferOffset = _serializer.uint32(obj.list_of_odoms.length, buffer, bufferOffset);
    obj.list_of_odoms.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point32.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type OdomRecordResult
    let len;
    let data = new OdomRecordResult(null);
    // Deserialize message field [list_of_odoms]
    // Deserialize array length for message field [list_of_odoms]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.list_of_odoms = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.list_of_odoms[i] = geometry_msgs.msg.Point32.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 12 * object.list_of_odoms.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lab_project/OdomRecordResult';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a23c25e5b3ba8d526c2e8cee6629770f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    geometry_msgs/Point32[] list_of_odoms
    
    ================================================================================
    MSG: geometry_msgs/Point32
    # This contains the position of a point in free space(with 32 bits of precision).
    # It is recommeded to use Point wherever possible instead of Point32.  
    # 
    # This recommendation is to promote interoperability.  
    #
    # This message is designed to take up less space when sending
    # lots of points at once, as in the case of a PointCloud.  
    
    float32 x
    float32 y
    float32 z
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new OdomRecordResult(null);
    if (msg.list_of_odoms !== undefined) {
      resolved.list_of_odoms = new Array(msg.list_of_odoms.length);
      for (let i = 0; i < resolved.list_of_odoms.length; ++i) {
        resolved.list_of_odoms[i] = geometry_msgs.msg.Point32.Resolve(msg.list_of_odoms[i]);
      }
    }
    else {
      resolved.list_of_odoms = []
    }

    return resolved;
    }
};

module.exports = OdomRecordResult;
