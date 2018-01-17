ListSplit
=========
The ListSplit block takes an incoming signal containing a list and splits that list into individual signals per element.

Properties
----------
- **dict_att**: Name of the attribute the list element is assigned to on the outgoing signal.
- **list_att**: The signal attribute containing the list to be split on the incoming signal.

Inputs
------
- **default**: Any list of signals containing a list.

Outputs
-------
- **default**: A signal per list element on the incoming signal.

Commands
--------
None

Example
-------
`incoming_signal = {"List": [1, 2, 3]}`  
`outgoing_signal_1 = {"Attr": 1}`  
`outgoing_signal_2 = {"Attr": 2}`  
`outgoing_signal_3 = {"Attr": 3}`  

