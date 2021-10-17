import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        image_name="image"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        result=False
    return image_name
    print("snapshot taken")
    videocaptureobject.release()
    cv2.destroyAllWindows()

def uploadfile(image_name):
    access_token="sl.A6iaRFipc-qlhEVGAlkgDqZi0SmfGbz4rZBksP06dSXHp5SruOpkX8l7eI0XFcS2bp1fSPrXQQ1ZP5JCNo7fb7KR-pmsy7IXxnYuaeEjH1gsxt2fI_tOtJd-pTTdbQBAJNjhqkCeW4o"
    file=image_name
    file_from=file
    file_to="/newfolder/"+(image_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        print(time.time()-start_time)
        if ((time.time()-start_time)>=5):
            print("taken")
            name=take_snapshot()
            uploadfile(name)
main()