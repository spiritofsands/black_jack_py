def get_answer(accepted_answers=['y', 'n']):
    loop_count = 0
    max_loops = 10

    accepted_answers = [str(answer) for answer in accepted_answers]
    while True:
        loop_count += 1
        if loop_count > max_loops:
            raise RuntimeError('Too much wrong answers')

        if len(accepted_answers) > 3:
            prompt = f'{accepted_answers[0]}/../{accepted_answers[-1]}' + ': '
        else:
            prompt = '/'.join(accepted_answers) + ': '
        answer = input(prompt)
        if answer in accepted_answers:
            print()
            return answer

def print_header(str):
    print('\n_______________________________')
    print(f'{str}\n')
