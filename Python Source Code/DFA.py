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
    
    def validate_dfa(self):
        """
            Validate the DFA to ensure that it meets all necessary conditions.
        """
        if self.start_state not in self.states:
            raise ValueError(f"Start state {self.start_state} is not in states")
        if not self.accept_states.issubset(self.states):
            raise ValueError("Some accept states are not in the set of states")
        for (state, symbol), next_state in self.transition_function.items():
            if state not in self.states:
                raise ValueError(f"State {state} in transition function is not in states")
            if symbol not in self.alphabet:
                raise ValueError(f"Symbol {symbol} in transition function is not in alphabet")
            if next_state not in self.states:
                raise ValueError(f"Next state {next_state} in transition function is not in states")
    
    def reset(self):
        """
            Reset the DFA to the start state.
        """
        self.current_state = self.start_state
        self.history = []
    
    def transition(self, state, symbol):
        """
            Get the next state from the transition function.

                - param state: The current state.
                - param symbol: The input symbol.
                - return: The next state.
        """
        if (state, symbol) in self.transition_function:
            next_state = self.transition_function[(state, symbol)]
            self.history.append((state, symbol, next_state))
            return next_state
        else:
            raise ValueError(f"No transition defined for state {state} on symbol {symbol}")
    
    def process_string(self, input_string):
        """
            Process an input string through the DFA.

                - param input_string: The input string to process.
                - return: True if the string is accepted, False otherwise.
        """
        self.reset()
        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"Symbol {symbol} is not in the alphabet")
            self.current_state = self.transition(self.current_state, symbol)
        return self.current_state in self.accept_states
    
    def is_accepting(self):
        """
            Check if the current state is an accepting state.

                - return: True if the current state is an accepting state, False otherwise.
        """
        return self.current_state in self.accept_states
    
    def print_dfa(self):
        """
            Print the DFA components.
        """
        print("States:", self.states)
        print("Alphabet:", self.alphabet)
        print("Transition Function:")
        for (state, symbol), next_state in self.transition_function.items():
            print(f"  δ({state}, {symbol}) -> {next_state}")
        print("Start State:", self.start_state)
        print("Accept States:", self.accept_states)
    
    def get_history(self):
        """
            Get the history of transitions.

                - return: A list of transitions (state, symbol, next_state).
        """
        return self.history
    
    def get_language(self):
            """
                Generates the accepted language of the DFA. Basic version, can be optimized or extended.

                    - return: Set of strings accepted by the DFA.
            """
            
            def dfs(current_state, current_string, visited):                          # Depth-first search function to traverse the DFA states
                if current_state in visited:                                          # Avoid revisiting states
                    return
                visited.add(current_state)
                if current_state in self.accept_states:                               # If the current state is an accept state, add the current string to the language
                    language.add(current_string) 
                
                for symbol in self.alphabet:                                          # Depth-first search function to traverse the DFA states
                    next_state = self.transition_function.get((current_state, symbol))
                    if next_state:
                        dfs(next_state, current_string + symbol, visited.copy())      # Recursively explore the next state

            language = set()
            dfs(self.start_state, '', set())                                          # Start DFS from the initial state with an empty string
            return language
    
    def check_input_language(self, input_string):
        """
            Check if the input string belongs to the language defined by the DFA.

                - param input_string: The input string to check.
                - return: True if the input string is part of the language, False otherwise.
        """
        try:
            return self.process_string(input_string)
        except ValueError:
            return False
    