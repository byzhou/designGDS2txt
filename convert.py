#!/ad/eng/research/eng_research_icsg/mixed/bobzhou/software/tools/bin/python3.4

import os
#regular expression
import re
#python gds related
import numpy
import gdspy

#import the library
library = gdspy.GdsImport('gds/NangateOpenCellLibrary.gds')
for cell_name in library.cell_dict:
#extract the info in each standard library
    library.extract(cell_name)
#    print ( cell_name )

#import the design
design		= gdspy.GdsImport ( 'design/TjIn.gds' )
#extract the design
gdsii		= design.extract ( 'top' )

#display the design with showing the one layer of reference
gdspy.LayoutViewer( cells={ 'top' } , depth=1 )

#write to file
outputPath  = 'txt/'
cellName    = 'TjIn'
writeFile   = open ( outputPath + cellName + '.txt' , 'w' )
print ( "open the file %s.txt\n" % cellName )

#get polygon info from the cell
polyinfo	= gdsii.get_polygons() 

#print cell attributes values
cellInst	= vars ( gdsii )
#search for word begin with 0x
regux	   = re.compile ( "0x\w+" )
#transform data type
strInst	 = str ( cellInst )
#search for regux, the first matched value is stored in firstInst
firstInst   = ( regux . search ( strInst ) ) . group ()
#All the info of the polygon including the layer info
instWithLayer = gdsii.get_polygons ( firstInst )
#transform into string
strWithLayer = str ( instWithLayer )

#print ( strWithLayer )
writeFile . write ( "11th layer" )
#Search for the 10th layer's polygon info
startToken  = re.compile ( "\(11\, 0\)\: \[array\(\[\[" )
#find out the start position of the layer 10
startpos	= ( startToken . search ( strWithLayer ) ) . start ()
#end token of layer 10
endToken	= re.compile ( "\(\w+\, 0\)\: \[array\(\[\[" )
#find out the end position of the layer 10
endpos	  = ( endToken . search ( strWithLayer , startpos + 1 ) ) . start ()
#find out the number tokens on the layer 10
numToken	= re.compile ( "\w\.\s" "|\w\w\.\s" "|[-|\s]\w+\.\w+" "|array" )
#write all the coordinates
coords	  = ( numToken . findall ( strWithLayer , startpos , endpos ) ) 
#print type ( coords )
for x in coords :
    if  x == "array" :
        #writeFile . write ( "  ;\n" + "POLYGON " ) 
        writeFile . write ( "\n" + "POLYGON " ) 
    else :
        writeFile . write ( str ( x ) + " " ) 

writeFile.close()
