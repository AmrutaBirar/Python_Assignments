formatter = "%r %r %r %r"

print formatter %(1,2,3,4)

print formatter %("one","two","three","four")
print formatter %(True,False,False,True)

#print %formatter
print formatter %(formatter,formatter,formatter,formatter)

print formatter %( 
 		"I had this thing",
 		"tht could type easily",
 		"now it doesnt work properly",
 		"so let it go......:P ")
 		
 		
