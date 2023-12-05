from socket import *
import threading
import time
import struct
from dataclasses import dataclass
from enum import Enum
from multipledispatch import dispatch

@dataclass
class systemSTAT:
    time: float = None
    jnt_ref: tuple = None
    jnt_ang: tuple = None
    cur: tuple = None
    tcp_ref: tuple = None
    tcp_pos: tuple = None
    analog_in: tuple = None
    analog_out: tuple = None
    digital_in: tuple = None
    digital_out: tuple = None
    temperature_mc: tuple = None
    task_pc: int = None
    task_repeat: int = None
    task_run_id: int = None
    task_run_num: int = None
    task_run_time: float = None
    task_state: int = None
    default_speed: float = None
    robot_state: int = None
    power_state: int = None
    tcp_target: tuple = None
    jnt_info: tuple = None
    collision_detect_onoff: int = None
    is_freedrive_mode: int = None
    program_mode: int = None
    init_state_info: int = None
    init_error: int = None
    tfb_analog_in: tuple = None
    tfb_digital_in: tuple = None
    tfb_digital_out: tuple = None
    tfb_voltage_out: float = None
    op_stat_collision_occur: int = None
    op_stat_sos_flag: int = None
    op_stat_self_collision: int = None
    op_stat_soft_estop_occur: int = None
    op_stat_ems_flag: int = None
    digital_in_config: tuple = None
    inbox_trap_flag: tuple = None
    inbox_check_mode: tuple = None
    eft_fx: float = None
    eft_fy: float = None
    eft_fz: float = None
    eft_mx: float = None
    eft_my: float = None
    eft_mz: float = None


@dataclass
class Joint:
    j0: float = None
    j1: float = None
    j2: float = None
    j3: float = None
    j4: float = None
    j5: float = None


@dataclass
class Point:
    x: float = None
    y: float = None
    z: float = None
    rx: float = None
    ry: float = None
    rz: float = None


class COBOT_STATUS(Enum):
    IDLE = 0
    PAUSED = 1
    RUNNING = 2
    UNKNOWN = 3


class CMD_TYPE(Enum):
    MOVE = 0
    NONMOVE = 1


class PG_MODE(Enum):
    SIMULATION = 0
    REAL = 1


class CIRCLE_TYPE(Enum):
    INTENDED = 0
    CONSTANT = 1
    RADIAL = 2
    SMOOTH = 3


class CIRCLE_AXIS(Enum):
    X = 0
    Y = 1
    Z = 2


class BLEND_OPTION(Enum):
    RATIO = 0
    DISTANCE = 1


class BLEND_RTYPE(Enum):
    INTENDED = 0
    CONSTANT = 1


class ITPL_RTYPE(Enum):
    INTENDED = 0
    CONSTANT = 1
    RESERVED1 = 2
    SMOOTH = 3
    RESERVED2 = 4
    CA_INTENDED = 5
    CA_CONSTANT = 6
    RESERVED3 = 7
    CA_SMOOTH = 8


class DOUT_SET(Enum):
    LOW = 0
    HIGH = 1
    BYPASS = 2


class DOUT_SET(Enum):
    VOLT_0 = 0
    VOLT_12 = 1
    VOLT_24 = 2


CMD_PORT = 5000
DATA_PORT = 5001
systemstat_global = systemSTAT()
cmd_connect = True
data_connect = True
bReadCmd = False
moveCmdFlag = False
# CMDSock = socket(AF_INET, SOCK_STREAM)
# DATASock = socket(AF_INET, SOCK_STREAM)
moveCmdCnt = 0
cmd_send_flag = 0  # read cmd에서 사용하기 위한 flag

__RB_VERSION__ = '0.0.5'


def ConnectToCB(ip):
    if not isValidIP(ip):
        print('error')
        # pass
        return False

    global CMDSock
    global DATASock
    CMDSock = socket(AF_INET, SOCK_STREAM)
    DATASock = socket(AF_INET, SOCK_STREAM)

    global cmd_connect
    global data_connect
    cmd_connect = CMDSock.connect_ex((ip, CMD_PORT))
    data_connect = DATASock.connect_ex((ip, DATA_PORT))
    
    if cmd_connect == 0 & data_connect == 0:

        DATAREQ_THREAD = threading.Thread(target=ReqDataStart, args=(DATASock,))
        CMDREAD_THREAD = threading.Thread(target=ReadCMD, args=(CMDSock,))
        DATAREAD_THREAD = threading.Thread(target=ReadDATA, args=(DATASock,))
        DATAREQ_THREAD.start()
        CMDREAD_THREAD.start()
        DATAREAD_THREAD.start()

        # pass
        return True


