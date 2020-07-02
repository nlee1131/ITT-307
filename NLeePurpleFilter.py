#Purple Filter Program
#Nathaniel Lee, 2020

#TO RUN:
#Load the program.
#Type "main()" in the command prompt
#Hit 'Enter' key


#Method to reduce green
def reduceGreen(pic):
  for p in getPixels(pic):
    #Reduce green value by 0.05
    setGreen(p, getGreen(p)*0.95)

#Method to loop for user approval
def main():
  #Select an image
  file = pickAFile()
  image = makePicture(file)
  explore(image)
  #Variable to continue
  varCont = true
  #Loop the green reducer
  while(varCont):
   #Reduce green
   reduceGreen(image)
   #Repaint image
   explore(image)
   #Check for user approval
   conVar = requestNumber("Enter 1 to continue, 0 to stop.")
   if conVar == 0:
     varCont = false
   else:
     continue
  #End the process
  showInformation("Process complete!")
  show(image)