def ds(f="file"):
    try:
        file=open("File.txt","+a")
        file.writelines("roll no:09 \n name:Shraddha \n class:TYIF")
        file.seek(0)
        print(file.read())
    except IOError:
        print("Exception is handled")
ds()