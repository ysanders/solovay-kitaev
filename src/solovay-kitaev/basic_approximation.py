from numpy import array, eye

def basic_approximation_generator(
        unitary : array,
        *gates, 
        depth = 3):
   
    # Dimension of operator
    # Currently probably 2; need to add combinations to single qubit gates
    if len(gates) == 0:
        raise IndexError("No gates provided to basic approximation")
    matrix_rank = gates[0].shape[0]

    # Space of all sequences
    for i in range(len(gates) ** depth):
          
        # Convert sequence to set of gates
        integer_representation = i
        current_combinations = []
    
        # Perform a basis change to the number of gates
        current_power = 1
        while integer_representation != 0:
            
            # Split on individual digits and append appropriate gate 
            current_combination.append(
                    gates[
                        int(integer_representation 
                            % (base ** current_power) 
                            // (base ** (current_power - 1))
                            )
                        ]
                    )

            integer_representation -= integer_representation % (base ** current_power)
            current_power += 1

        # There needs to be a nicer way to express this
        base_approximation = eye(matrix_rank)
    
        for gate in current_combination:
            base_approximation = gate @ base_approximation

        yield base_approximation, current_combination
