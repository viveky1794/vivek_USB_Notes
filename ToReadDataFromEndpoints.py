import usb.core
import usb.util

VENDOR_ID = 0x0D8F
PRODUCT_ID = 0x0200

# find the USB device
device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if device.is_kernel_driver_active(0):
    device.detach_kernel_driver(0)


# use the first/default configuration
device.set_configuration()
# first endpoint
print("***************************************************")
endpoint = device[0][(0,0)][0]
print(endpoint)
ep_addr = endpoint.bEndpointAddress
print(ep_addr)
ep_msp = endpoint.wMaxPacketSize
print(ep_msp)
print("***************************************************")
# read a data packet
attempts = 10
data = None
#while data is None and attempts > 0:
while True:
    print(data)
    try:
        data = device.read(ep_addr, ep_msp)
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            attempts -= 1
            continue

#print( data )
