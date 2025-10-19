
class SQL:
    CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS `students` (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL
        );
    """

    REGISTER_STUDENT = """
        INSERT INTO `students` (firstName, lastName) VALUES (?, ?);
    """

    ALL_STUDENTS = """
        SELECT * FROM `students`;
    """
