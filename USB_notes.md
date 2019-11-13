

# USB Enumeration :[Raw Link](https://microchipdeveloper.com/usb:enumeration)
  Enumeration is the process whereby the Host detects the presence of a Device and takes the necessary steps to ensure 
  that the Device endpoints are added to the list of endpoints serviced by the Host.
  
## Device Enumeration States :
  ![alt text](https://microchip.wikidot.com/local--files/usb:enumeration/device-states.svg)
  
## Device Detection :
  The presence of a newly installed Full Speed, High Speed or Low Speed Device is recognized
  by changes in the D- or D+ signal. A low-speed device places 5 V on D-, high- and full-speed
  devices assert 5 V on D+ . The connection signals are detected by the Hub and reported to the Host.
  Once a Device is detected, the Host issues a **RESET command** to the Device.

+ ### RESET command :
  During the enumeration process the Host issues a Reset signal to the Device. This USB Reset is not
  to be confused with a hardware or power-on reset. The purpose of the USB Reset is to set the software
  state of the Device so enumeration can proceed.

  Devices recognize a Reset condition when both D- and D+ are both held low (SE0) for 10 ms.
  In some cases the Device is able to detect the Reset within 2.5 µs, however the Host will maintain
  the Reset condition for the entire 10 ms.

![alt text](https://microchip.wikidot.com/local--files/usb:reset-suspend-resume/reset-signal.svg)

  To initiate a reset, D+ and D- are held low by the Hub. Having the Hub hold the data lines low allows
  the Host to continually service the other devices and avoid having Devices enter suspend mode for lack
  of activity on D+ and D-. The Host causes the Hub to reset a Device by issuing a SET_PORT_FEATURE(PORT_RESET)
  control command to the Hub.

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
  
  
**===============================================================================================================**

# Commonly used USB Speed Specifications :
  ![alt text](https://www.electronicdesign.com/sites/electronicdesign.com/files/uploads/2015/02/0216_TI_USBtypeC_No2_Table1.gif)
  
  
  
