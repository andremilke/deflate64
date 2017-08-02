import argparse, zlib, base64

parser = argparse.ArgumentParser(description = 'Deflate64  Decripting Base 64 strings, decompress content')
group = parser.add_mutually_exclusive_group()
group.add_argument("-b", "--base64", action="store", dest="b", help="string in Base64 format")
group.add_argument("-u", "--uncompress", action="store", dest="u", help="compress string in Base64 format")
parser.add_argument("--txt",  dest="txt", action="store", help="enter the file name")
args = parser.parse_args()
def base64ToAnsi(s):
	return base64.b64decode(s)
"""
zlib can decompress all those formats:
    to (de-)compress deflate format, use wbits = -zlib.MAX_WBITS
    to (de-)compress zlib format, use wbits = zlib.MAX_WBITS
    to (de-)compress gzip format, use wbits = zlib.MAX_WBITS | 16
"""
def uncompressToAnsi(data):	
	return zlib.decompress(data, -zlib.MAX_WBITS)

def helpMessage():
 print ("""
Options:
  -h, --help                      show this help message and exit  
  -b, --base64                    text in Base64 format to decrypt
  -u, --decompress                compress text in Base64 format to decrypt  
  --txt                           Write the result in a txt  File (optional)
	 """)

def info():
 print ("""
Deflate64 - Decripting Base 64 strings, decompress content
\n   AndreMilke (Programmer and Ethical Hacker) - @andremilke \n 
   Usage: deflate64.py [-b, --base64     <keyword>]\n 		   	
                            [--txt Write txt file  ]\n                             
		  deflate64.py [-u, --decompress <keyword>]\n 		   	
                            [--txt Write txt file  ]\n                          
      \n              Get basic options and Help, use: -h\--help
	 """)
	 
def writeFile(file, data):        
    with open(file, 'wb') as filew:
        filew.write(data)		
		
if args.b:	
	value = base64ToAnsi(args.b)
	if args.txt:
		writeFile(args.txt, value)
	else:
		print(value)
elif args.u:	
	uncomp = base64ToAnsi(args.u)
	value = uncompressToAnsi(uncomp)
	if args.txt:
		writeFile(args.txt, value)
	else:
		print(value)
else:	
	info()
	

		

	 


