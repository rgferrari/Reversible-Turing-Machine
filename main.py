from rtm import Rtm

machine = Rtm()

n_states, input_alphabet_size, output_alphabet_size, n_trasitions = [int(i.strip()) for i in input().strip().split(' ')]

states = input().strip().split(' ')
for state in states:
    machine.add_state(state)

input_alphabet = input().strip().split(' ')
machine.set_input_alphabet(input_alphabet)

output_alphabet = input().strip().split(' ')
machine.set_output_alphabet(output_alphabet)

for i in range(0, n_trasitions):
    _in, _out = input().strip().split('=')

    _in = _in.strip('()').split(',')
    _out = _out.strip('()').split(',')

    machine.add_transition(_in[0], _in[1], _out[0], _out[1], _out[2])

input_tape = list(input().strip())
machine.set_input_tape(input_tape)

machine.run()

# print(machine.input_alphabet)
# print(machine.output_alphabet)
# print(machine.states)
# print(machine.current_state)
# print(machine.final_state)
# print("Transitions:")
# for transition in machine.transitions:
#     print(transition)
# print(machine.tapes['input'])



    