
import urllib.request
dwn_link = "https://firebasestorage.googleapis.com/v0/b/speechai2.appspot.com/o/speeches%2FA8E5E98A-346C-44DD-A8CE-323621634838.wav?alt=media&token=c40dfd75-61a5-4f72-b962-39da1e6fefd8"
file_name = "test.wav"
rsp = urllib.request.urlopen(dwn_link)
with open(file_name, "wb") as f:
   f.write(rsp.read())