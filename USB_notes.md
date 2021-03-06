1.  USB data transfers occur through a series of events called **transactions**.
2.  Transactions are conducted within a Host-controlled time interval called a frame.
    The length and frequency of the transactions depends upon the **Transfer Type** being used for an endpoint.
3.  The type of transfer which can be sent in a frame, and the frame length is defined by the specified USB speed.
4.  The four possible USB [transfer types](https://microchipdeveloper.com/usb:transfer) allowed are:
       + Interrupt
       + Bulk
       + Isochronous
       + Control
                              
5.                              +-+-+-+-+-+-+-+-+-+-+-+-+
                                |                       |
                                |    USB Data Transfer  |
                                |                       |
                                +-+-+-+-+-+-+-+-+-+-+-+-+
                                            |
                                            |
                                            |
                    +-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+
                    || Transactions || + || Transactions || + || Transactions  ||
                    +-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+
                            |
                            |
                            |
                    +-+-+-+-+-+-+-+-+-+-+-+-+    
                    || Token Packet         ||
                    || Data Packet          ||
                    || HandShake Packet     ||
                    || Start of Frame       ||
                    +-+-+-+-+-+-+-+-+-+-+-+-+


[Also See](https://www.keil.com/pack/doc/mw/USB/html/pipemodel.png)


+ Token Packet :
![alt text](https://engineersgarag.wpengine.com/wp-content/uploads/2019/07/Image-Showing-Data-Format-Token-Packets.png)

+ Data Packet :
![alt Text](https://engineersgarag.wpengine.com/wp-content/uploads/2019/07/Image-Showing-Data-Format-Data-Packets.png)

+ HandShake Packet :
![alt text](https://engineersgarag.wpengine.com/wp-content/uploads/2019/07/Image-Showing-Data-Format-Handshake-Packets.png)

+ Start OF Frame :
![alt text](https://engineersgarag.wpengine.com/wp-content/uploads/2019/07/Image-Showing-Data-Format-Start-Frame-Packets-SOF.png)




#### USB Packet Fields [See](https://www.engineersgarage.com/tutorials/usb-protocol-types-of-usb-packets-and-usb-transfers-part-2-6/)


6. **USB Descriptors** : [See...](https://www.engineersgarage.com/article_page/usb-descriptors-and-their-types-part-3-6/)
                   
                    Each Universal Serial Bus (USB) Device has a set of descriptors.
                    The descriptors are read by the Host during enumeration. Descriptors inform
                    the host of the following information about a Device:

+ The version of USB supported by the Device
+ Who made the Device
+ How many ways the Device can be configured by the Host
+ The power consumed by each Device configuration
+ The number and length of endpoints on the device
+ What type of transfer method is to be used to communicate with endpoints
+ How often the endpoints are to be serviced
+ What text to display if the Host operating systems accepts text descriptions


7. **Descriptor Types** : [See](https://microchipdeveloper.com/usb:descriptor)

The most commonly used descriptors include:

+ Device Descriptor
+ Configuration Descriptor
+ Interface Descriptor
+ Endpoint Descriptor
+ String Descriptor


8. **USB Device Classes** : [See](https://microchipdeveloper.com/usb:device-classes)

===============================================================================

9. **USB Enumeration** : [See](https://microchipdeveloper.com/usb:enumeration)
  Enumeration is the process whereby the Host detects the presence of a Device and takes the necessary steps to ensure 
  that the Device endpoints are added to the list of endpoints serviced by the Host.
  
   + **Device Enumeration States** :
  ![alt text](https://microchip.wikidot.com/local--files/usb:enumeration/device-states.svg)
  
   + **Device Detection :**
  The presence of a newly installed Full Speed, High Speed or Low Speed Device is recognized
  by changes in the D- or D+ signal. A low-speed device places 5 V on D-, high- and full-speed
  devices assert 5 V on D+ . The connection signals are detected by the Hub and reported to the Host.
  Once a Device is detected, the Host issues a **RESET command** to the Device.

+ [RESET command](https://microchipdeveloper.com/usb:reset-suspend-resume)
+ [Suspent Command](https://microchipdeveloper.com/usb:reset-suspend-resume)
+ [Resume Command](https://microchipdeveloper.com/usb:reset-suspend-resume)
 

   + **Default State :**
  When a RESET control signal sequence is received, the Device will manage its load, per specification, to enumerate.
  If the attached Device is a High Speed device a “chirp” will be returned and the High Speed detection process will
  be completed. Once the speed has been settled the Host reads the Device descriptor and assigns an address
  
   + **Addressed State :**
  After setting the address the Host reads all remaining descriptor tables for the device. If a Host determines 
  it can service the Device’s interface endpoints and provide sufficient power, the Host issues a command informing
  the Device which of its configurations to activate.
  
   + **Configured State :**
  After receiving notification from the Host regarding which configuration to activate, the Device is ready to run 
  using the active configuration.
  
  
  
10. **Control Commands for USB Devices** : [See](https://microchipdeveloper.com/usb:control-commands)

    
11. The Control Transfer is the only transfer type which is supported even when the device is yet not configured.
the Control Transfer consists of three transactions –
[See](https://www.engineersgarage.com/tutorials/usb-requests-and-stages-of-control-transfer-part-4-6/)

+ Setup transaction,
+ Data transaction (optional) and
+ Status transaction

![alt text](https://engineersgarag.wpengine.com/wp-content/uploads/2019/07/Image-Showing-Data-Format-USB-Control-Transfer.png)


12. Standard USB Requests : [See](https://www.engineersgarage.com/tutorials/usb-requests-and-stages-of-control-transfer-part-4-6/)
    + GET_STATUS :
    + SET_FEATURE/CLEAR_FEATURE:
    + DEVICE_REMOTE_WAKEUP
    + SET_ADDRESS
    + GET_DESCRIPTOR
    + SET_DESCRIPTOR: 
    + SET_CONFIGURATION
    + GET_CONFIGURATION
    + SET_INTERFACE
    + GET_INTERFACE
    + SYNCH_FRAME
    
    
 13. Validity of Requests : [See](https://www.engineersgarage.com/tutorials/usb-requests-and-stages-of-control-transfer-part-4-6/)
 
 14.  **Signal and Encoding of USB System** : [See](https://www.engineersgarage.com/tutorials/signal-and-encoding-of-usb-system-part-5-6/)
 
 + Differential 0 and Differential 1:
 + Single Ended Zero
 + Single Ended One:
 + idle
 + Data J and Data K
 + Start of Packet:
 + End of Packet
 + Disconnect
 + connect
 + Keep Alive Signal
 + Suspend State:
 + Resume:
 + Reset State:
 + Detached State:
 + Attached State:
 + Encoding Scheme
 + Bit stiffing
        
    
   
  
  
**=============================================================================**

# Commonly used USB Speed Specifications :
  ![alt text](https://www.electronicdesign.com/sites/electronicdesign.com/files/uploads/2015/02/0216_TI_USBtypeC_No2_Table1.gif)
  
## Speed Identification :
  At the device end of the link a 1.5 kohm resistor pulls one of the lines up to a 3.3V supply derived from VBUS.

This is on D- for a low speed device, and on D+ for a full speed device.

(A high speed device will initially present itself as a full speed device with the pull-up resistor on D+.)

The host can determine the required speed by observing which line is pulled high.
![alt text](http://www.usbmadesimple.co.uk/ums_j_speed_r.jpg)

+ [BUS States](http://www.usbmadesimple.co.uk/ums_3.htm)


