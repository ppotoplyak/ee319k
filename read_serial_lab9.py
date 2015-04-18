import serial
# for windows replace '/dev/ttyACM0' with something like 'COM3', see http://pyserial.sourceforge.net/pyserial_api.html
# note the baud is 115200
# needs super user rights to open '/dev/ttyACM0', run like 'sudo python read_serial_lab9.py'
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False, bytesize=8, parity='N', stopbits=1)
good_msg_count = 0

def read_until_start_byte():
    while True:
        data = ser.read(1)
        if data[0] != chr(0x02):
            print("Ignoring 0x%X while waiting for start byte"  % ord(data[0]))
        else:
            return

while True:
    read_until_start_byte()
    msg = [chr(0x02), ser.read(1)[0]]
    if not msg[len(msg) - 1].isdigit():
        print("Bad byte %d: %X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(ser.read(1)[0])
    if msg[len(msg) - 1] != '.':
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(ser.read(1)[0])
    if not msg[len(msg) - 1].isdigit():
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(ser.read(1)[0])
    if not msg[len(msg) - 1].isdigit():
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(ser.read(1)[0])
    if not msg[len(msg) - 1].isdigit():
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(ser.read(1)[0])
    if msg[len(msg) - 1] != chr(0x0D):
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(ser.read(1)[0])
    if msg[len(msg) - 1] != chr(0x03):
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    good_msg_count += 1
    print "Good MSG #" + str(good_msg_count) + " " + ''.join(msg[1:6])