

# USB Enumeration :[...](https://microchipdeveloper.com/usb:enumeration)
  Enumeration is the process whereby the Host detects the presence of a Device and takes the necessary steps to ensure 
  that the Device endpoints are added to the list of endpoints serviced by the Host.
  
## Device Enumeration States :
  ![alt text](https://microchip.wikidot.com/local--files/usb:enumeration/device-states.svg)
  
## Device Detection :
  The presence of a newly installed Full Speed, High Speed or Low Speed Device is recognized
  by changes in the D- or D+ signal. A low-speed device places 5 V on D-, high- and full-speed
  devices assert 5 V on D+ . The connection signals are detected by the Hub and reported to the Host.
  Once a Device is detected, the Host issues a **RESET command** to the Device.

+ [RESET command](https://microchipdeveloper.com/usb:reset-suspend-resume)
+ [Suspent Command](https://microchipdeveloper.com/usb:reset-suspend-resume)
+ [Resume Command](https://microchipdeveloper.com/usb:reset-suspend-resume)
 

## Default State :
  When a RESET control signal sequence is received, the Device will manage its load, per specification, to enumerate.
  If the attached Device is a High Speed device a “chirp” will be returned and the High Speed detection process will
  be completed. Once the speed has been settled the Host reads the Device descriptor and assigns an address
  
## Addressed State :
  After setting the address the Host reads all remaining descriptor tables for the device. If a Host determines 
  it can service the Device’s interface endpoints and provide sufficient power, the Host issues a command informing
  the Device which of its configurations to activate.
  
## Configured State :
  After receiving notification from the Host regarding which configuration to activate, the Device is ready to run 
  using the active configuration.
  
  
  
# Control Commands for USB Devices [...](https://microchipdeveloper.com/usb:control-commands)

  
  
  
  
  
  
**================================================================================**

# Commonly used USB Speed Specifications :
  ![alt text](https://www.electronicdesign.com/sites/electronicdesign.com/files/uploads/2015/02/0216_TI_USBtypeC_No2_Table1.gif)
  
## Speed Identification :
  At the device end of the link a 1.5 kohm resistor pulls one of the lines up to a 3.3V supply derived from VBUS.

This is on D- for a low speed device, and on D+ for a full speed device.

(A high speed device will initially present itself as a full speed device with the pull-up resistor on D+.)

The host can determine the required speed by observing which line is pulled high.
![alt text](http://www.usbmadesimple.co.uk/ums_j_speed_r.jpg)

+ [BUS States](http://www.usbmadesimple.co.uk/ums_3.htm)