def DisConnectToCB():
    global cmd_connect
    global data_connect
    cmd_connect = True
    data_connect = True

    time.sleep(1)

    CMDSock.close()
    DATASock.close()
    print('Disconnected...')
    return True


def __Version():
    msg = 'RB-API : ' + __RB_VERSION__
    print(msg)


def GetCurrentJoint():
    if not data_connect:
        current_joint_ = Joint(systemstat_global.jnt_ref[0], systemstat_global.jnt_ref[1], systemstat_global.jnt_ref[2]
                               , systemstat_global.jnt_ref[3], systemstat_global.jnt_ref[4],
                               systemstat_global.jnt_ref[5])
        return current_joint_
    else:
        print("'data socket isn't connect")
        current_joint_ = Joint(0, 0, 0, 0, 0, 0)
        return current_joint_


def GetCurrentSplitedJoint():
    if not data_connect:
        current_joint_ = (systemstat_global.jnt_ref[0], systemstat_global.jnt_ref[1], systemstat_global.jnt_ref[2]
                          , systemstat_global.jnt_ref[3], systemstat_global.jnt_ref[4], systemstat_global.jnt_ref[5])
        return current_joint_
    else:
        print("'data socket isn't connect")
        current_joint_ = (0, 0, 0, 0, 0, 0)
        return current_joint_


def GetCurrentTCP():
    if not data_connect:
        current_tcp_ = Point(systemstat_global.tcp_ref[0], systemstat_global.tcp_ref[1],
                             systemstat_global.tcp_ref[2]
                             , systemstat_global.tcp_ref[3], systemstat_global.tcp_ref[4],
                             systemstat_global.tcp_ref[5])
        return current_tcp_
    else:
        print("'data socket isn't connect")
        current_tcp_ = Point(0, 0, 0, 0, 0, 0)
        return current_tcp_


def GetCurrentSplitedTCP():
    if not data_connect:
        current_tcp_ = (systemstat_global.tcp_ref[0], systemstat_global.tcp_ref[1],
                        systemstat_global.tcp_ref[2]
                        , systemstat_global.tcp_ref[3], systemstat_global.tcp_ref[4],
                        systemstat_global.tcp_ref[5])
        return current_tcp_
    else:
        print("'data socket isn't connect")
        current_tcp_ = ()
        return current_tcp_


def GetCurreJP():
    if not data_connect:
        current_tcp_ = Point(systemstat_global.tcp_ref[0], systemstat_global.tcp_ref[1],
                             systemstat_global.tcp_ref[2]
                             , systemstat_global.tcp_ref[3], systemstat_global.tcp_ref[4],
                             systemstat_global.tcp_ref[5])
        current_joint_ = Joint(systemstat_global.jnt_ref[0], systemstat_global.jnt_ref[1], systemstat_global.jnt_ref[2]
                               , systemstat_global.jnt_ref[3], systemstat_global.jnt_ref[4],
                               systemstat_global.jnt_ref[5])
        return (current_joint_, current_tcp_)
    else:
        print("'data socket isn't connect")
        current_tcp_ = Point(0, 0, 0, 0, 0, 0)
        current_joint_ = Joint(0, 0, 0, 0, 0, 0)
        return (current_joint_, current_tcp_)


def CobotInit():
    msg = 'mc jall init'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def SetProgramMode(mode=PG_MODE):
    msg = None
    if mode == PG_MODE.SIMULATION:
        msg = 'pgmode simulation'
    elif mode == PG_MODE.REAL:
        msg = 'pgmode real'

    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


@dispatch(Point, float, float)
def MoveL(pnt, spd, acc):
    msg = 'move_l(pnt[' + str(pnt.x) + ',' + str(pnt.y) + ',' + str(pnt.z) + ',' + str(pnt.rx) + ',' + str(
        pnt.ry) + ',' + str(pnt.rz) + '], ' + str(spd) + ',' + str(acc) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


# @dispatch(float, float, float, float, float, float, float, float)
def MoveL(x, y, z, rx, ry, rz, spd, acc):
    msg = 'move_l(pnt[' + str(x) + ',' + str(y) + ',' + str(z) + ',' + str(rx) + ',' + str(ry) + ',' + str(
        rz) + '], ' + str(spd) + ',' + str(acc) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


