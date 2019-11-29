class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def accept(self, string):
        # initialize a list of current_states
        # initialize current_state_under_consideration
        # put the start state into current_states
        # if string is empty:
            # if there is a lambda move from the start state, put the new state(s) in current_states
        # else
            # for each char in the string
                # if current_states is empty, break
                # else, for each state in current_states
                    # current_state_under_consideration = state
                    # remove state from current states
                    # check if there is a transition from current_state_under_consideration for this char
                        # if there isn't, don't do anything
                        # else, add the new state(s) into current_states (if they aren't already in there)
                    # also check if there is a lambda move for current_state_under_consideration
                        # if there isn't, don't do anything
                        # else, add the new state(s) into current_states (if they aren't already in there)
        # check if current_states contain goal state
            # if yes, return true
        return false
