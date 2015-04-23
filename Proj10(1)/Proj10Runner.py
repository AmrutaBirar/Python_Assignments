import dbm.dumb

def run(mykey,myvalue,db):
    #Open database in read write mode
    dumbDb = dbm.dumb.open('database','c')

    #keys and values will be imported from other file

    #populate the database
    for cnt in range(len(mykey)):
        dumbDb[mykey[cnt]] = myvalue[cnt]

    #print the values
    print('Amruta Birar')
    keys = dumbDb.keys()
 
    for cnt in range(len(mykey)):
        print("key:",keys[cnt],"value:",dumbDb.get(keys[cnt]))

    
