import random
import csv

# TASK: create input file with packets 
# Packets include a serial number (1 to N) and a priority (1 to 10)

N_PACKETS = 50
HIGHEST_PRIORITY = 1
LOWEST_PRIORITY = 10
BATCH_SIZE=10
FILE_NAME_INPUT = "input.csv"


def generate_packets(number_of_packets=N_PACKETS, ongoing=True):
    """
    Create a list of n packets.
    Each packet is a tuple (serial_number, priority)
    - where serial_number is an int from 1 to 10 (ongoing=False) or from 1 to N_PACKETS (ongoning=True)
    - where priority is a random int from HIGHEST_PRIORITY to LOWEST_PRIORITY. 
    
    Args:
        number_of_packets (int, optional): Defaults to N_PACKETS.

    Returns:
        list of packetes(int, int) = [(serial_number, priority), ...]
    """
    packets = []
    serial_number = 0

    if not ongoing: # use serial nr 1-10

        for packet in range(1, number_of_packets+1):
            # define first batch of 10 packages
            if serial_number < BATCH_SIZE:
                serial_number += 1
                priority = random.randint(HIGHEST_PRIORITY,LOWEST_PRIORITY) 
                # print(packet, serial_number, priority)
                packets.append((serial_number, priority)) # use serial nr 1-10
            
            else:
                serial_number = 0 # reset serial nr for next batch

    else: # use ongoing serial nrs

        for packet in range(1, number_of_packets+1):
                priority = random.randint(HIGHEST_PRIORITY,HIGHEST_PRIORITY) 
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


if __name__ == "__main__":

    new_packets = generate_packets(number_of_packets=N_PACKETS, ongoing=True)
    input_to_csv(new_packets)


