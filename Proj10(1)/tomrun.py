import dbm.dumb
def run(key,value,name):
    dumbDb = dbm.dumb.open('database', 'c')
    for cnt in range(len(key)):
        dumbDb[key[cnt]] = value[cnt]
    print('name')
    for key in dumbDb.keys():
        print('key: ', key, 'value:', dumbDb[key])
    dumbDb.close()
