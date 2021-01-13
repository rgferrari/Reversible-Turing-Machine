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

            # Essas quádruplas só são necessárias para emularmos de forma verossímil a máquina reversível
            self.set_rw_quadruple()
            self.set_shift_quadruple()

        def __str__(self):
            return "(" + self.from_state + "," + self.input_symbol + ")=(" + self.to_state + "," + self.output_symbol + "," + self.shift_direction + ")"

        def set_rw_quadruple(self):
            self.rw_quadruple = {
                'from_state': self.from_state, 
                'input_symbol': self.input_symbol,
                'output_symbol': self.output_symbol,
                'temporary_state': self.from_state + "_"
            }
        
        def set_shift_quadruple(self):
            self.shift_quadruple = {
                'temporary_state': self.from_state + "_",
                'blank_space': '/',
                'shift_direction': self.shift_direction,
                'to_state': self.to_state
            }

    def get_transition(self, state, symbol):
        index = 0
        for transition in self.transitions:
            if transition.from_state == state and transition.input_symbol == symbol:
                return transition, index
            index += 1

        exit("Nenhuma transição encontrada para o estado e símbolo atuais")        

    def add_state(self, name):
        name = name.strip()
        if self.current_state is None:
            self.start_state = name
            self.current_state = name      
        self.states.append(name)
        self.final_state = name

    def add_transition(self, from_state, input_symbol, to_state, output_symbol, shift_direction):
        if from_state in self.states:
            if to_state in self.states:
                transition = self.Transition(from_state, input_symbol, to_state, output_symbol, shift_direction)
                self.transitions.append(transition)
            else:
                exit("O estado ", to_state, " não existe")
        else:
            exit("O estado ", from_state, " não existe")

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
                exit("O símbolo ", symbol, " não pertence ao alfabeto de input.")
        self.tapes['input'] = tape
        self.tapes['input'].append(self.blank)


    def execute(self, transition: Transition, backward=False):
        if backward:
            # Avança a cabeça da fita
            if transition.shift_quadruple['shift_direction'] == 'L':
                self.heads['input'] += 1
            elif transition.shift_quadruple['shift_direction'] == 'R':
                self.heads['input'] -= 1

            self.tapes['input'][self.heads['input']] = transition.rw_quadruple['input_symbol']

            self.current_state = transition.rw_quadruple['from_state']
        else:
            # Escreve o output no fita do input
            self.tapes['input'][self.heads['input']] = transition.rw_quadruple['output_symbol']

            # Avança para o próximo estado
            self.current_state = transition.shift_quadruple['to_state']

            # Avança a cabeça da fita
            if transition.shift_quadruple['shift_direction'] == 'R':
                self.heads['input'] += 1
            elif transition.shift_quadruple['shift_direction'] == 'L':
                self.heads['input'] -= 1


    def retraced_computation(self):
        while True:
            if self.current_state == self.start_state and self.heads['input'] == 0:
                return

            transition_index = self.tapes['history'][self.heads['history']]

            self.execute(self.transitions[transition_index], backward=True)

            # Avança para o próximo estado
            self.heads['history'] -= 1

    def forward_computation(self):
        while True:
            if self.current_state == self.final_state and self.heads['input'] >= len(self.tapes['input']):
                # Atualiza a cabeça da fita history para o final da fita
                self.heads['history'] = len(self.tapes['history']) - 1
                return

            current_symbol = self.tapes['input'][self.heads['input']]
            
            transition, index = self.get_transition(self.current_state, current_symbol)

            # Salva a transição
            self.tapes['history'].append(index)

            self.execute(transition)

    def copy_output(self):
        # Salva o output na fita output
        self.tapes['output'] = self.tapes['input'].copy()

    def run(self):
        # Fase 1
        self.forward_computation()

        # Fase 2
        self.copy_output()

        # Fase 3
        self.retraced_computation()

        print('Input: ', self.tapes['input'])
        print('History: ', self.tapes['history'])
        print('Output: ', self.tapes['output'])