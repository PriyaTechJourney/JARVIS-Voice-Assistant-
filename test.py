# Global Declaration
import sqlite3


connection = sqlite3.connect('assistant.sqlite')
cursor = connection.cursor()

# find contacts
def findContact(query):
    from engine.helper import remove_words as rw
    words_to_remove = ['make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = rw(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobileno, email FROM phonebook WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][1])
        mobile_number_str = str(results[0][0])
        email = str(results[0][1])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        return 0, 0

findContact("papa")