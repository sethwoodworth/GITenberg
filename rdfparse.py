# GutenPy - rdfparse.py
# Copyright (C) 2006 Lee Bigelow <ligelowbee@yahoo.com> 
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import bz2, os, os.path, re, string, cPickle
import sys, tempfile, urllib, xml.sax, xml.sax.handler
from platform import system

class Ebook:
    def __init__(self, bookid, title, author, subj, loc, lang=None, filename=None, mdate=None):
        self.bookid = bookid
        self.title = title
        self.author = author
	self.subj = subj
	self.loc = loc
        self.lang = lang
	self.filename = filename
	self.mdate = mdate
                
class Gutenberg:
    def __init__(self, pickle_path,
            catalog_url="http://www.gutenberg.org/feeds/catalog.rdf.bz2"):
        self.pickle_path = pickle_path
        self.catalog_url = catalog_url

    def updatecatalogue(self):
        #try: remotefh = urllib.urlopen(self.catalog_url)
        #except: return False
	try: localfh = open('./catalog.rdf.bz2', 'r')
	except: return False
	#print 'opened'
        decompressor = bz2.BZ2Decompressor()
        book_dict = {}
        handler = CatalogueDocumentHandler(sys.stdout, book_dict)
        parser = xml.sax.make_parser(['xml.sax.expatreader'])
        parser.setContentHandler(handler)
        chunksize = 1024 * 2
        offset = chunksize
	#print 'prepped, attempting read'
        data = localfh.read(chunksize)
	#print data
        while data != '':
            out = decompressor.decompress(data)
            if out != '':
                parser.feed(out)
            data = localfh.read(chunksize)
        parser.close()
	#print 'closed'
        for book in book_dict.values():
            if book.filename == None:
                del book_dict[book.bookid]
        sorted_ids = sorted(book_dict,
                      lambda x,y: cmp("%s%s" % (book_dict[x].author.lower(),
                                                book_dict[x].title.lower()),
                                      "%s%s" % (book_dict[y].author.lower(),
                                                book_dict[y].title.lower())))
        book_list = []
        bid = sorted_ids.pop(0)
        while bid:
            book_list.append(book_dict.pop(bid))
            try: bid = sorted_ids.pop(0)
            except: bid = None
        f = open(self.pickle_path, 'wb')
        cPickle.dump(book_list, f, -1)
        f.close()
        return True

class CatalogueDocumentHandler (xml.sax.handler.ContentHandler):
    def __init__(self, outfile, book_dict):
        self.outfile = outfile
        self.book_dict = book_dict
        self.init()

    def init(self):
        """Reset all variables to initial state."""
        self.bookid = ''
        self.title = 'Unknown'
        self.author = 'Unknown'
	self.subj = []
	self.loc = ''
        self.lang = ''
        self.filename = ''
        self.mdate = ''
        self.content = ''
        self.intext = False
        self.isZip = False
        self.isText = False

    def startElement(self, name, attrs):
        if name == 'pgterms:etext':
            self.context = name
            self.bookid = str(attrs.getValue('rdf:ID')[5:])
        elif name == 'pgterms:file':
            self.context = name
            self.filename = str(attrs.getValue('rdf:about')[30:])
        elif name in ['dc:title', 'dc:creator',
                      'dc:language', 'dc:subject',
                      'dc:format', 'dcterms:modified']:
            self.intext = True
        elif name == 'dcterms:isFormatOf':
            self.bookid = str(attrs.getValue('rdf:resource')[6:])

    def endElement(self, name):
	#print "subj: %s" % type(self.subj)
        if name == 'pgterms:etext':
            self.book_dict[self.bookid] = Ebook(self.bookid,
                                      self.title, self.author,
                                      self.subj, self.loc, self.lang)
            self.init()
        elif name == 'pgterms:file':
            if self.isText and self.isZip:
                book = self.book_dict[self.bookid]
                if book.filename:
                    if self.mdate > book.mdate:
                        book.filename = self.filename
                        book.mdate = self.mdate
                else:
                    book.filename = self.filename
                    book.mdate = self.mdate
            self.init()
        elif name == 'dc:title':
            self.title = self.cleanup(self.content)
            self.content = ''
            self.intext = False
        elif name == 'dc:creator':
            self.author = self.cleanup(self.content)
            self.content = ''
            self.intext = False
        elif name == 'dc:language':
            self.lang = self.cleanup(self.content)
            self.content = ''
            self.intext = False
        elif name == 'dcterms:LCSH':
            #if self.subj: self.subj = self.subj + ", "
	    #print self.cleanup(self.content)
            self.subj.append(self.cleanup(self.content))
            self.content = ''
            #self.intext = False
	elif name == 'dcterms:LCC':
	    self.loc = self.cleanup(self.content)
            self.content = ''
            self.intext = False
        elif name == 'dcterms:modified':
            self.mdate = self.cleanup(self.content)
            self.content = ''
            self.intext = False
        elif name == 'dc:format':
            clean_content = self.cleanup(self.content)
            if clean_content.startswith('text/plain'):
                self.isText = True
            elif clean_content == 'application/zip':
                self.isZip = True
            self.content = ''
            self.intext = False

    def characters(self, chars):
        if self.intext:
            self.content = self.content + chars

    def cleanup(self, words):
        words = words.split()
        words = ' '.join(words)
        words = words.encode('utf-8','replace')
        return words

class InvalidURLError (Exception):
    def __init__ (self, value):
        self.value = value

    def __str__ (self):
        return repr(self.value)

