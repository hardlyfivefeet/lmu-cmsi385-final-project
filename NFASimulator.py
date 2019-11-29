from NFA import NFA
import sys

def add_transition(state, action, new_state):
    if state in transition_function:
        transitions = transition_function[state]
        if action in transitions:
            # f this action already exists for the state but the action doesn't go to new_state
            if not new_state in transitions[action]:
                transitions[action].append(new_state)
        else:
            transitions[action] = new_state
    else:
        transition_function[state] = {action: [new_state]}


description_lines = []
transition_function = {} # stores keys of states, and values of dictionary {action: [new_state]}
start_state = []
accept_states = []

# Format input lines, remove whitespace and semicolons
input_lines = sys.stdin.read().splitlines()
for line in input_lines:
    if ";" in line:
        line1, line2 = line.split(";")
        description_lines.append(line1)
        description_lines.append(line2)
    elif line:
        description_lines.append(line)

# translate input lines into machine description
for line in description_lines:
    if ":" in line:
        state, rhs = line.split(":")
        action, new_state = rhs.split("->")
        add_transition(state, action, new_state)
    if "->" in line and ":" not in line:
        state, new_state = line.split("->")
        add_transition(state, "", new_state)
    if "START" in line:
        _, start_state = line.split("=")
    if "ACCEPT" in line:
        _, accepted = line.split("=")
        accept_states = accepted.split(",")

print(transition_function)
print(start_state)
print(accept_states)
