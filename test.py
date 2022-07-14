"""# RETURN UID's
def get_teachers(): 
    if cursor.execute('SELECT * FROM teachers').fetchone() is None: 
        teachers2 = 'Список учителей пуст!'
    else:
        cursor.execute("SELECT uid, name FROM teachers")
        teachers1 = cursor.fetchall()
        teachers2 = 'Список учителей:\n'
        for i in range(len(teachers1)):
            teachers2+=(str(teachers1[i][1])) + ' '
            teachers2+=(str(teachers1[i][0])) + '\n'
    return(teachers2)

# RETURN UID's
def get_teachers():
    cursor.execute("SELECT uid FROM teachers")
    teachers1 = cursor.fetchall()
    teachers2 = []
    for i in range(len(teachers1)):
        teachers2.append(teachers1[i][0])
    return(teachers2)"""