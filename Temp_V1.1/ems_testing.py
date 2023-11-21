from flask import Flask, jsonify, render_template ,request ,send_file
from gpiozero import CPUTemperature
import threading
from threading import Thread
from datetime import datetime
import time
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client import ModbusSerialClient
from pymodbus.client import ModbusTcpClient
import os.path
import io

global kwh_data
global unit

kwh_data = 0
unit ="KWH"
access=False

def energy_data_update1():
        ip_address ="172.16.4.235"
        HMI_Doller_Address1 = 746
        client = ModbusTcpClient(ip_address,port = 502)
        client.connect()
        global kwh_data
        global unit
        data1 = client.read_holding_registers(HMI_Doller_Address1 , 2 , slave = 1)
        if not data1.isError():
            decoder1 = BinaryPayloadDecoder.fromRegisters(data1.registers,  Endian.Big, wordorder=Endian.Little)
            address_result1   = decoder1.decode_32bit_float()
            string_convert1   = str(address_result1)
            length_of_number1 = len(string_convert1)
            print ("The Register Address Value Is :  ",(address_result1))
            print("Total Length Of Character : ",(length_of_number1))
            Round_Value1 = round(address_result1)
            kwh1 = Round_Value1
            kwh_data1=kwh1
            unit1="KW"
            print ("1 :",kwh_data1)
        else :
             print ("ERROR")
energy_data_update1()
