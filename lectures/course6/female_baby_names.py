#open the text file  
with open('./data/female_baby_names_2012.txt', 'r') as f: 
  #read the text file into a list of lines 
  lines = f.readlines() 
 
#create an empty dictionary 
female_baby_names_2012= {} 
 
#loop through the lines in the text file  
for line in lines: 
  #split the line on ':' 
  key, value = line.split(',') 
  #strip the whitespace 
  key = key.strip() 
  value = value.strip() 
  #add the key, value pair to the dictionary 
  female_baby_names_2012[key] = value 
   
#print the dictionary 
print(female_baby_names_2012) 