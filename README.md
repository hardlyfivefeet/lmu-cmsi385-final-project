# LMU CMSI 385 Final Project

This repository contains a Python NFA simulator that takes in a description of an NFA (via STDIN) and a string (via command line arg) and returns whether or not the string is accepted in the language of the NFA passed in.

## Usage Scenario

Sample input NFA description:

```
START=q0;ACCEPT=q2,q1

q0:a->q1

q0:a->q2

q0->q2

q0:a->q0
```

To run the simulator for the string "aabbbbaa" and machine description "nfa_description.txt", run the following in the command line:

```
python3 NFASimulator.py aabbbbaa < nfa_description.txt
```

The simulator will then output whether or not the string "aabbbbaa" is accepted by the language of the NFA described in "nfa_description.txt".
