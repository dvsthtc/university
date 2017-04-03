import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    if line.find('@') != -1:
        org = line[line.index('@')+1:len(line)+1]
    print str(org)

    cur.execute('SELECT count FROM Counts WHERE email = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES ( ?, 1 )''', ( org, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?',
            ( org, ))
    
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10 '

print '__________________________'
print "Counts:"
for row in cur.execute(sqlstr) :
    print row[0][:-1],'-',str(row[-1])
cur.close()
