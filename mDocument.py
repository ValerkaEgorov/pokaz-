#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqllite3
import os.path

def create (  ) :
    '''Create new Document'''
    return Document ( status = Document.New )
    
def load ( Id ) :
    '''Load document from database'''
    Doc = Document ( id = Id )
    Doc.restore ()
    return Doc

class Document ( object ) :

    New = 1
    Status_Allowed = [ New ]

    def __init__ ( self, **kwargs ) :
    # TODO: запоминать значения остальных параметров
    # TODO: но никак их не обрабатывать.
        if u'id' in kwargs :
            self.__Id = int ( kwargs['id'] )
        if u'status' in kwargs :
            if kwargs['status'] not in Document.Status_Allowed :
                raise ValueError 
            self.__Status = status
    
    id = property ( lambda self : self.__Id )
    
    @property
    def _id ( self ) :
        try :
            return self.id
        except AttributeError :
            return None
    
    @property
    def status ( self ) :
        return self.__Status
    
    @property
    def _status ( self ) :
        try :
            return self.status
        except AttributeError :
            return None
    
    def save ( self ) :
        with bd
        
        
    def restore ( self ) :
        pass
    
    @classmethod
    def create_table ( self ) :
        conn = sqllite3.connect ( os.path.expanduser( u"~/data.db") )
        curr = conn.cursor()
        curr.execute
        curr.commit()
        conn.close()
    
if __name__ == '__main__' :
    D = create ()
    print u'Status = ', D.status
    try :
        print u'Id = ',     D.id
    except AttributeError :
        print u'None'
        
    D = load ( id = 1 )
    try : 
        print u'Status =', D.status
    except AttributeError
    try :
        print u'Id = ',     D.id
    except AttributeError :
        print u'None'
    