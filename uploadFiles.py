import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))



def main():
    access_token = 'sl.BKMhowrsHPFIc_s3Ml4IzG1Xl3glAEKIgEbNfxzfGFZXWWC6SvCLKCDXhYC00UOf2qummz7OkpY5D7culH9FAgdPUode92z1eBXWJypkdWsD_tKW_oMJXV76gILnIDLhms9uaio'
    transferData = TransferData(access_token)

    file_from = input("enter the source file path :-  ")
    file_to = input("enter the full dropbox path for destination:-  ")



    transferData.upload_file(file_from,file_to)

if __name__=="__main__":
    main()