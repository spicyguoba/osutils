#!/usr/local/bin/python3
# requires pyobjc, colorama
import sys, re
try:
	from DictionaryServices import *
except:
	print("WARNING: The pyobjc Python library was not found. You can install it by typing: 'pip install -U pyobjc'")
	print("..................\n")
try:
	from colorama import Fore, Back, Style
except:
	print("WARNING: The colorama Python library was not found. You can install it by typing: 'pip install colorama'")
	print("..................\n")

def main():
    try:
        searchword = sys.argv[1]
    except IndexError:
        errmsg = 'You did not enter any terms to look up in the Dictionary.'
        print(errmsg)
        sys.exit()
    wordrange = (0, len(searchword))
    dictresult = DCSCopyTextDefinition(None, searchword, wordrange)
    if not dictresult:
        errmsg = "'%s' not found in Dictionary." % (searchword)
        print(errmsg)
    else:
        s = dictresult

        s = re.sub(r'([0-9]) ', doColor(r'\n\n\1 ', 'important'), s)

        bullet = doColor("\n• ", "red")
        s = s.replace('•', bullet)  # bullet
		
        phrases_header = doColor("\n\nPHRASES\n", "important")
        s = s.replace('PHRASES', phrases_header)
		
        derivatives_header = doColor("\n\nDERIVATIVES\n", "important")
        s = s.replace('DERIVATIVES', derivatives_header)
		
        origin_header = doColor("\n\nORIGIN\n", "important")
        s = s.replace('ORIGIN', origin_header)
        
        print(s)

def doColor(s, style=None):
	"""
	util for returning a colored string
	if colorama is not installed, FAIL SILENTLY
	"""
	try:
		if style == "comment":
			s = Style.DIM + s + Style.RESET_ALL
		elif style == "important":
			s = Style.BRIGHT + s + Style.RESET_ALL
		elif style == "normal":
			s = Style.RESET_ALL + s + Style.RESET_ALL	
		elif style == "red":
			s = Fore.RED + s + Style.RESET_ALL	
		elif style == "green":
			s = Fore.GREEN + s + Style.RESET_ALL			
	except: 
		pass
	return s

if __name__ == '__main__':
    main()
