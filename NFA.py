class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def transition(self, state, a):
        if state in self.transitions:
            if a in self.transitions[state]:
                return set(self.transitions[state][a])
        return set()

    def accept(self, string):
        # initialize a list of current_states
        current_states = set()
        # if string is empty:
        if not string:
            # if there is a lambda move from the start state, put the new state(s) in current_states
            new_states = self.transition(self.start_state, "")
            if len(new_states) != 0:
                current_states.update(new_states)
        else:
            current_states.add(self.start_state)
            for char in string:
                if len(current_states) == 0:
                    break
                else:
                    # add states that you can get to with lambda moves into current_states
                    for state in current_states:
                        lambda_move_states = self.transition(state, "")
                    current_states.update(lambda_move_states)
                    new_states = set()
                    for state in current_states:
                        new_states.update(self.transition(state, char))
                    current_states = new_states
        # check if current_states contain goal state
        for accept_state in self.accept_states:
            if accept_state in current_states:
                return True
        return False
