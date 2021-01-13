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
            'input': 0,
            'history': 0
        }
        self.current_state = None
        self.start_state = None
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
            self.start_state = name
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

    # Executa a transição ao contrário
    def execute_backward(self, transition: Transition):
        # Avança a cabeça da fita
        if transition.shift_direction == 'L':
            self.heads['input'] += 1
        elif transition.shift_direction == 'R':
            self.heads['input'] -= 1

        self.tapes['input'][self.heads['input']] = transition.input_symbol

        self.current_state = transition.from_state


    def retraced_computation(self):
        if self.current_state == self.start_state and self.heads['input'] == 0:
            return True

        transition_index = self.tapes['history'][self.heads['history']]

        self.execute_backward(self.transitions[transition_index])

        # Avança para o próximo estado
        self.heads['history'] -= 1

        return False
        

    def execute_forward(self, transition: Transition):
        # Escreve o output no fita do input
        self.tapes['input'][self.heads['input']] = transition.output_symbol

        # Avança para o próximo estado
        self.current_state = transition.to_state

        # Avança a cabeça da fita
        if transition.shift_direction == 'R':
            self.heads['input'] += 1
        elif transition.shift_direction == 'L':
            self.heads['input'] -= 1

    def forward_computation(self):
        if self.current_state == self.final_state and self.heads['input'] >= len(self.tapes['input']):
            # Atualiza a cabeça da fita history para o final da fita
            self.heads['history'] = len(self.tapes['history']) - 1
            return True

        current_symbol = self.tapes['input'][self.heads['input']]
        
        transition, index = self.get_transition(self.current_state, current_symbol)

        # Salva a transição
        self.tapes['history'].append(index)

        self.execute_forward(transition)

        return False

    def copy_output(self):
        # Salva o output na fita output
        self.tapes['output'] = self.tapes['input'].copy()

    def run(self):
        # Fase 1
        completed = False
        while(not completed):
            completed = self.forward_computation()

        # Fase 2
        self.copy_output()

        # Fase 3
        completed = False
        while(not completed):
            completed = self.retraced_computation()

        print('Input: ', self.tapes['input'])
        print('History: ', self.tapes['history'])
        print('Output: ', self.tapes['output'])
         
    def get_transition(self, state, symbol):
        index = 0
        for transition in self.transitions:
            if transition.from_state == state and transition.input_symbol == symbol:
                return transition, index
            index += 1
        
        print("Nenhuma transição encontrada para o estado e símbolo atuais")
        exit()