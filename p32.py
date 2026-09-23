class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class Light(SmartDevice):
    def turn_on(self):
        return "Light is turned ON. Brightness set to 100%."

    def turn_off(self):
        return "Light is turned OFF."

class Fan(SmartDevice):
    def turn_on(self):
        return "Fan is turned ON. Speed set to 3."

    def turn_off(self):
        return "Fan is turned OFF."

class AC(SmartDevice):
    def turn_on(self):
        return "AC is turned ON. Temperature set to 24°C."

    def turn_off(self):
        return "AC is turned OFF."

class TV(SmartDevice):
    def turn_on(self):
        return "TV is turned ON. Displaying home screen."

    def turn_off(self):
        return "TV is turned OFF into standby mode."

if __name__ == "__main__":
    devices = [Light(), Fan(), AC(), TV()]

    for device in devices:
        print(device.turn_on())
        print(device.turn_off())
        print()
