def convert(feet_inches):
 output=feet_inches.split(" ")
 feet=float(output[0])
 inches=float(output[1])
 return {"feet" : feet  , "inches":inches}

def parse(feet,inches):
  measure= feet *0.3048 + inches *0.0254
  return measure    

""" 
we need to give return the output from above code as simple a possible ,
if we make this complex , then if  we need to have actual value from this output in some case then it becomes
difucult to extract from there
"""

feet_inch=input("please enter feet and inches")
output = parse(convert(feet_inch)["feet"],convert(feet_inch)["inches"])

print (f" {output} meters for given feet and inches ")