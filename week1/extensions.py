def extension() :
    e = input("write  your file name : ")
    e = e.lower()
    e = e.strip()
    last = e.split(".")[-1]
    if   last == "gif" :
        print("image/gif")
    elif last == "jpg" :
        print("image/jpeg")
    elif last == "jpeg" :
        print("image/jpeg")
    elif last == "png" :
        print("image/png")
    elif last == "pdf" :
        print("application/pdf")
    elif last == "txt" :
        print("text/plain")
    elif last == "zip" :
            print("application/zip")
    else :
         print("application/octet-stream")
extension()
