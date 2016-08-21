#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stakan ( object ) :
    
    Position = [ u'Shkaf', u'table' ]
    
    def __init__ ( self ) :
        self.__Water = 0.0
        self.__Milk  = 0.0
        self.__Pos   = u'Shkaf'
    
    def add_water ( self, vol ) :
        if vol < 0 :
            raise ValueError
        self.__Water += vol
        
    
    def add_milk ( self, vol ) :
        if vol < 0 :
            raise ValueError
        self.__Milk += vol    
    
    def take ( self, vol ) :
        if vol < 0 :
            raise ValueError
        if vol > self.total () :
            raise Exception
        M = self.part_milk () * vol
        W = vol - M
        self.__Milk  -= M
        self.__Water -= W
        return ( vol, M / vol )
        
    def set_position ( self, pos ) :
        pass
    
    @property
    def total ( self ) :
        return self.__Water + self.__Milk
    
    @property
    def part_milk ( self ) :
        return self.__Milk / self.total ()
    
if __name__ == '__main__' :
    St = Stakan ()
    St.add_water ( 5.0 )
    St.add_milk  ( 1.0 )
    print St.total
    print St.part_milk