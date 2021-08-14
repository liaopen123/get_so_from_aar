# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import zipfile
import os
import shutil

newDestDir= "/Users/pony/Desktop/aar/"
def printSOFile(rootDir):
   files =getAllAARFilePath(rootDir)
   moveFileToDeskAndReName(files)
   # newfiles =getAllAARFilePath(newDestDir)
   # for newFile in newfiles:
   #     zipFile = zipfile.ZipFile(newFile)
   #     print(zipFile.infolist())

def moveFileToDeskAndReName(files):
    for f in files:
        fileName = f.split("/")[-1].split(".")[0]+".zip"
        shutil.copyfile(f, '/Users/pony/Desktop/aar/'+fileName)


def getAllAARFilePath(rootdir,ends="aar"):
    all = []
    for path,dirs,fs in os.walk(rootdir):
        for f in  fs:
            absoluteFilePath = os.path.join(path,f)
            if absoluteFilePath.endswith(ends):
                print(absoluteFilePath)
                fsize = os.path.getsize(absoluteFilePath)
                print("文件大小"+str(fsize))
                if fsize>0:
                    all.append(absoluteFilePath)

    return all

if __name__ == '__main__':
    # printSOFile("/Users/pony/.gradle/caches/modules-2/files-2.1")
    newfiles = getAllAARFilePath(newDestDir,"zip")
    for newFile in newfiles:
        zipFile = zipfile.ZipFile(newFile)
        for info in zipFile.infolist():
            if info.filename.endswith(".so"):
                print(newFile+info.filename)

