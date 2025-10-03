# Project description
This mini-firewall exercise was created as an assignment for the 3rd week of the Coding Bootcamp for Cybersecurity Professionals.</br>

**Goal**: Design a firewall that filters packets in batches and allows them through in a certain priority order.
- Packets are tuples (serial number, priority) 
- Serial numbers are ongoing from 1
- Priorities range from 1:10 with 1 being the highest priority

# How to run the program 
- **Required**: input from a csv file called 'input.csv'
- If there is no such input file: run `python create_input.py` from the command line to create an example 'input.csv' file with packets
- Expected input format: 1 packet (serial number, priority) per line
- Run `python main.py` from the command line to create batches with a priority order 
- **Output**: writes the newly ordered packets to an' output.csv' file, with one line per packet

# Features
- Program includes:
    -   Reading packet input from file and skipping lines with deviating formats (blank lines, comments, negative numbers, no numbers ...)
    -   Check if the input has the correct format for further processing  --> list of tuples [(int, int), (int, int)]
    -   Creating batches (default BATCH_SIZE=10) from the input list of packets
    -   Sorting packets in batches using a two pass quick sort algorythm (rule: highest priority and lowest serial nr first)
    

# Future improvement ideas

1.  Add output format variants
    - Either one line per packet "SerialNo, Priority" or a serial-only list
        - Currently 'per-packet lines': for each batch, for each packet (s, p), write "s, p" on its own line.
        - optional 'serial-only per batch': a single line with just the serials for each batch (e.g., 3,10,2,4,1,9,5,6) 
    
2.  Introduce output variant CLI options
    -   Offer a serial-only output or print to stdout as an alternative to make testing easier
    -   CLI options: --input, --output, and an optional --serial-only or --stdout mode 
    
3. Simpler and safer comparator 
    -   Replace the two-pass quicksort with Python’s built-in stable sort using a single key to make the intent explicit and avoid relying on sort stability nuances ( `sorted(batch, key=lambda x: (x[1], x[0]))`)
    - Note: used quick sort algorythm to test the function introduced in the bootcamp

3. Improve create_input.py script to include edge cases 

4. Implement systematic testing of edge cases
    

# Disclaimer
This is a WIP, I am still learning (Oktober 2025)