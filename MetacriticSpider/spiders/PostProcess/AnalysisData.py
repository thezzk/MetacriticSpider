import pandas as pd

gameDetailDataframe = pd.read_csv('.。/GameDetail.csv')
genreLst = []
for item in gameDetailDataframe.genre:
    item = item.strip()
    for i in item.split(','):
        i = i.strip();
        if i != "":
            genreLst.append(i)

genreDataframe = pd.DataFrame(data = {'Genre' : genreLst})
cntDf = genreDataframe.groupby(['Genre'],as_index=False)['Genre'].agg({'cnt':'count'})
cntDf = cntDf.sort_values(by=['cnt'])
cntDf.to_csv('GenreCnt.csv', index = False)