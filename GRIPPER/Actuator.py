from odrive.enums import *

class Actuator(object):

    def __init__(self, odrv, encoder_offset, direction, link_offset):
        self.odrv = odrv
        self.axis = odrv.axis0
        self.encoder_offset = encoder_offset
        self.direction = direction
        self.link_offset = link_offset
        if(self.encoder_offset > 0.5) :
            self.setPointOffset = encoder_offset - 1
        else :
            self.setPointOffset = encoder_offset


    @property
    def encoder(self):
        posEstimate = self.odrv.encoder_estimator1.pos_estimate

        if posEstimate > 0.5 :
            calibratedEncoder = posEstimate - 1.0
        else :
            calibratedEncoder = posEstimate

        return calibratedEncoder

    @property
    def motor_pos(self):
        tempEncoderValue = self.odrv.encoder_estimator1.pos_estimate
        if tempEncoderValue > 0.5 :
            return 360 * (tempEncoderValue - 1 - self.setPointOffset)
        else :
            return 360 * (tempEncoderValue - self.setPointOffset)

    @motor_pos.setter
    def motor_pos(self, desiredMotorPosition):
        desiredSetPoint = desiredMotorPosition / 360 + self.setPointOffset
        self.axis.controller.input_pos = desiredSetPoint

    @property
    def theta(self):
        return self.motor_pos + self.link_offset

    @theta.setter
    def theta(self, setpoint):
        self.motor_pos = setpoint - self.link_offset

    @property
    def armed(self):
        return self.axis.current_state is AxisState.CLOSED_LOOP_CONTROL

    @armed.setter
    def armed(self, val):
        if val:  # arm
            self.axis.controller.config.input_mode = InputMode.PASSTHROUGH
            self.axis.requested_state = AxisState.CLOSED_LOOP_CONTROL
        else:  # disarm
            self.axis.requested_state = AxisState.IDLE

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

    def iBusValue(self):
        return self.odrv.ibus

    def clearErrors(self):
        self.odrv.clear_errors()
