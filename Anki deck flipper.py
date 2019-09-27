import sqlite3

deck = sqlite3.connect("G:/Users/Jozhus/Desktop/Files/Downloads/collection.anki2")
fetched = deck.execute('select id, flds, sfld from notes;')
cards = fetched.fetchall()
c = deck.cursor()

for i, card in enumerate(cards):
    cardid = card[0]
    flds = card[1].split('\x1f')
    sfld = card[2]
    
    sfld = flds[3]
    temp = flds[0]
    flds[0] = flds[3]
    flds[3] = temp
    
    flds = '\x1f'.join(flds)

    c.execute("""update notes set flds = ?, sfld = ? where id = ?""", (flds, sfld, cardid))
    print(i)

deck.commit()
deck.close()
input('Done!')
