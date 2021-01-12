class Rtm:
    def __init__(self):
        # As próximas 3 variáveis servem apenas para checagem
        self.states = []
        self.input_alphabet = []
        self.output_alphabet = []

        self.tapes = {
            'input': [],
            'history': [],
            'output': []
        }
        self.heads = {
            'input': 0
        }
        self.current_state = None
        self.final_state = None
        self.transitions = []
        self.blank = 'B'

    class Transition:
        def __init__(self, from_state, input_symbol, to_state, output_symbol, shift_direction):
            self.from_state = from_state
            self.input_symbol = input_symbol
            self.to_state = to_state
            self.output_symbol = output_symbol
            self.shift_direction = shift_direction

        def _print(self):
            print("from_state: ", self.from_state) 
            print("input_symbol: ", self.input_symbol)
            print("to_state: ", self.to_state)
            print("output_symbol: ", self.output_symbol)
            print("shift_direction: ", self.shift_direction)

    def add_state(self, name):
        name = name.strip()
        if self.current_state is None:
            self.current_state = name      
        self.states.append(name)
        self.final_state = name

    def add_transition(self, from_state, input_symbol, to_state, output_symbol, shift_direction):
        if from_state in self.states and to_state in self.states:
            transition = self.Transition(from_state, input_symbol, to_state, output_symbol, shift_direction)
            self.transitions.append(transition)
        else:
            print("Estado presente na transição não existe")
            exit()

    def set_input_alphabet(self, input_alphabet):
        for symbol in input_alphabet:
            self.input_alphabet.append(symbol)
        self.input_alphabet.append(self.blank)

    def set_output_alphabet(self, output_alphabet):
        for symbol in output_alphabet:
            self.output_alphabet.append(symbol)

    def set_input_tape(self, tape):
        for symbol in tape:
            if symbol not in self.input_alphabet:
                print("O símbolo ", symbol, " não pertence ao alfabeto de input.")
                exit()
        self.tapes['input'] = tape
        self.tapes['input'].append(self.blank)

    def execute(self, transition: Transition):
        # Escreve o output no fita do input
        self.tapes['input'][self.heads['input']] = transition.output_symbol

        # Avança para o próximo estado
        self.current_state = transition.to_state

        # Avança a cabeça da fita
        if transition.shift_direction == 'R':
            self.heads['input'] += 1
        elif transition.shift_direction == 'L':
            self.heads['input'] -= 1

    def step(self):
        print(self.tapes['input'])

        if self.current_state == self.final_state and self.heads['input'] >= len(self.tapes['input']):
            return True

        current_symbol = self.tapes['input'][self.heads['input']]
        
        transition = self.get_transition(self.current_state, current_symbol)

        self.execute(transition)

        return False

    def run(self):
        completed = False
        while(not completed):
            completed = self.step()
         
    def get_transition(self, state, symbol):
        for transition in self.transitions:
            if transition.from_state == state and transition.input_symbol == symbol:
                return transition
        
        print("Nenhuma transição encontrada para o estado e símbolo atuais")
        exit()

        