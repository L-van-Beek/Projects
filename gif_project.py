import imageio.v3 as iio
filenames = ["connor1.png", "connor2.png"]
images = []
for filename in filenames:
    images.append(iio.imread(filename)) # the .imread() method loads an image based on the file path. So now, our images variable has all the images. 
iio.imwrite("connor.gif", images, duration = 500, loop = 0) # .imwrite() method turns the images into a GIF


# It takes in four arguments: 
# - "team.gif": this is the name you want to give to your new GIF file
# - images: the list containing the image data
# - duration = 500: how long each picture should show in the GIF, in milliseconds
# - loop = 0: how many time the GIF should repeat (0 means it keeps looping forever). 
