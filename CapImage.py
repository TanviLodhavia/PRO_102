import cv2
import time
import random
import dropbox

start_time=time.time()
print(start_time)

def take_snapshot():
    #for generating random image name
    number=random.randint(1,100)
    print(number)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while (result):
        #Read Frames while Cam is on
        ret, frame = videoCaptureObject.read()
        #print(ret)
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        #print("Image Saved")
        result=False
    return img_name
    print("Snapshot Taken")


    #Releasing the webcam
    videoCaptureObject.release()

    #Close all windows that might have opened
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="jZSeeL46mVQAAAAAAAAAAXkbwOGGGTptMwkHZw_NBvqbTNHWpeFQMW2RxDVjGlVr"
    file=img_name
    file_from=file
    file_to="/NewFolder1"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded!")

def main():
    while (True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)

main()