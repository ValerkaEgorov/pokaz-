#!/usr/bin/python
# -*- coding: utf-8 -*-

def func1 ( A ) :
    print u'func1( ', A, u' )'
    return 2 * A
    
S = func1

S ( 3 ) 

print u'func1:', func1

func1 = 5
print u'func1:', func1

def func2 ( A, function ) :
    print u'func2'
    return function ( A )
    
func2 ( 120, S )

def func3 ( B ) :
    def func4 ( C ) :
        print u'func4'
    def func5 ( C ) :
        print u'func5'
    if B % 2 == 0 :
        return func4
    else :
        return func5    
        
D = func3 ( 1 )
E = func3 ( 2 )

D(1)
E(1)