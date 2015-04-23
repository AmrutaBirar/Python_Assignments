import dbm.dumb

def run(dbname):
    mykeys =  b'name',b'age',b'gender'
    myValues = b'Joe',b'39',b'male'
    
    dumbDb = dbm.dumb.open(dbname, 'c')
    dumbDb[b'name'] = b'Joe'
    dumbDb[b'gender'] = b'male'
    dumbDb[b'age'] = b'39'
    
        
    print("Amruta Birar")
