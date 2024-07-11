with open('hr_system.txt') as file:
    for line in file:
        line = line.strip()
        splitted = line.split()
        name = splitted[0]
        id_number = splitted[1]
        job_title = splitted[2]
        salary = float(splitted[3]) / 24
        if job_title == 'Engineer':
            salary += 1000
        print(f'{name} (ID: {id_number}), {job_title} - ${salary:.2f}')