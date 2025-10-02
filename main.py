import csv
import os

# ------------------------------------ constants ------------------------------------

FILE_NAME_INPUT = "input.csv"
FILE_NAME_OUTPUT = "output.csv"
BATCH_SIZE = 10 #  batch size of packets to be processed
VERBOSE = 0     #  enable additional print statements with 1, disable  with 0


# ------------------------------ utility functions -----------------------------------

def read_from_csv(file_path=FILE_NAME_INPUT) -> list[tuple]:
    """
    From a csv file read packets in the format serial_nr, priority.
    Return a list of tuples.

    Version 1. Not optimized for edge cases.
    """
    if not os.path.exists(file_path):
        print(f"\n-There is no file '{file_path}' to read from.")
        return 
    
    input_data = []

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header if present
        for row in reader:
        
            #read each line as a tuple, convert to int -> (int, int) and append to list
            input_data.append((int(row[0].strip()), int(row[1].strip())))
    
    print(f"\n+++ Reading {len(input_data)} packets from '{file_path}'." )

    return input_data


def read_from_file(file_path=FILE_NAME_INPUT) -> list[tuple]:
    """
    From a file read packets.
    Assumes 1 packet per line with 2 int values: serial_nr, priority. 
    Return a list of tuples.

    Version 2. Optimized:
        - Skips blank or comment line (starting with #)
        - Accepts blank space and comma seperators
        - Checks for number of values = 2 per row 
        - Test for int conversion (otherwise skips)
        - Test vor value range (both values must be positive and the second not larger than 10)
    """
    if not os.path.exists(file_path):
        print(f"\n-There is no file '{file_path}' to read from.")
        return 
    
    input_data = []

    with open(file_path, "r", encoding="utf-8") as f:
        
        for row in f:
            # go though muliple check per row
            row=row.strip()

            # skip blank lines or comment lines starting with #
            if not row or row.startswith("#"):
                continue

            # split line: try comma first, otherwise split on whitespace
            if "," in row:
                parts = row.split(",")
            else:
                parts = row.split()
            
            # sanity check: must have exactly 2 values
            if len(parts) != 2:
                # print(f"Skipping row: expected 2 values, got {len(parts)}")
                continue 

            # try int conversion
            try: 
                a, b = int(parts[0]), int(parts[1])

                # additionally check range a and b have positive values, and b is max 10
                if a <= 0 or b <= 0 or b > 10:
                    # print(f"Skipping row: out-of-range values ({parts})")
                    continue  
                
                # append the row to input_data
                input_data.append((a,b))

            except ValueError:
                #print(f"Skipping row: invalid integers ({parts})")
                continue
    
    print(f"\n+++ Reading {len(input_data)} packets from '{file_path}'." )

    return input_data



def input_valid(input_data:list) -> bool:
    """
    Check if input_data has the correct format for further processing.

    Args:
        input_data (list of tuples): Format [(int, int), (int, int)]

    Returns:
        bool: Return false if not valid and true otherwise
    """

    if not isinstance(input_data, list):
        print("\n- Input data is not a list")
        return False
    
    for packet in input_data:
        if not isinstance(packet, tuple):
            print("\n- Packet is not a tuple.")
            return False
        if len(packet) != 2:
            print("\n- Packet is not of size 2.")
            return False
        if not all(isinstance(x, int) for x in packet):
            print("\n- Not all packet info is an int.")
            return False
        
    return True

def create_batches(input_data:list, batch_size=BATCH_SIZE, verbose=1)-> list:
    """
    From list of input data with packets, create a new list of packets in batches.
    Use indexing to slice batches of size batch_size and return a new list with batched_data.

    Args:
        input_data ([(int,int), (int,int)]): List of packets that are tuples(int, int).
        batch_size (int, optional): Number of packets in a batch. Defaults to BATCH_SIZE.
    """
    all_packages = len(input_data)             # nr of packets
    full_batches = len(input_data)//batch_size # nr of full batches
    last_batch = len(input_data)%batch_size    # nr of pakets in last batch
    
    batched_data=[]
    j=0
    for i in range(full_batches):
        # go through indexes for all subsequent full batches
        j += batch_size
        # print(f"Indexes: {i*10}, {j}"")
        batched_data.append(input_data[i*batch_size: j])

    # add the last incomplete batch if there is one
    if last_batch:
        batched_data.append(input_data[j:])

    print(f"\n+++ Created {full_batches} batches of {batch_size} packets plus {last_batch} packets. ")

    return batched_data

 
