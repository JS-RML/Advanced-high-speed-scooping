from odrive.enums import *

class Actuator(object):

    def __init__(self, odrv, encoder_offset, direction, link_offset):
        self.odrv = odrv
        self.axis = odrv.axis0
        self.encoder_offset = encoder_offset
        self.direction = direction
        self.link_offset = link_offset

    @property
    def encoder(self):
        return self.odrv.encoder_estimator1.pos_estimate

    @property
    def motor_pos(self):
        return 360 * self.direction * (self.odrv.encoder_estimator1.pos_estimate - self.encoder_offset)

    @motor_pos.setter
    def motor_pos(self, setpoint):
        self.axis.controller.input_pos = (setpoint / 360.) * self.direction + self.encoder_offset

    @property
    def theta(self):
        return self.motor_pos + self.link_offset

    @theta.setter
    def theta(self, setpoint):
        self.motor_pos = setpoint - self.link_offset

    @property
    def armed(self):
        return self.axis.current_state is AXIS_STATE_CLOSED_LOOP_CONTROL

    @armed.setter
    def armed(self, val):
        if val:  # arm
            self.axis.controller.config.input_mode = INPUT_MODE_POS_FILTER  # INPUT_MODE_PASSTHROUGH
            self.axis.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
        else:  # disarm
            self.axis.requested_state = AXIS_STATE_IDLE

    @property
    def stiffness(self):
        return self.axis.controller.config.pos_gain

    @stiffness.setter
    def stiffness(self, val):
        self.axis.controller.config.pos_gain = val

    @property
    def vel_gain(self):
        return self.axis.controller.config.vel_gain

    @vel_gain.setter
    def vel_gain(self, val):
        self.axis.controller.config.vel_gain = val

    @property
    def bandwidth(self):
        return self.axis.controller.config.input_filter_bandwidth

    @bandwidth.setter
    def bandwidth(self, val):
        self.axis.controller.config.input_filter_bandwidth = val
