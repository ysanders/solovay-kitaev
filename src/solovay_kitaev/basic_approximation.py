from numpy import array, eye
from numpy.linalg import norm

from solo

class BaseCaseQuery():

    def __init__(self, *gates : list, depth=3, unique=True, norm_bound=1e-5):
        self.depth = depth
        self.gates = gates

        self.query_structure = None
        self.generate_query_structure(unique=unique)

        self.vector_norm = self.construct_vector_norm()
        
    def generate_query_structure(self, unique=True):
        '''
            generate_query_structure
            Generates an array of matricies and their decompositions
            :: unique : bool :: A flag to filter the array for unique approximations
            This flag increases the construction time but may result in a more efficient (read smaller) set of gates
            leading to performance improvements at query time.
        '''
        query_structure = []
        for approximation, construction in basic_approximation_generator(*self.gates, depth=depth):
 
            # Check if close approximation already exists    
            approximated = False
            if len(query_structure) > 0 or not self.unique: # If not unique then skip this check

                for extant_approximation, extant_construction in enumerate(query_structure):
                    # Compare Frobenius norm
                    if norm(approximation, extant_approximation, ord='fro') < self.norm_bound:
                        approximated = True
                        break
                    
            # Not found, insert as normal
            if not approximated:
                query_structure.append((approximation, construction))
            
        return query_structure


    def __call__(self, unitary : array:) -> tuple:
        '''
            __call__
            Calls the query method
            :: unitary : array :: Unitary for which we want to find the base approximation
            Returns a tuple of the approximate gate along with the gates required to construct it.
        '''
        self.query(unitary)

    def query(self, unitary : array) -> tuple:
    '''
        query
        Performs a query on the base case structure
        :: unitary :: Unitary to find the approximation of
        Returns a tuple of the approximate gate along with the gates required to construct it.
    '''
        pass

    
    def construct_vector_norm(self):
        def vector_norm(matrix_a : array, matrix_b : array):
            return np.norm(matrix_a, matrix_b, ord='fro')

def basic_approximation_generator(
        *gates, 
        depth = 3):
    '''
        basic_approximation_generator
        Enumerates through convex combinations of gates
        :: gates : list :: A list of numpy array representations of gates
        :: depth :: The depth of the enumeration
    '''
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


