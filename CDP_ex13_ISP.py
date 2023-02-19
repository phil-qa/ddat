# Title: CDP_ex13_ISP
# Purpose : Refactor the code to make it meet Interface segregation principle
# Instructions : The following code is used to set a gas supply Gate that
#                controls the flow of gas. There are two derived classes
#                but this currently it does not meet ISP,
#                This is reflected when it is run.
#                Refactor the code to make the right elements of the class
#                abstract

class SupplyGate:
    def __init__(self, identifier, max_flow):
        self.identifier = identifier
        self.current_rate = 0
        self.valve_settings = ["off", "mid", "full"]
        self.current_valve_setting = self.valve_settings[0]
        self.max_flow = max_flow

    def open_valve(self):
        """
        Open valve will attempt to open the flow falve to the next level, if at maximum it will return with no change
        :return:
        """
        if self.current_valve_setting == self.valve_settings[2]:
            return
        else:
            self.current_valve_setting = self.valve_settings[self.valve_settings.index(self.current_valve_setting)+1]
            self._set_current_rate()

    def _set_current_rate(self):
        """
        Function to set the current flow rate according to the current valve state setting
        at off flow rate is 0,
        mid the current rate is 50% of maximum,
        at full the current rate is the same as the maximum flow
        :return:
        """
        if self.current_valve_setting == 'off':
            self.current_rate = 0
        elif self.current_valve_setting == 'mid':
            self.current_rate =  self.max_flow * 0.5
        elif self.current_valve_setting == 'full':
            self.current_rate = self.max_flow


class PumpedSupplyGate(SupplyGate):
    def __init__(self, identifier, max_flow):
        super().__init__(identifier, max_flow)
        self.pump_multiplier = [1,2]
        self.current_pump_setting = self.pump_multiplier[0]

    def open_valve(self, pump_state):
        """
        function to open the flow valve
        sets the current flow rate depending on the valve setting and modifies the value according
        to the if the pump is on or off

        :param pump_state: 'on' / 'off'
        :return:
        """
        if pump_state == 'on':
            self.current_pump_setting = self.pump_multiplier[1]
        else:
            self.current_pump_setting = self.pump_multiplier[0]

        if self.current_valve_setting == self.valve_settings[2]:
            return
        else:
            self.current_valve_setting = self.valve_settings[
                self.valve_settings.index(self.current_valve_setting) + 1]
            self._set_current_rate()

    def set_current_rate(self):
        """
        sets the current rate based on the valve setting and the pump status
        off : valve is closed 0 flow rate
        mid : valve is half open and base flow rate is half max
        full : valve is fully open and the base flow rate is maximum
        pump off : no modification to the flow
        pump on : flow = base * current_pump_setting
        :return:
        """
        if self.current_valve_setting == 'off':
            self.current_rate = 0
        elif self.current_valve_setting == 'mid':
            self.current_rate =  self.max_flow * 0.5 * self.current_pump_setting
        elif self.current_valve_setting == 'full':
            self.current_rate = self.max_flow * self.current_pump_setting


new_gate = SupplyGate("new gate", 1000)
print(new_gate.current_rate)
new_gate.open_valve()
print(f"The standard pumped gate in valve open gives half the max :{new_gate.current_rate == (new_gate.max_flow/2)}")

new_pumped_gate = PumpedSupplyGate("pumped gate", 1000)
new_pumped_gate.open_valve('on')
print(f"The pumped gate adds 2x pressure: {new_pumped_gate.current_rate == new_pumped_gate.max_flow}")
