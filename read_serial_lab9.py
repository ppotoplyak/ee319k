import serial
# for windows replace '/dev/ttyACM0' with something like 'COM3', see http://pyserial.sourceforge.net/pyserial_api.html
# needs super user rights to open '/dev/ttyACM0', run like 'sudo python read_serial_lab9.py'
# on micro, set UART#_IBRD_R = 43 and UART#_FBRD_R = 26 to match 115200 baud
# on micro write to UART0, unless you have one of these http://amzn.com/B008AGDTA4
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False, bytesize=8, parity='N', stopbits=1)
good_msg_count = 0
echo_bytes = True

def get_next_char():
    next_char = ser.read(1)[0]
    if echo_bytes:
        ser.write(next_char)
    return next_char

def read_until_start_byte():
    while True:
        char_read = get_next_char()
        if char_read != chr(0x02):
            print("Ignoring 0x%X while waiting for start byte"  % ord(char_read))
        else:
            return char_read

while True:
    msg = [read_until_start_byte(), get_next_char()]
    if not msg[len(msg) - 1].isdigit():
        print("Bad byte %d: %X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(get_next_char())
    if msg[len(msg) - 1] != '.':
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(get_next_char())
    if not msg[len(msg) - 1].isdigit():
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(get_next_char())
    if not msg[len(msg) - 1].isdigit():
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(get_next_char())
    if not msg[len(msg) - 1].isdigit():
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(get_next_char())
    if msg[len(msg) - 1] != chr(0x0D):
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    msg.append(get_next_char())
    if msg[len(msg) - 1] != chr(0x03):
        print("Bad byte %d: 0x%X"  % (len(msg) - 1,  ord(msg[len(msg) - 1])))
        continue
    good_msg_count += 1
    print "Good MSG #" + str(good_msg_count) + " " + ''.join(msg[1:6])