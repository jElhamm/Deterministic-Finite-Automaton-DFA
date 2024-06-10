# ********************************************************************************************************************************
#                                                                                                                                *
#       - The DFA class represents a Deterministic Finite Automaton.It is initialized with parameters including a                *
#         set of states, input symbols (alphabet), transition function, start state, and accept states.                          *
#                                                                                                                                *
#       - The class provides methods to validate the DFA, process input strings, check if the current state is                   *
#         accepting, print DFA components, retrieve transition history, generate the language accepted by the DFA,               *
#         and check if an input string belongs to the DFA's language.                                                            *
#                                                                                                                                *
#       - The get_language method generates the language accepted by the DFA using a depth-first search (DFS) algorithm.         *
#                                                                                                                                *
# ********************************************************************************************************************************



class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        """
            Initialize the DFA with the given parameters.

                - param states: A set of states.
                - param alphabet: A set of input symbols.
                - param transition_function: A dictionary representing the transition function.
                - param start_state: The start state.
                - param accept_states: A set of accept states.
        """
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        self.history = []
        self.validate_dfa()
    