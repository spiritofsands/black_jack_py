def get_answer(accepted_answers=['y', 'n']):
    accepted_answers = [str(answer) for answer in accepted_answers]
    while True:
        if len(accepted_answers) > 3:
            prompt = f'{accepted_answers[0]}/../{accepted_answers[-1]}' + ': '
        else:
            prompt = '/'.join(accepted_answers) + ': '
        answer = input(prompt)
        if answer in accepted_answers:
            return answer
