# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import zipfile
import os

from pip._vendor.distlib.compat import raw_input

newDestDir = "/Users/pony/.gradle/caches/modules-2/files-2.1"
soName = "libemulator_check.so"



def getAllAARFilePath(rootdir, ends="aar"):
    all = []
    for path, dirs, fs in os.walk(rootdir):
        for f in fs:
            absoluteFilePath = os.path.join(path, f)
            if absoluteFilePath.endswith(ends):
                # print(absoluteFilePath)
                fsize = os.path.getsize(absoluteFilePath)
                # print("文件大小" + str(fsize))
                if fsize > 0:
                    all.append(absoluteFilePath)

    return all


# newFile: /Users/pony/.gradle/caches/modules-2/files-2.1/com.github.humorousz/FrameSequenceDrawable/1.0.1-SNAPSHOT/945d34d9cb4baaefbfe2d69b4afb364cf892628a/FrameSequenceDrawable-1.0.1-SNAPSHOT.aar
#
if __name__ == '__main__':
    _count = 0
    newDestDir = raw_input("1.请输入gradle缓存位置，(一般在:/Users/用户名/.gradle/caches/modules-2/files-2.1):")
    soName = raw_input("2.请输入SO库的名称，(例如:libffmpeg.so):")
    allAARs = getAllAARFilePath(newDestDir)
    for newFile in allAARs:
        zipFile = zipfile.ZipFile(newFile)
        for info in zipFile.infolist():
            if info.filename.endswith(soName):
                print("发现文件:", newFile, "so所在aar中的位置:", info.filename)
                _count += 1

    if _count == 0:
        print("Oops,没有找到")
