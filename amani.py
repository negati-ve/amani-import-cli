# const testFolder = '/Users/zed/Downloads/walletpics/9';
import pandas as pd
from os import listdir
from os.path import isfile, join,splitext
df = pd.read_csv ('./csv/03.csv', dtype={'picture no.': str})
df['images']=df['images'].astype('string')
def getImages(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    finalFiles = []
    for i in onlyfiles:
        filename, file_extension = splitext(i)
        filename=filename+'-scaled'
        filename= filename.replace(' ','-')
        filename= filename.replace('(','')
        filename= filename.replace(')','')
        filename = filename
        finalFiles.append(filename+file_extension)
    return ",".join(finalFiles)

for i,r in df.iterrows():
    print(str(int(r[2])))
    final=getImages('/Users/zed/Downloads/allamani/'+(r[2]))
    # print(final)
    # print(r[2],r[3])
    df.at[i, 'images'] = final
    # r[3] = final

df.to_csv('file_name.csv', index=False)


