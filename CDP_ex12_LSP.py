# Title: CDP_ex12_LSP
# Purpose : To implement Liskovs Substitution Principle
# Instructions : The following is code in the design stage, and is implemented in psuedocode, you
#                have been asked to review it, can you determine if it meets LSP rules, if not can you
#                suggesat a fix.

class ApplianceMonitor():
    def on(self):
        """
        on - function to turn the monitor on
        :return: Boolean
        """
        #send the hex code 0x0001 to the hardware interface
        #confirm the response and respond True for 0x0011 False for all other states
        pass

    def off(self):
        """
        of - function to turn the monitor off
        :return: Boolean
        """
        #send the hex code 0x0002 to the hardware interface
        #confirm the response and respond True for 0x0022 False for all other states
        pass

    def send_command(self, command, value):
        """
        send_command - function to instruct the attached device with appropriate hex command and hex value
        :return: Boolean
        """
        #send the bytes [command:value] to the hardware interface
        #confirm the response and respond True for 0xFF00, False for all other states
        pass



class GasSupplyValve(ApplianceMonitor):
    def on(self):
        # Code to send to interface
        pass

    def off(self):
        # Code to send to interface
        pass

    def send_command(self, command, value):
        # code to send command
        pass


class ElectricityControl(ApplianceMonitor):
    def on(self):
        # Code to send to interface
        pass

    def off(self):
        # Code to send to interface
        pass