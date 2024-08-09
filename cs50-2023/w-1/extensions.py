x=input("enter file name.extesion: ").strip().lower()

if ".jpg" in x :
    print("image/jpeg")
elif  ".jpeg" in x:
    print("image/jpeg")
elif ".gif"in x :
    print("image/gif")
elif ".png" in x:
    print("image/png")
elif ".pdf" in x :
    print("application/pdf")
elif ".zip" in x :
    print("application/zip")
elif ".txt" in x:
    print("text/plain")
else :
    print("application/octet-stream")