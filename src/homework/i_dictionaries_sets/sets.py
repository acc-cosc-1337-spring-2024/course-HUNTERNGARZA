def get_students_who_took_prog1_and_prog2(prog1, prog2):
    return {i for i in prog1 if i in prog2}


def get_students_who_took_prog2_only(prog1, prog2):
    return prog2


def get_students_who_took_prog1_not_prog_2(prog1, prog2):
    return {i for i in prog1 if i not in prog2}


def get_students_who_took_prog2_not_prog_1(prog1, prog2):
    return {i for i in prog2 if i not in prog1}
