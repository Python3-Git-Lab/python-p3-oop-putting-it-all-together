#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title= title
        self.page_count = page_count
    
    #page getter
    def get_page(self):
        return self._page_count
    
    #page setter
    def set_page(self, page_count):
        if type(page_count)!=int:
            print("page_count must be an integer")
        else:
            self._page_count = page_count
        
    #page property
    page_count = property(get_page,set_page)
    
    #turn page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
     
    
#test code
book = Book("And Then There Were None", 272)
book.turn_page

        