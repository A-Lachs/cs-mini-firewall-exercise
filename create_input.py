import random
import csv

# TASK: create input file with packets 
# packets include a serial number (1-10) and a priority (1-10)

NR_PACKETS = 50
FILE_NAME_INPUT = "input.csv"


def generate_packets(number_of_packets=NR_PACKETS, ongoing=False):
    """
    Create a list of n packages, with n defined by number_of_packages.
    Each package is a tuple (serial_bumber, priority)
    - where serial_number is an int from 1 to 10 (ongoing=False) or 1 to NR_PAckets (ongoning=True)
    - where priority is a random int from 1 to 10. 
    
    Args:
        number_of_packets (int, optional): Defaults to NR_PACKETS.

    Returns:
        list of tuples: packages = [(serial_number, priority), ...]
    """
    packets = []
    serial_number = 0

    if not ongoing: # use serial nr 1-10

        for packet in range(1, number_of_packets+1):
            # define first batch of 10 packages
            if serial_number < 10:
                serial_number += 1
                priority = random.randint(1,10) 
                # print(packet, serial_number, priority)
                packets.append((serial_number, priority)) # use serial nr 1-10
            
            else:
                serial_number = 0 # reset serial nr for next batch

    else: # use ongoing serial nrs

        for packet in range(1, number_of_packets+1):
                priority = random.randint(1,10) 
                # print(packet, serial_number, priority)
                packets.append((packet, priority)) # use ongoing serial nr
     
    return packets


def input_to_csv(packets_list, file_name=FILE_NAME_INPUT):
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        writer=csv.writer(f, skipinitialspace=True)
        # write header
        writer.writerow(["serial_number", "priority"])
        # write data
        [writer.writerow(packet) for packet in packets_list]
     
# ----------------------------------- test input ----------------------------

new_p = generate_packets(ongoing=True)
print(new_p)
print(type(new_p[0][0]))
input_to_csv(new_p)



# TODO: create faulty input 

