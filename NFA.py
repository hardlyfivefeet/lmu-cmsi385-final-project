import copy

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def update_states_for_lambda_moves(self, current_states):
        states_to_consider = list(copy.deepcopy(current_states))
        updated_current_states = set()
        while len(states_to_consider) > 0:
            for state in states_to_consider:
                if not state in updated_current_states and state in self.transitions:
                    if "" in self.transitions[state]:
                        states_to_consider.extend(self.transitions[state][""])
                updated_current_states.add(state)
                states_to_consider.remove(state)
        return updated_current_states

    def transition(self, state, a):
        if state in self.transitions:
            if a in self.transitions[state]:
                return set(self.transitions[state][a])
        return set()

    def accept(self, string):
        current_states = set()
        # if the input string is empty
        if not string:
            # if there is a lambda move from the start state, put the new state(s) in current_states
            current_states.update(self.transition(self.start_state, ""))
        else:
            current_states.add(self.start_state)
            for char in string:
                if len(current_states) == 0:
                    break
                else:
                    updated_current_states = self.update_states_for_lambda_moves(current_states)
                    new_states = set()
                    for state in updated_current_states:
                        new_states.update(self.transition(state, char))
                    current_states = self.update_states_for_lambda_moves(new_states)
        for accept_state in self.accept_states:
            if accept_state in current_states:
                return True
        return False
