#!/ad/eng/research/eng_research_icsg/mixed/bobzhou/software/tools/bin/python3.4
import os
#regular expression
import re
#python gds related
import numpy
import gdspy


os.environ['LD_LIBRARY_PATH'] = os.getcwd()  # or whatever path you want

path		= './gds/'

#import the library
gdsii = gdspy.GdsImport('gds/NangateOpenCellLibrary.gds')
for cell_name in gdsii.cell_dict:
#extract the info in each standard library
    gdsii.extract(cell_name)
#    print ( cell_name )

#import the design
#design		= gdspy.GdsImport ( 'design/TjIn.gds' )
#extract the design
#gdsii		= design.extract ( 'top' )

#just draw some stuff
#gdsii . add ( gdspy . Rectangle ( (18, 1), (22, 2), 11) )
#display the design with showing the one layer of reference
#gdspy.LayoutViewer( cells={ 'top' } , depth=1 )
gdspy.LayoutViewer( cells={ 'FILLCELL_X1' } )
#export stuff
#gdspy.gds_print( 'test.gds', cells={'top'},unit=1e-06,precision=1e-09) 
