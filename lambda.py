
#test
#fn = lambda x: x +1
#print( fn(2) )


#my_list = [1, 5, 4, 6, 8, 11, 3, 12]
my_list = {
    7 : 'sam',
    8: 'john',
    9: 'mathew',
    10: 'riti',
    11 : 'aadi',
    12 : 'sachin'
}

def isValid( id, name ):
    return id > 9 and len(name) >= 5

collection = filter(lambda it: isValid( it[0], it[1] ), my_list.items())


#print(help(collection))
#print( list(collection) )
foo = dict(collection);
print( foo )
print( foo )
for i in foo.items():
    print(i[0],i[1])