@dispatch(Joint, float, float)
def MoveJ(jnt, spd, acc):
    msg = 'move_j(jnt[' + str(jnt.j0) + ',' + str(jnt.j1) + ',' + str(jnt.j2) + ',' + str(jnt.j3) + ',' + str(
        jnt.j4) + ',' + str(jnt.j5) + '], ' + str(spd) + ',' + str(acc) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


# @dispatch(float, float, float, float, float, float, float, float)
def MoveJ(j0, j1, j2, j3, j4, j5, spd, acc):
    msg = 'move_j(jnt[' + str(j0) + ',' + str(j1) + ',' + str(j2) + ',' + str(j3) + ',' + str(j4) + ',' + str(
        j5) + '], ' + str(spd) + ',' + str(acc) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


@dispatch(Point, float, float)
def MoveJL(pnt, spd, acc):
    msg = 'move_jl(pnt[' + str(pnt.x) + ',' + str(pnt.y) + ',' + str(pnt.z) + ',' + str(pnt.rx) + ',' + str(
        pnt.ry) + ',' + str(pnt.rz) + '], ' + str(spd) + ',' + str(acc) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


@dispatch(float, float, float, float, float, float, float, float)
def MoveJL(x, y, z, rx, ry, rz, spd, acc):
    msg = 'move_jl(pnt[' + str(x) + ',' + str(y) + ',' + str(z) + ',' + str(rx) + ',' + str(ry) + ',' + str(
        rz) + '], ' + str(spd) + ',' + str(acc) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


def MoveJB_Clear():
    msg = 'move_jb_clear()'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


@dispatch(Joint)
def MoveJB_Add(jnt):
    msg = 'move_jb_add(jnt[' + str(jnt.j0) + ',' + str(jnt.j1) + ',' + str(jnt.j2) + ',' + str(jnt.j3) + ',' + str(
        jnt.j4) + ',' + str(jnt.j5) + '])'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


@dispatch(float, float, float, float, float, float)
def MoveJB_Add(j0, j1, j2, j3, j4, j5):
    msg = 'move_jb_add(jnt[' + str(j0) + ',' + str(j1) + ',' + str(j2) + ',' + str(j3) + ',' + str(j4) + ',' + str(
        j5) + '])'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def MoveJB_Run(spd=float, acc=float):
    msg = 'move_jb_run(' + str(spd) + ',' + str(acc) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


def MovePB_Clear():
    msg = 'move_pb_clear()'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


@dispatch(Point, float, BLEND_OPTION, float)
def MovePB_Add(pnt, spd, option, quantity):
    b_option = 0
    if option == BLEND_OPTION.DISTANCE:
        b_option = 1
        if quantity < 0:
            quantity = 0
    elif option == BLEND_OPTION.RATIO:
        b_option = 0
        if quantity < 0:
            quantity = 0
        elif quantity > 1:
            quantity = 1

    msg = 'move_pb_add(pnt[' + str(pnt.x) + ',' + str(pnt.y) + ',' + str(pnt.z) + ',' + str(pnt.rx) + ',' + str(
        pnt.ry) + ',' + str(pnt.rz) + '], ' + str(spd) + ',' + str(b_option) + ',' + str(quantity) + ')'

    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


@dispatch(float, float, float, float, float, float, float, BLEND_OPTION, float)
def MovePB_Add(x, y, z, rx, ry, rz, spd, option, quantity):
    b_option = 0
    if option == BLEND_OPTION.DISTANCE:

        b_option = 1
        if quantity < 0:
            quantity = 0
    elif option == BLEND_OPTION.RATIO:
        b_option = 0
        if quantity < 0:
            quantity = 0
        elif quantity > 1:
            quantity = 1

    msg = 'move_pb_add(pnt[' + str(x) + ',' + str(y) + ',' + str(z) + ',' + str(rx) + ',' + str(ry) + ',' + str(
        rz) + '], ' + str(spd) + ',' + str(b_option) + ',' + str(quantity) + ')'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def MovePB_Run(acc=float, type=BLEND_RTYPE):
    rtype = 0
    if type == BLEND_RTYPE.INTENDED:
        rtype = 0
    elif type == BLEND_RTYPE.CONSTANT:
        rtype = 1

    msg = 'move_pb_run(' + str(acc) + ',' + str(rtype) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


######################################################
def MoveITPL_Clear():
    msg = 'move_itpl_clear()'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


