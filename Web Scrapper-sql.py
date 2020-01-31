#!/usr/bin/env python
# coding: utf-8

# In[170]:


# webscrapping amazon.in from book name entered

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import urllib.error


# In[171]:


## converting book name into url

book_name = input("please enter the name of the book or ISBN no.  ")
book_name = book_name.replace(' ' ,'+')
if book_name[3] == '-':
    book_name = book_name[:3]+book_name[4:]
url = "https://www.amazon.in/s?k="


# In[172]:


## isolating webpage

try:                                                                                            
    my_url = url + book_name
    uClient = uReq(my_url)
    page = uClient.read()
    uClient.close()
except urllib.error.URLError as e:
    print(e)


# In[173]:


## creating soup objet for image, title

try:
    page_soup = soup(page,"html.parser")
    containers = page_soup.findAll("h2",{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
    
    img_containers = page_soup.findAll("div",{"class":"a-section aok-relative s-image-fixed-height"})
    print("Best Matching Result is \n")
    img_containers = page_soup.findAll("div",{"class":"a-section aok-relative s-image-fixed-height"})
    image_src = img_containers[0].img['src']
    print("\n")
    print(image_src)
    
    title = containers[0].a.span.text 
    print(title)
    
    link = "https://www.amazon.in"
    link += containers[0].a.get('href')
except urllib.error.URLError as e:
    print(e)
    print("PLEASE TRY AFTER SOMETIME.")
except:
    print("Some thing Went Wrong PLease try after Some time")


# In[174]:


## opening link for scrapping further details

try:
    uClient = uReq(link)
    page_book = uClient.read()
    uClient.close()
except urllib.error.URLError as e:
    print(e)
except urllib.error.HTTPError as e:
    print(e)
except:
    print("HTTP error please try after some time")


# In[175]:


## genre list
listofgenre = ['Action and adventure', 'Art', 'Alternate history', 'Anthology', 'Autobiography', 'Biography', 'Book review', 'Chick lit', 'Children', 'Cookbook', 'Comic book', 'Coming of age', 'Crime', 'Diary', 'Dictionary', 'Drama', 'Encyclopedia', 'Fairytale', 'Fantasy', 'Guide', 'Graphic novel', 'Health', 'Historical fiction', 'History', 'Horror', 'Journal', 'Math', 'Memoir', 'Mystery', 'New age', 'Paranormal romance', 'Poetry', 'Political thriller', 'Picture book', 'Prayer', 'Religion', 'Romance', 'Review', 'Spirituality', 'Science', 'Self help', 'Satire', 'Science fiction', 'Short story', 'Suspense', 'Textbook', 'Travel', 'True crime', 'Thriller', 'Young adult']

index = -1


# In[176]:


##gathering Author, ALL details

try:
    page_soup = soup(page_book,"lxml")
    About_Book = page_soup.findAll("div",{"class":"content"})
    By_line = page_soup.find(id="bylineInfo")

    if By_line.span.a.text:
        if "Visit" not in By_line.span.a.text:
            By_line = By_line.span.a.text
        else:
            By_line = By_line.span.span.text
    else:
        By_line = By_line.span.span.text
        
    
    By_line = By_line.strip()
    By_line = By_line.replace('(Author)','').strip()
    print(By_line.strip())
    
    
                                                                                                         
except urllib.error.URLError as e:
    print(e)
except urllib.error.HTTPError as e:
    print(e)
except: 
     print("Some thing Went Wrong Please type checking the name of the book again")


# In[177]:


try:
    genre = About_Book[0].ul.findAll('li', {"class":"zg_hrsr_item"})
    genre_1 = genre[-1].a.text
    if '(Books)' in genre_1:
        genre_1 = genre_1.strip("(Books)")

    for i in range(len(listofgenre)):
        if listofgenre[i] in genre_1:
            index = i
            break
    if index != -1:
        genre_1 = listofgenre[index]

    print(genre_1)


    #for genre_1 in genre:
     #  if '(Books)' in genre_1:
      #      print(genre_1.replace('&',',').strip("(Books)"), sep = ',')
       # else:
        #    print(genre_1.replace('&',','), sep = ',')
except urllib.error.URLError as e:
    print(e)
except urllib.error.HTTPError as e:
    print(e)
except: 
     print("Some thing Went Wrong Please type checking the name of the book again")


# In[178]:


try:
    #ISBN10
    #ISBN13
    
    for each in About_Book[0].ul.findAll('li'):
        b = each.b.text
        AboutBook = each.text
        if('pages' in AboutBook):
            print(AboutBook.strip(b).strip())
            Pages = AboutBook.strip(b).strip()
        elif('Publisher' in AboutBook):
            print(AboutBook.strip(b).strip())
            Publisher = AboutBook.strip(b).strip()
        elif('Language:' in AboutBook):
            print(AboutBook.strip(b).strip())
            Language = AboutBook.strip(b).strip()
        elif('ISBN-10' in AboutBook):
            print(AboutBook.strip(b).strip())
            ISBN10 = AboutBook.strip(b).strip()
        elif('ISBN-13' in AboutBook):
            ISBN13 = AboutBook.strip(b).strip()
            ISBN13 = ISBN13.replace('-', '')
            print(AboutBook.strip(b).strip())
            
    
       
        #print(AboutBook.strip(b))
        
except urllib.error.URLError as e:
    print(e)
except urllib.error.HTTPError as e:
    print(e)
except AttributeError:
    None
#     print("Some thing Went Wrong Please type checking the name of the book again")


# In[179]:


## incrementing data scrapped into mysql database

respond = input('Is this is the same book you are searching for??\n # Press Enter for adding it to Database')
if respond == "":
    #print('Press enter if you want to enter rack no. and copies...')
    #reply = input()
    
    
    import mysql.connector

    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'surya2001',
        database = 'suryadb')

    obj = conn.cursor()
    f_insert = 'insert into booklist(title,pic,genre,author,publisher,language,pages,isbn10,isbn13) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    try:
        #ISBN10 = int(ISBN10)
        #ISBN13 = int(ISBN13)
        print(image_src)
        print(title)
        print(By_line)
        print(genre_1)
        print(Pages)
        print(Publisher)
        print(Language)
        print(ISBN10)
        print(ISBN13)
        '''
        value1 = (title, title)
        value2 = (pic, image_src)
        value3 = (genre, genre_1)
        value4 = (author, By_line)
        value5 = (publisher, Publisher)
        value6 = (language, Language)
        value7 = (pages, Pages)
        value8 = (isbn10, ISBN10)
        value9 = (isbn13, ISBN13)
        '''


        obj.execute(f_insert,(title, image_src, genre_1, By_line, Publisher, Language, Pages, ISBN10, ISBN13))

        conn.commit()

        obj.close()
        conn.close()
        
        print('\nThanks for using our service...')
    except mysql.connector.IntegrityError:
        print('The book is already present in database, Enter name of another book')
        
else:
    print('\nThanks for using our service...')

