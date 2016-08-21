#!/usr/bin/python
# -*- coding: utf-8 -*-

import mDocument
import mNakPos

def create () :
    return Nakladnaya ( status = mDocument.Document.New )

class Nakladnaya ( mDocument.Document ) :
    
    def __init__ ( self, **kwargs ) :
        mDocument.Document.__init__ ( self, **kwargs )
        self.__Positions = []
        
    itogo = property ( lambda self : self.__Itogo )
    
    @property
    def _itogo ( self ) :
        try :
            return self.itogo
        except AttributeError :
            return None
    
    def __len__ ( self ) :
        return len ( self.__Positions )
    
    def get_position ( self, index ) :
        return self.__Positions [index]
    
    def __getitem__ ( self, index ) :
        return self.__Positionsp[index]
    
    def __iter__ ( self ) :
        for P in self.__Positions :
            yield P
    
    def append_blank ( self ) :
        #TODO: функция должна принимать параметры соответствующие
        #TODO: параметам консттруктора класса NakPos
        #TODO: и добавлять в наколадную позицию
        self.__Positions.append ( mNakPos.NakPosition() )
    
    def append ( self, position ) :
        if not isinstance ( position, mNakPos.NakPosition ) :
            raise ValueError
        self.__Positions.append ( position )
        
    def delete ( self, index ) :
        del self.__Positions [index]
    
    def __unicode__ ( self ) :
        
        Posit = u''
        K = 1
        for P in self :
            Posit += u'%d. %s\n' % ( K, unicode (P) )
            K     += 1
        
        result  = u'(Id:%d) (Status:%d)' % ( self._id, self._status )
        result += u'Накладная\n'
        result += u'%s' % ( Posit, )
        result += u'Итого %s' % ( self._itogo, )
        
        return result
        
  #      result  = u'''
   #         (Id:%d) (Status:%d)( self._id, self._status )
    #       %s
     #       Итого: %s
      #      ''' % \
       #     ( self._id, self._status, Posit, unicode( self._itogo) )
    
        
if __name__ == '__main__' :
        Nakl = create ()