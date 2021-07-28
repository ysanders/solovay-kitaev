from numpy import array, eye

class BaseCaseQuery():

    def __init__(self, *gates : list, depth=3):
        self.depth = depth
        self.generate_query_structure()
        self.gates = gates


    def generate_query_structure(self):
        

        for approx, construction in basic_approximation_generator(*self.gates, depth=depth)



    def __call__(self, unitary : array:) -> tuple:
        self.query(unitary)

    def query(self, unitary : array) -> tuple:
    '''
        query
        Performs a query on the base case structure
        :: unitary :: Unitary to find the approximation of
        Returns a tuple of the approximate gate along with the gates required to construct it.
    '''
        


def basic_approximation_generator(
        *gates, 
        depth = 3):
   
    # Dimension of operator
    # Currently probably 2; need to add combinations to single qubit gates
    if len(gates) == 0:
        raise IndexError("No gates provided to basic approximation")
    matrix_rank = gates[0].shape[0]

    # Space of all sequences
    base = len(gates)
    for i in range(base ** depth):
          
        # Convert sequence to set of gates
        integer_representation = i
        current_combination = []
    
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



