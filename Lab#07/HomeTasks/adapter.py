#sockect and charger adapter design pattern example

class Socket:
    def __init__(self):
        self.voltage = 220
        self.type = '2Pins'
    def get_voltage(self):
        return self.voltage
    def get_type(self):
        return self.type

class Charger:
    def __init__(self):
        self.voltage = 220
        self.type = '3Pins'
    def get_voltage(self):
        return self.voltage
    def get_type(self):
        return self.type

class Adapter:
    def __init__(self, socket):
        self.socket = socket
    def get_voltage(self):
        return self.socket.get_voltage()
    def get_type(self):
        return self.socket.get_type()

class Device:
    def __init__(self, adapter):
        self.adapter = adapter
    def charge(self):
        if self.adapter.get_type() == '3Pins':
            print('Charging...')
        else:
            print('Cannot charge. Adapter type is not compatible.')

if __name__ == '__main__':
    print('Socket Type: 2Pins')
    print('Socket Voltage: 220V')

    print('Mobile Charger Type: 3Pins')
    print('Mobile Charger Voltage: 220V')
    print('Mobile Socket Type: 3Pins')

    charger = Charger()
    adapter = Adapter(charger)
    print('Adapter Type: {}'.format(adapter.get_type()))
    device = Device(adapter)
    print('Plug in the adapter to the device...')
    device.charge()


