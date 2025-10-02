# Project description
This mini-firewall exercise was created as an assignment for the 3rd week of the Coding Bootcamp for Cybersecurity Professionals.</br>

Goal: Design a firewall that filters packets in batches and allows them through in a certain priority order.
- Packets are tuples (serial number, priority) 
- Serial numbers are ongoing
- Priorities range from 1:10 with 1 being the highest priority

# Features 
- Run `python main.py` from the command line to create batches with a priority order 
- **Required**: input from a csv file called 'input.csv'
- If there is no such input file: run `python create_input.py` from the command line to create an  example 'input.csv' file with packets
- Program includes:
    -   Check if the input has the correct format for further processing  --> list of tuples [(int, int)]
    -   Creating batches (BATCH_SIZE=10) from the input list of packets
    -   Sorting packets in batches using quick algorythm (highest prio priority and lowest serial nr first)
    -   Writing sorted batches to 'output.csv' with one line for each batch

# Future improvement ideas

1.  Change Output formats
    - Before: one batch per line
    - Expected: either one line per packet "SerialNo, Priority" or a serial-only list
        - NOW: **Option A** (per-packet lines): for each batch, for each packet (s, p), write "s, p" on its own line.
        - **Option B** (serial-only per batch): write a single line with just the serials for each batch (e.g., 3,10,2,4,1,9,5,6) 
    
2.  Introduce output variants and CLI options
    -   Offer a serial-only output or print to stdout as an alternative to make testing easier
    -   Add a CLI option: --input, --output, and an optional --serial-only or --stdout mode to match the “serials-only” accepted variant 
    
3. Simpler and safer comparator 
    -   replace the two-pass quicksort with Python’s built-in stable sort using a single key to make the intent explicit and avoid relying on sort stability nuances.
    -   e.g., `sorted(batch, key=lambda x: (x[1], x[0]))`

3. Improve create_input.py script to include edge cases 

4. Implement systematic testing of edge cases
    

# Disclaimer
This is a WIP, I am still learning (Oktober 2025)