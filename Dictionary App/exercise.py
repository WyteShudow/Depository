import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

query = cursor.execute("SELECT * FROM Dictionary ")
results = cursor.fetchall()
con.close()
data = dict(results)

def diction(w):
    if w.lower() in data:
        return data[w.lower()]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        lex = input("Did you mean %s? Y/N: " % get_close_matches(w, data.keys())[0])
        if lex.upper() == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif lex.upper() == 'N':
            return "The word %s doe not exist" % w
        else:
            return "I don't understand!!"
    else:
        return "The word %s doe not exist" % w


word = input("Enter a word: ")
output = diction(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)