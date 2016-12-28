SERVER_IP = "ftp.kozos.comule.com"
USER = "a1151360"
PASSWORD = "agyacska000"
DIR = False
NAME = "x.test"
CONTENT = "9999"

# FTP upload
import ftplib
import io
ftp = ftplib.FTP(SERVER_IP)
ftp.login(USER, PASSWORD)
if DIR:
    ftp.cwd(DIR)
counter = 290

while counter < 300:
    myfile = io.BytesIO()
    myfile.write(bytes(str(counter+10**1000), 'UTF-8'))
    myfile.seek(0)
    print (ftp.storlines("STOR " + NAME, myfile))
    print("-------------------------")
    if counter < 299:
        counter += 1
    else:
        counter = 1
    print (counter)
