import mysql.connector


def main():
    cnx = mysql.connector.connect(user='root', host='127.0.0.1', database='employees')
    with open('E.txt', 'w') as f:
        sql = 'select E.emp_no, E.first_name, E.last_name, S.salary, S.from_date, S.to_date  from employees E, salaries S where E.emp_no = S.emp_no;'
        cursor = cnx.cursor()
        cursor.execute(sql)
        f.write('emp_no(integer) first_name(string) last_name(string) salary(integer) from_date(string) to_date(string)\n')
        for (emp_no, first_name, last_name, salary, from_date, to_date) in cursor:
            f.write('{} {} {} {} {} {}\n'.format(emp_no, first_name, last_name, salary, from_date, to_date))

    cnx.close()


if __name__ == '__main__':
    main()
