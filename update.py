import sqlite3


def update_basic(old_id, new_id):
    main_db = sqlite3.connect('drivers.db')
    print("Database connected")
    cursor = main_db.cursor()
    sql_query = "update Staff_BasicData set StaffID = ? where StaffID = ?"
    try:
        cursor.execute(sql_query, (new_id, old_id))
    except sqlite3.Error as error:
        print("Error", str(error))
    else:
        main_db.commit()
        print("Successfully added basic data")
    finally:
        main_db.close()
        print("Database closed")


def update_driver(old_id, new_id):
    main_db = sqlite3.connect('drivers.db')
    print("Database connected")
    cursor = main_db.cursor()
    sql_query = "update Staff_DriverData set StaffID = ? where StaffID = ?"
    try:
        cursor.execute(sql_query, (new_id, old_id))
    except sqlite3.Error as error:
        print("Error", str(error))
    else:
        main_db.commit()
        print("Successfully added basic data")
    finally:
        main_db.close()
        print("Database closed")


def update_game(old_id, new_id):
    main_db = sqlite3.connect('drivers.db')
    print("Database connected")
    cursor = main_db.cursor()
    sql_query = "update Staff_GameData set StaffID = ? where StaffID = ?"
    try:
        cursor.execute(sql_query, (new_id, old_id))
    except sqlite3.Error as error:
        print("Error", str(error))
    else:
        main_db.commit()
        print("Successfully added basic data")
    finally:
        main_db.close()
        print("Database closed")


def update_performance(old_id, new_id):
    main_db = sqlite3.connect('drivers.db')
    print("Database connected")
    cursor = main_db.cursor()
    sql_query = "update Staff_PerformanceStats set StaffID = ? where StaffID = ?"
    try:
        cursor.execute(sql_query, (new_id, old_id))
    except sqlite3.Error as error:
        print("Error", str(error))
    else:
        main_db.commit()
        print("Successfully added basic data")
    finally:
        main_db.close()
        print("Database closed")


def update_state(old_id, new_id):
    main_db = sqlite3.connect('drivers.db')
    print("Database connected")
    cursor = main_db.cursor()
    sql_query = "update Staff_State set StaffID = ? where StaffID = ?"
    try:
        cursor.execute(sql_query, (new_id, old_id))
    except sqlite3.Error as error:
        print("Error", str(error))
    else:
        main_db.commit()
        print("Successfully added basic data")
    finally:
        main_db.close()
        print("Database closed")


def update_contracts(old_id, new_id):
    main_db = sqlite3.connect('drivers.db')
    print("Database connected")
    cursor = main_db.cursor()
    sql_query = "update contracts set id = ? where id = ?"
    try:
        cursor.execute(sql_query, (new_id, old_id))
    except sqlite3.Error as error:
        print("Error", str(error))
    else:
        main_db.commit()
        print("Successfully added basic data")
    finally:
        main_db.close()
        print("Database closed")


def main():
    # Getting data from drivers db
    drivers_db = sqlite3.connect('drivers.db')

    # Staff_BasicData retrieval
    cursor = drivers_db.cursor()
    sql_query = "SELECT * FROM ids ORDER BY oldId DESC;"
    cursor.execute(sql_query)
    all_basic_rows = cursor.fetchall()
    for row in all_basic_rows:
        old_id = row[0]
        new_id = row[1]

        update_contracts(old_id, new_id)



if __name__ == '__main__':
    main()
