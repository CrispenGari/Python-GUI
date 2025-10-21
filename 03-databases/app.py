import sqlite3


conn = sqlite3.connect("employees.db")

cur = conn.cursor()

cur.execute('DROP DATABASE employees;')

# ========== Q1

# DROP TABLE `EMPLOYEES`;
def q1():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS `employees`(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            EmployeeNumber INTEGER UNIQUE NOT NULL,
            Name TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Gender TEXT NOT NULL
        )
    """)
    conn.commit()


def q2():
    cur.executemany(
        """
    INSERT INTO `employees` (EmployeeNumber, Name, Age, Gender)
    VALUES (?, ?, ?, ?);
    """,
        [
            [224145, "Andiswa", 22, "Female"],
            [220022, "Fiona", 28, "Female"],
            [201122, "Rodney", 29, "Male"],
            [214120, "Sipho", 24, "Female"],
            [230005, "Ivana", 30, "Female"],
        ],
    )
    conn.commit()


def q3():
    res = cur.execute("""SELECT * FROM `employees` WHERE Age >= 20;""").fetchall()
    print("ID \tEmp # \tName \tAge \tGender")
    for id, emId, name, age, gender in res:
        print(f"{id} \t{emId} \t{name} \t{age} \t{gender}")


def q4():
    cur.execute(
        """
    UPDATE `employees` SET Gender = ? 
    WHERE Name = ?;
""",
        ["Male", "Sipho"],
    )
    conn.commit()


def q5():
    cur.execute(
        """
    DELETE FROM `employees` WHERE Gender = ?;
""",
        ["Male"],
    )
    conn.commit()


if __name__ == "__main__":
    # q1();
    # q2()
    q3()
    print("=" * 50)
    q4()
    q3()
    print("=" * 50)
    q5()
    q3()
    pass

conn.close()
