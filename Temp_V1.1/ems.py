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
processed_addresses = set()

kwh_data = 0
unit = "KWH"
access = False

def read_hmi_doller_addresses():
    # Read all HMI_DOLLER addresses from the text file
    with open("/home/pi/Temp_V1.1/data_files/hmi_address_file.txt", "r") as file:
        addresses = [int(line.strip()) for line in file]

    return addresses

def energy_data_update1():
    ip_address = "172.16.4.235"
    client = ModbusTcpClient(ip_address, port=502)
    client.connect()

    global kwh_data
    global unit
    global processed_addresses

    try:
        while True:
            hmi_doller_addresses = read_hmi_doller_addresses()

            with open("/home/pi/Temp_V1.1/data_files/hmi_output_file.txt", "r+") as output_file:
                lines = output_file.readlines()
                output_file.seek(0)
                
                for hmi_doller_address in hmi_doller_addresses:
                    data = client.read_holding_registers(hmi_doller_address, 2, slave=1)
                    if not data.isError():
                        decoder = BinaryPayloadDecoder.fromRegisters(data.registers, Endian.Big, wordorder=Endian.Little)
                        address_result = decoder.decode_32bit_float()
                        string_convert = str(address_result)
                        length_of_number = len(string_convert)

                        round_value = round(address_result)
                        kwh = round_value
                        kwh_data = kwh
                        unit = "KW"
                        result_line = f"{kwh_data}\n"
                        print(result_line)
                        output_file.writelines(result_line)
                        processed_addresses.add(hmi_doller_address)
                    else:
                        print(f"Error reading from address {hmi_doller_address}")
                output_file.truncate()

            time.sleep(1)

    except KeyboardInterrupt:
        print("Thread stopped by user.")

update_thread = threading.Thread(target=energy_data_update1)
update_thread.start()
update_thread.join()

