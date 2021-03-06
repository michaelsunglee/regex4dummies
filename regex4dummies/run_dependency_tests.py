__author__ = 'Vale Tolpegin'

# Importing operating system related libraries
import os
import sys

# Importing other libraries needed for testing
import nltk
import nlpnet
from textblob import TextBlob

# Importing parsing related classes
from compare import compare
from gui_downloader import gui_downloader

# Importing GUI related classes
import Tkinter as tk
import ttk as ttk
import tkMessageBox

"""

This class will test to see whether the dependencies for the given parser are installed. In the event that they are not already installed, the program will ask the user whether to install them. If the user agrees, it will download and install the dependencies

Class information:

- name: run_dependency_tests
- version: 1.0.0

"""

class run_dependency_tests:
    # Blank constructor method
    def __init__( self, *args, **kwargs ):
        pass

    def test( self, parser_name ):
        # Testing for textblob corpora which is used in every parser
        self.test_for_textblob()

        # Testing for parser corpora for each parser
        if parser_name.lower() == 'nltk':
            self.test_for_nltk()
        elif parser_name.lower() == 'nlpnet':
            self.test_for_nlpnet()

        return

    def test_for_textblob( self ):
        # Attempting to use textblob. This will cause an error if the textblob corpora is not downloaded
        try:
            # Creating a textblob object
            my_blob = TextBlob( "This is the first test sentence. This is the second test sentence. This it the third and final test sentence." )

            # Testing to see whether the textblob corpora has been downloaded
            for sentence in my_blob.sentences:
                str_sentence = str( sentence )
        except:
            if tkMessageBox.askokcancel( "Dependency Downloader", "Would you like to download the dependencies for TextBlob? All parsers will not be able to be used until the dependencies are downloaded.\n\nThe required space is: 45.7 MB" ):
                textblob_downloader = gui_downloader()
                textblob_downloader.download( "TextBlob Corpora", "45.7 MB" )
                textblob_downloader.mainloop()
            else:
                print ""
                print "Dependencies MUST be downloaded to use this library's parsers."
                print ""

                exit( 0 )

    def test_for_nltk( self ):
        # Attempting to use nltk. This will cause an error if the corpora is not downloaded
        try:
            # Creating a new compare object
            compare_nltk = compare()

            # Comparing using the nltk parser
            compare_nltk.compare_strings( [ "Back at my desk, I poured and killed him a rattlesnake and some more rattlesnake", "the cat and the mouse in the house is sitting, in the house, on the mat", "time is it?", "what time is it here?", "This is the cat's hat" ], False, 'nltk'  )

            # If that was successfuly, getting information
            sentence_information = compare_nltk.get_sentence_information()
            for sentence in sentence_information:
                my_pattern           = "[ Pattern ]          : " + sentence.pattern
                my_subject           = "[ Subject ]          : " + sentence.subject
                my_verb              = "[ Verb ]             : " + sentence.verb
                my_object            = "[ Object ]           : " + sentence.object[0]
                my_reliability_score = "[ Reliability Score ]: " + str( sentence.reliability_score )
        except:
            # If it didn't work, this means the dependencies are missing from the system
            # The user will be asked whether he/she wants to install the dependencies. If so, they will be installed.
            # Otherwise, the program will quit and an error will appear saying the dependencies must be installed to use that parser
            if tkMessageBox.askokcancel( "Dependency Downloader", "Would you like to download the dependencies for nltk? The nltk parser will not be able to be used until the dependencies are downloaded.\n\nThe required space is: 1 GB" ):
                nltk_downloader = gui_downloader()
                nltk_downloader.download( "NLTK Corpora", "1 GB" )
                nltk_downloader.mainloop()
            else:
                print ""
                print "Dependencies MUST be downloaded to use this parser. Either do not use this parser, or download the dependencies."
                print ""

                exit( 0 )

    def test_for_nlpnet( self ):
        pass
