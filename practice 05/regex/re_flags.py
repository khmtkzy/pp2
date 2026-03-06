import re
#RegEx FLAGS
re.ASCII	    #re.A	#Returns only ASCII matches	
re.DEBUG		        #Returns debug information	
re.DOTALL	    #re.S	#Makes the . character match all characters (including newline character)	
re.IGNORECASE	#re.I	#Case-insensitive matching	
re.MULTILINE	#re.M	#Returns only matches at the beginning of each line	
re.NOFLAG		        #Specifies that no flag is set for this pattern	
re.UNICODE	    #re.U	#Returns Unicode matches. This is default from Python 3. For Python 2: use this flag to return only Unicode matches	
re.VERBOSE	    #re.X	#Allows whitespaces and comments inside patterns. Makes the pattern more readable