def quick_sort(current_batch:list, sort_by:int, verbose=VERBOSE)-> list:
    """
    Sort a batch of packets (int, int) using quick sort.
    Sort_by = 0 --> sorting paket[0] by serial number (smallest first)
    Sort_by = 1 --> sorting paket[1] by priority (highest first), range 1(high) to 10(low)

    Args:
        current_batch (list):   list of packets (int, int) 
        sort_by (int):          0 or 1. 
                                packet[0] --> Sort by serial number 
                                packet[1] --> Sort by priority
        verbose (int, optional): en- or disable additional print statements. Defaults to VERBOSE.

    Returns:
        list: Sorted batch of pakets (int, int)
    """
  
    # Case 1: already sorted if the array has 0 or 1 elements
    if len(current_batch) <= 1:
        # print(f"{indent}Returning {current_batch} (already sorted)")
        return current_batch
    
    # Choose pivot point (= middle packet of current batch)
    pivot = current_batch[len(current_batch) // 2]
     
    # Partition step
    left = [x for x in current_batch if x[sort_by] < pivot[sort_by]]
    middle = [x for x in current_batch if x[sort_by] == pivot[sort_by]]
    right = [x for x in current_batch if x[sort_by] > pivot[sort_by]]
    
    if verbose:
        
        indent="    " # readability in print statements
        print(f"\n\n{indent}- Pivot chosen: {pivot} from {current_batch}")   
        print(f"{indent}- Partitions: ")  
        print(f"{indent*2}Left: {left}\n{indent*2}Middle: {middle}\n{indent*2}Right: {right}")
    
    # Recursively apply quicksort to left and right, combine results
    return quick_sort(left, sort_by,verbose=VERBOSE) + middle + quick_sort(right, sort_by, verbose=VERBOSE)


def sort_batches(batched_input:list) -> list:
    """
    Idea: Frist use quick sort to sort by serial nr --> packet[0] and then by priority --> packet[1]
    Result: the packages with the highest prio and smallest serial nr are queued first

    Args:
        batched_input (list of batches): batches = lists of unsorted packets(int, int)

    Returns:
        list: (list of batches): batches = lists of sorted packets(int, int)
    """

    print("\n+++ Sorting batches...")
    sorted_input = []

    for batch in batched_input:
        sort_step_1 = quick_sort(batch,0)
        sort_step_2 = quick_sort(sort_step_1,1)
        sorted_input.append(sort_step_2)

    return sorted_input


def output_to_csv(sorted_output, file_name=FILE_NAME_OUTPUT):
    """ Write output to .csv file with one sorted batch of packets per line.

    Args:
        sorted_output (list of lists): list contains lists that are batches of packets.
        file_name (str, optional): output file name. Defaults to FILE_NAME_OUTPUT.
    """
        
    with open(file_name, "w", encoding="utf-8", newline="") as f: 
        # write data
        for batch in sorted_output:
            #f.write(str(batch) + "\n") # remove ""  for each batch
            f.write(", ".join(str(t) for t in batch) + "\n")   # remove []  for each batch
    print(f"\n+++ Writing {len(sorted_output)} sorted batches to '{file_name}'.")
        
# --------------------------------- main program  -----------------------------------


if __name__ == "__main__":

    # try to read in input 
    new_input = read_from_file()

    # continue if there is inpur 
    if new_input:

        # continue if the input has the correct format
        if input_valid(new_input):
            batches = create_batches(new_input)
            sorted_batches = sort_batches(batches)

            # save the sorted batches in output file
            output_to_csv(sorted_batches)


