import view
import model


def start():
    model.set_class(view.input_class())
    if model.checking_path():
        view.not_class()
        exit()
    subject_list = model.get_subject_list()
    view.list_of_subject(subject_list)
    model.set_subject(view.input_subject())
    if not model.checking_subject():
        view.not_subject()
        exit()
    model.open_file()
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'выход':
            break
        for key in journal:
            if key == student:
                mark = int(view.what_mark())
                if 0 < mark < 6:
                    model.student_mark(student, mark)
                    break
                else:
                    view.not_mark()
                    break
        else:
            view.not_student()

        model.save_file()
