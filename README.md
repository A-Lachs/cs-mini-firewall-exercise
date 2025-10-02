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
    - Check if the input has the correct format for further processing  --> list of tuples [(int, int)]
    - Creating batches (BATCH_SIZE=10) from the input list of packets
    - Sorting packets in batches using quick algorythm (highest prio priority and lowest serial nr first)
    - Writing sorted batches to 'output.csv' with one line for each batch

# Future improvement ideas

1. Improve parsing to include more input file variants
    - Skip blank and comment lines
    - Accept other delimiters (commas and white space)
    - wrap int parsing in try/except to continue on malformed rows

2. Introduce output variants 
    - offer a serial-only output or print to stdout as an alternative to match accepted output formats (idea: add a small CLI flag e.g., --serial-only)

3. Improve create_input.py script to introduce edge cases 
    - implement systematic testing of edge cases
    

# Disclaimer
This is a WIP, I am still learning (Oktober 2025)