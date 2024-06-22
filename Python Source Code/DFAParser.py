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
    