#****************************************************************************************************************************
#                                                                                                                           *
#      - The DFAParser class provides static methods to parse DFA definitions from different sources                        *
#      - It includes methods to parse from a file, a JSON string, a dictionary, or a text file with a specific format.      *
#      - These methods extract states, alphabet, start state, accept states, and transition function from the input         *
#        data and create an instance of the DFA class using this information.                                               *
#                                                                                                                           *
#****************************************************************************************************************************



import json
from DFA import DFA


class DFAParser:
    @staticmethod
    def parse_from_file(file_path):
        """
            Parse DFA definition from a file.

                - param file_path: Path to the DFA definition file.
                - return: An instance of DFA.
        """
        with open(file_path, 'r') as file:
            dfa_data = json.load(file)
        return DFAParser.parse_from_dict(dfa_data)
    
    @staticmethod
    def parse_from_string(dfa_string):
        """
            Parse DFA definition from a JSON string.

                - param dfa_string: JSON string containing DFA definition.
                - return: An instance of DFA.
        """
        dfa_data = json.loads(dfa_string)
        return DFAParser.parse_from_dict(dfa_data)
    
    @staticmethod
    def parse_from_dict(dfa_data):
        """
            Parses DFA definition from a dictionary.

                - param dfa_data: Dictionary containing DFA definition.
                - return: DFA instance.
        """
        states = set(dfa_data['states'])                                              # Extract states.
        alphabet = set(dfa_data['alphabet'])                                          # Extract alphabet.
        # Parse transition function from dictionary.
        transition_function = {(state, symbol): next_state for state, symbol, next_state in dfa_data['transition_function']}
        start_state = dfa_data['start_state']                                         # Extract start state.
        accept_states = set(dfa_data['accept_states'])                                # Extract accept states.
        return DFA(states, alphabet, transition_function, start_state, accept_states)
    
    @staticmethod
    def parse_from_text_file(file_path):
        """
            Parses DFA definition from a text file with specific format.

                - param file_path: Path to DFA definition text file.
                - return: DFA instance.
        """
        with open(file_path, 'r') as file:                                          # Read lines from the text file
            lines = file.readlines()
        states = set(lines[0].strip().split())                                      # Extract states
        alphabet = set(lines[1].strip().split())                                    # Extract alphabet
        start_state = lines[2].strip()                                              # Extract start state
        accept_states = set(lines[3].strip().split())                               # Extract accept states
        transition_function = {}
        for line in lines[4:]:                                                      # Parse transition function
            state, symbol, next_state = line.strip().split()
            transition_function[(state, symbol)] = next_state
        return DFA(states, alphabet, transition_function, start_state, accept_states)
    