@dispatch(Point, float)
def MoveITPL_Add(pnt, spd):
    msg = 'move_itpl_add(pnt[' + str(pnt.x) + ',' + str(pnt.y) + ',' + str(pnt.z) + ',' + str(pnt.rx) + ',' + str(
        pnt.ry) + ',' + str(pnt.rz) + '], ' + str(spd) + ')'

    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


# @dispatch(float, float, float, float, float, float, float)
def MoveITPL_Add(x, y, z, rx, ry, rz, spd):
    msg = 'move_itpl_add(pnt[' + str(x) + ',' + str(y) + ',' + str(z) + ',' + str(rx) + ',' + str(ry) + ',' + str(
        rz) + '], ' + str(spd) + ')'

    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def MoveITPL_Run(acc=float, type=ITPL_RTYPE):
    rtype = 0
    if type == ITPL_RTYPE.INTENDED:
        rtype = 0
    elif type == ITPL_RTYPE.CONSTANT:
        rtype = 1
    elif type == ITPL_RTYPE.SMOOTH:
        rtype = 3
    elif type == ITPL_RTYPE.CA_INTENDED:
        rtype = 5
    elif type == ITPL_RTYPE.CA_CONSTANT:
        rtype = 6
    elif type == ITPL_RTYPE.CA_SMOOTH:
        rtype = 8

    msg = 'move_itpl_run(' + str(acc) + ',' + str(rtype) + ')'
    return SendCOMMAND(msg, CMD_TYPE.MOVE)


@dispatch(Point, Point, float, float, CIRCLE_TYPE)
def MoveCircle_ThreePoint(pnt1, pnt2, spd, acc, type):
    r_option = 0
    if type == CIRCLE_TYPE.INTENDED:
        r_option = 0
    elif type == CIRCLE_TYPE.CONSTANT:
        r_option = 1
    elif type == CIRCLE_TYPE.RADIAL:
        r_option = 2
    elif type == CIRCLE_TYPE.SMOOTH:
        r_option = 3

    msg = 'move_c_points(pnt[' + str(pnt1.x) + ',' + str(pnt1.y) + ',' + str(pnt1.z) + ',' + str(pnt1.rx) + ',' + str(
        pnt1.ry) + ',' + str(pnt1.rz) + '], pnt[' + str(pnt2.x) + ',' + str(pnt2.y) + ',' + str(pnt2.z) + ',' + str(
        pnt2.rx) + ',' + str(
        pnt2.ry) + ',' + str(pnt2.rz) + '], ' + str(spd) + ',' + str(acc) + ',' + str(r_option) + ')'

    return SendCOMMAND(msg, CMD_TYPE.MOVE)


@dispatch(float, float, float, float, float, float, float, float, float, float, float, float, float, float, CIRCLE_TYPE)
def MoveCircle_ThreePoint(x1, y1, z1, rx1, ry1, rz1, x2, y2, z2, rx2, ry2, rz2, spd, acc, type):
    r_option = 0
    if type == CIRCLE_TYPE.INTENDED:
        r_option = 0
    elif type == CIRCLE_TYPE.CONSTANT:
        r_option = 1
    elif type == CIRCLE_TYPE.RADIAL:
        r_option = 2
    elif type == CIRCLE_TYPE.SMOOTH:
        r_option = 3

    msg = 'move_c_points(pnt[' + str(x1) + ',' + str(y1) + ',' + str(z1) + ',' + str(rx1) + ',' + str(
        ry1) + ',' + str(rz1) + '], pnt[' + str(x2) + ',' + str(y2) + ',' + str(z2) + ',' + str(
        rx2) + ',' + str(ry2) + ',' + str(rz2) + '], ' + str(spd) + ',' + str(acc) + ',' + str(r_option) + ')'

    return SendCOMMAND(msg, CMD_TYPE.MOVE)


