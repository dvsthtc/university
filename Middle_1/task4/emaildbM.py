import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, month TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From ') : continue
    org = line.split()
    email = org[1]
    month = org[3]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, month, count )
                VALUES ( ?, ?, 1 )''', ( email, month, ) )
    else :
        cur.execute('UPDATE Counts SET count = count+1 WHERE email = ?',
            ( email, ))
        cur.execute('UPDATE Counts SET month=? WHERE email = ?',
            ( month, email, ))
        

    
    conn.commit()

sqlstr = 'SELECT email, count, month FROM Counts ORDER BY count,month DESC LIMIT 10 '

print '__________________________'

for row in cur.execute(sqlstr) :
    print row[0],row[1],row[-1]
cur.close()
