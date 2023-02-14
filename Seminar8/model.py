import os

journal = {}
subject = ''
path = ''
subject_list = []
student = ''


def set_class(class_path: str):
    global path
    path = 'Classes/' + class_path + '.txt'


def checking_path():
    isfile = os.path.isfile(path)
    return isfile


def set_subject(our_subject: str):
    global subject
    subject = our_subject


def get_subject_list():
    global subject_list
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        var = sub.split(';')[0]
        subject_list.append(var)
    return subject_list


def checking_subject():
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == subject:
            return True


def open_file():
    global subject
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] == subject:
            for study in sub.split(';')[1].strip().split(', '):
                journal[study.split(':')[0]] = list(map(int, study.split(':')[1].split()))


def checking_student():
    for key in journal:
        if key == student:
            return True


def set_student(our_student: str):
    global student
    student = our_student


def save_file():
    new_file = []
    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readlines()
    for sub in file:
        if sub.split(';')[0] != subject:
            new_file.append(sub.strip())
    item = []
    for student, marks in journal.items():
        item.append(student + ':' + ' '.join(list(map(str, marks))))
    item = subject + ';' + ', '.join(item)
    new_file.append(item)
    with open(path, 'w', encoding='UTF-8') as data:
        data.write('\n'.join(new_file))


def student_mark(student: str, mark: int):
    marks = journal.get(student)
    marks.append(mark)
    journal[student] = marks


def get_journal():
    return journal


def get_subject():
    return subject