@dispatch(Point, CIRCLE_AXIS, float, float, float, float, CIRCLE_TYPE)
def MoveCircle_Axis(pnt, axis, direction, angle, spd, acc, type):
    r_option = 0
    a_option = 0
    if type == CIRCLE_TYPE.INTENDED:
        r_option = 0
    elif type == CIRCLE_TYPE.CONSTANT:
        r_option = 1
    elif type == CIRCLE_TYPE.RADIAL:
        r_option = 2

    if axis == CIRCLE_AXIS.X:
        if direction == 1:
            a_option = '1,0,0'
        elif direction == -1:
            a_option = '-1,0,0'
        else:
            a_option = '1,0,0'
    elif axis == CIRCLE_AXIS.Y:
        if direction == 1:
            a_option = '0,1,0'
        elif direction == -1:
            a_option = '0,-1,0'
        else:
            a_option = '0,1,0'
    elif axis == CIRCLE_AXIS.Z:
        if direction == 1:
            a_option = '0,0,1'
        elif direction == -1:
            a_option = '0,0,-1'
        else:
            a_option = '0,0,1'
    else:
        print('axis-error')

    msg = 'move_c_axis(pnt[' + str(pnt.x) + ',' + str(pnt.y) + ',' + str(pnt.z) + ',' + str(pnt.rx) + ',' + str(
        pnt.ry) + ',' + str(pnt.rz) + '], ' + str(a_option) + ',' + str(angle) + ',' + str(spd) + ',' + str(
        acc) + ',' + str(r_option) + ')'

    return SendCOMMAND(msg, CMD_TYPE.MOVE)


@dispatch(float, float, float, float, float, float, CIRCLE_AXIS, float, float, float, float, CIRCLE_TYPE)
def MoveCircle_Axis(x, y, z, rx, ry, rz, axis, direction, angle, spd, acc, type):
    r_option = 0
    a_option = 0
    if type == CIRCLE_TYPE.INTENDED:
        r_option = 0
    elif type == CIRCLE_TYPE.CONSTANT:
        r_option = 1
    elif type == CIRCLE_TYPE.RADIAL:
        r_option = 2

    if axis == CIRCLE_AXIS.X:
        if direction == 1:
            a_option = '1,0,0'
        elif direction == -1:
            a_option = '-1,0,0'
        else:
            a_option = '1,0,0'
    elif axis == CIRCLE_AXIS.Y:
        if direction == 1:
            a_option = '0,1,0'
        elif direction == -1:
            a_option = '0,-1,0'
        else:
            a_option = '0,1,0'
    elif axis == CIRCLE_AXIS.Z:
        if direction == 1:
            a_option = '0,0,1'
        elif direction == -1:
            a_option = '0,0,-1'
        else:
            a_option = '0,0,1'
    else:
        print('axis-error')

    msg = 'move_c_axis(pnt[' + str(x) + ',' + str(y) + ',' + str(z) + ',' + str(rx) + ',' + str(
        ry) + ',' + str(rz) + '], ' + str(a_option) + ',' + str(angle) + ',' + str(spd) + ',' + str(
        acc) + ',' + str(r_option) + ')'

    return SendCOMMAND(msg, CMD_TYPE.MOVE)


def CBDigitalOut(port=float, type=DOUT_SET):
    dstatus = 0
    if type == DOUT_SET.LOW:
        dstatus = 0
    elif type == DOUT_SET.HIGH:
        dstatus = 1
    elif type == DOUT_SET.BYPASS:
        dstatus = -1

    msg = 'set_box_dout(' + str(port) + ',' + str(dstatus) + ')'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def CBAnalogOut(port=float, voltage=float):
    if voltage > 10 | voltage < 0:
        return False

    if port > 3 | port < 0:
        return False

    msg = 'set_box_aout(' + str(port) + ',' + str(voltage) + ')'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def SetBaseSpeed(spd):
    if spd > 1.0:
        spd = 1.0
    elif spd < 0.:
        spd = 0.
    print(spd)
    msg = 'set_speed_bar(' + str(spd) + ')'
    # print(systemstat_global.jnt_ref)

    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def MotionPause():
    msg = 'task pause'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def MotionHalt():
    msg = 'task stop'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def MotionResume():
    msg = 'task resume_a'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def CollisionResume():
    msg = 'task resume_b'
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def RobotPowerDown():
    msg = "arm_powerdown()"
    return SendCOMMAND(msg, CMD_TYPE.NONMOVE)


def ManualScript(ex_msg):
    return SendCOMMAND(ex_msg, CMD_TYPE.NONMOVE)


def ReqDataStart(sock):
    while True:
        msg = 'reqdata'
        sock.send(msg.encode('utf-8'))
        # print(msg)
        # time.sleep(0.1)

        if cmd_connect == 1 & data_connect == 1:
            break


def ReadCMD(sock):
    while True:
        time.sleep(0.01)
        global cmd_send_flag
        global bReadCmd
        global moveCmdFlag, moveCmdCnt
        # if cmd_connect == True & data_connect == True:
        #     break
        # msg = 'set_speed_bar(0.1)'
        # sock.send(msg.encode('utf-8'))

        if cmd_send_flag == 1:
            msg_recv = sock.recv(26)
            if msg_recv.decode('utf-8') == 'The command was executed\n':
                cmd_send_flag = 0
                bReadCmd = True

                if moveCmdFlag:
                    moveCmdCnt = 3
                    systemstat_global.robot_state = 3
                    moveCmdFlag = False

                bReadCmd = False

        if cmd_connect == 1 & data_connect == 1:
            print('b')
            break


