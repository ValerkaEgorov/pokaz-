#!/usr/bin/python
# -*- coding: utf-8 -*-

class NakPosition ( object ) :

    def __init__ ( self ) :
        pass
    
    id
    
    
    def get_title ( self ) :
        return self.__Title
        
    def set_title ( self, title ) :
        self.__Title = unicode ( title )
        
    def del_title ( self ) :
        del self.__Title

    title = property ( get_title, set_title, del_title )
    
    @property
    def _title ( self ) :
        try: 
            return self.title
        except AttributeError :
            return None
    
    @property
    def unit ( self ) :
        return self.__Unit
    
    @unit.setter
    def unit ( self, unit ) :
        self.__Unit = unicode ( unit )
    
    @unit.deleter
    def unit ( self ) :
        del self.__Unit
    
    @property
    def _unit ( self ) :
        try: 
            return self.unit
        except AttributeError :
            return None
    
    
    @property
    def price ( self ) :
        return self.__Price
        
    @price.setter
    def price ( self, price ) :
        self.__Price = int ( price )
        
    @price.deleter
    def price ( self ) :
        del self.__Price
    
    @property
    def _price ( self ) :
        try: 
            return self.price
        except AttributeError :
            return None
    
    
    @property
    def amount ( self ) :
        return self.__Amount
        
    @amount.setter
    def amount ( self, amount ) :
        self.__Amount = long ( amount )
        
    @amount.deleter
    def amount ( self ) :
        del self.__Amount
        
    @property
    def _amount ( self ) :
        try: 
            return self.amount
        except AttributeError :
            return None
        
        
        
    @property
    def summa ( self ) :
        try :
            return self.__Summa
        except AttributeError :
            return self.amount * self.price
            
    @summa.setter
    def summa ( self, summa ) :
        self.__Summa = long ( summa )
        
    @summa.deleter
    def summa ( self ) :
        del self.__Summa
        
    @property
    def _summa ( self ) :
        try: 
            return self.summa
        except AttributeError :
            return None
        
        
    def __unicode__ ( self ) :
        return u'%s, %s, %s, %s, %s, %s' % (
                self._id,
                self._title,
                self._unit,
                self._price,
                self._amount,
                self._summa,
                )
    
        
        
        
        
        
    