#****************************************************************************************************************************
#                                                                                                                           *
#       This code defines a DFA using a JSON string, parses it, and then tests various input strings against the DFA.       *
#                            Finally, it prints the results of the tests and transitions.                                   *
#                                                                                                                           *
#****************************************************************************************************************************



from DFAParser import DFAParser


# This function provides a summary of the code and an example of its usage.
def banner():
    print("""

********************************************************************************************************************
*                                                                                                                  *
*                                     Deterministic Finite Automaton (DFA)                                         *
*                                                                                                                  *
*       The DFA class represents a Deterministic Finite Automaton with methods to validate, process strings,       *
*         and check if input strings belong to the language defined by the DFA. DFAParser provides methods         *
*                       to parse DFA definitions from files, strings, or dictionaries.                             *
*                                                                                                                  *
*                                                                                                                  *
*       ## Example usage:                                                                                          *
*                       - Parsing a DFA from a JSON string:                                                        *
*                                                                                                                  *
*                       a) dfa_definition = '{"states": ["q0", "q1", "q2"], ...}'                                  *
*                                                                                                                  *
*                       b) dfa = DFAParser.parse_from_string(dfa_definition)                                       *
*                                                                                                                  *
********************************************************************************************************************
    """)


def main():
    banner()
    # DFA definition in JSON format (as a string for this example)
    dfa_definition = '''
    {
        "states": ["q0", "q1", "q2"],
        "alphabet": ["0", "1"],
        "transition_function": [
            ["q0", "0", "q1"],
            ["q0", "1", "q0"],
            ["q1", "0", "q2"],
            ["q1", "1", "q0"],
            ["q2", "0", "q2"],
            ["q2", "1", "q2"]
        ],
        "start_state": "q0",
        "accept_states": ["q2"]
    }
    '''

    dfa = DFAParser.parse_from_string(dfa_definition)                                 # Parse the DFA from the JSON string
    dfa.print_dfa()                                                                   # Print the DFA components
    # -----------------------------------------------------------------------------------------------------------------------------
    
    input_string = "001"                                                              # Test the DFA with an input string
    if dfa.process_string(input_string):
        print(f"    - The string '{input_string}' is accepted by the DFA.")
    else:
        print(f"    - The string '{input_string}' is not accepted by the DFA.")

    print("\n********************************************************************************************************************")
    print("\n ## History of transitions and current state:")                              # Print the history of transitions and the current state
    for transition in dfa.get_history():
        print(f"  δ({transition[0]}, {transition[1]}) -> {transition[2]}")
    print(f"\nCurrent state: {dfa.current_state}")
    
    print("\n********************************************************************************************************************")
    print("\n ## Language accepted by the DFA:", dfa.get_language())                      # Print the language accepted by the DFA
    if dfa.check_input_language(input_string):                                        # Check if a string belongs to the language
        print(f"    - The string '{input_string}' is in the language of the DFA.")
    else:
        print(f"    - The string '{input_string}' is not in the language of the DFA.")

    input_string = "010101"                                                           # Test with another input string
    if dfa.process_string(input_string):
        print(f"\n    - The string '{input_string}' is accepted by the DFA.")
    else:
        print(f"\n    - The string '{input_string}' is not accepted by the DFA.")

    print("\n********************************************************************************************************************")
    print("\n ## Updated history of transitions and current state:")                      # Print the updated history of transitions and the current state
    for transition in dfa.get_history():
        print(f"  δ({transition[0]}, {transition[1]}) -> {transition[2]}")
    print(f"\nCurrent state: {dfa.current_state}")

    print("\n********************************************************************************************************************")
    invalid_input_string = "012"                                                      # Example of checking an invalid string
    try:
        if dfa.check_input_language(invalid_input_string):
            print(f"\n    - The string '{invalid_input_string}' is in the language of the DFA.")
        else:
            print(f"\n    - The string '{invalid_input_string}' is not in the language of the DFA.")
    except ValueError as e:
        print(f"\nError: {e}")

    long_input_string = "000111000"                                                   # Example of using a longer string
    if dfa.process_string(long_input_string):
        print(f"\n    - The string '{long_input_string}' is accepted by the DFA.")
    else:
        print(f"\n    - The string '{long_input_string}' is not accepted by the DFA.")

    print("\n********************************************************************************************************************")
    print("\n ## Program finished.")                                                      # End of program
    print("\n********************************************************************************************************************\n")


if __name__ == "__main__":
    main()
    