def ReadDATA(sock):
    while True:
        msg_recv = sock.recv(580)

        if msg_recv[0] == 0x24:
            size = int((msg_recv[2] << 8) | msg_recv[1])
            if size <= len(msg_recv) - 4:
                if msg_recv[3] == 3:
                    msg_recv_split = msg_recv[4:512]
                    result = struct.unpack(
                        'fffffffffffffffffffffffffffffffffffffffiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiffffffiiiififiiffffffiiiiiiiiiiiffiiiifiiiiiiiiiiiffffff',
                        msg_recv_split)
                    global systemstat_global
                    systemstat = systemSTAT(result[0], result[1:7], result[7:13], result[13:19], result[19:25],
                                            result[25:31], result[31:35], result[35:39], result[39:55], result[55:71]
                                            , result[71:77], result[77], result[78], result[79], result[80], result[81],
                                            result[82], result[83], result[84], result[85], result[86:92]
                                            , result[92:98], result[98], result[99], result[100], result[101],
                                            result[102],
                                            result[103:105], result[105:107], result[107:109], result[109]
                                            , result[110], result[111], result[112], result[113], result[114],
                                            result[115:117], result[117:119], result[119:121], result[121], result[122]
                                            , result[123], result[124], result[125], result[126])
                    systemstat_global = systemstat
                elif msg_recv[3] == 4:
                    print('config')
                elif msg_recv[10] == 10:
                    print('popup')

        if cmd_connect == 1 & data_connect == 1:
            break


def SendCOMMAND(str, cmd_type):
    global cmd_send_flag
    global bReadCmd, moveCmdFlag
    str_space = str + ' '
    if cmd_type == CMD_TYPE.MOVE:
        while True:
            time.sleep(0.03)
            if IsIdle() & (bReadCmd == False):
                CMDSock.send(str_space.encode('utf-8'))
                moveCmdFlag = True
                cmd_send_flag = 1
                systemstat_global.robot_state = 3
                return True
            elif IsPause():
                return False
            else:
                print(".")
    else:
        CMDSock.send(str_space.encode('utf-8'))
        cmd_send_flag = 1
        return True


def IsIdle():
    return systemstat_global.robot_state == 1


def IsPause():
    return systemstat_global.op_stat_soft_estop_occur == 1


def IsInitialized():
    if systemstat_global.init_state_info == 6:
        return True
    else:
        return False


def IsRobotReal():
    if systemstat_global.program_mode == 0:
        return True
    else:
        return False


def IsCommandSockConnect():
    if not cmd_connect:
        # print('connect commmand')
        return True
    else:
        return False


def IsDataSockConnect():
    if not data_connect:
        # print('connect data')
        return True
    else:
        return False


def isValidIP(ip):
    ipsplit = ip.split(".")
    if (int(ipsplit[0]) < 0) | (int(ipsplit[1]) < 0) | (int(ipsplit[2]) < 0) | (int(ipsplit[3]) < 0):
        return False
    elif (int(ipsplit[0]) > 255) | (int(ipsplit[1]) > 255) | (int(ipsplit[2]) > 255) | (int(ipsplit[3]) > 255):
        return False
    else:
        return True


def GetCurrentCobotStatus():
    if systemstat_global.op_stat_soft_estop_occur == 1:
        return COBOT_STATUS.PAUSED

    if systemstat_global.robot_state == 1:
        return COBOT_STATUS.IDLE
    elif systemstat_global.robot_state == 3:
        return COBOT_STATUS.RUNNING
    else:
        return COBOT_STATUS.UNKNOWN


def ToCB(ip):
    if data_connect == False & cmd_connect == False:
        DisConnectToCB()
        print('disconnecting')
    elif data_connect == True & cmd_connect == True:
        ConnectToCB(ip)
        print('connecting')


print("                                    ")
print("      ,--.                     ,--. ")
print(",--.--|  |-.,-----.,--,--.,---.`--' ")
print("|  .--| .-. '-----' ,-.  | .-. ,--. ")
print("|  |  | `-' |     \ '-'  | '-' |  | ")
print( "`--'   `---'       `--`--|  |-'`--' ")
print( "                         `--'       ")