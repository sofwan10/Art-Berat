import ascii_magic
output = ascii_magic.from_image_file("girl.jpg",columns=200,char="#")   # put any image in your folder to print out the image
ascii_magic.to_terminal(output)
