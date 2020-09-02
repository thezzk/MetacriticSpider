import pandas as pd
import pdb
genreReduceDataframe = pd.read_csv('./GenreReduce.csv', dtype={'mergeto': str, 'Genre': str, 'cnt': int})
finalGenreLst = []
genreReduceDic = {}
for item in genreReduceDataframe.iloc:
    mergeto = str(item.mergeto)
    mergeto = mergeto.strip()
    mergeto = mergeto.lower()
    found = False
    if mergeto == "x":
        genreReduceDic[item.Genre.strip().lower()] = "x"
        continue
    if mergeto == "" or mergeto == "nan":
        finalGenreLst.append(item.Genre.strip().lower())
        continue;
    #pdb.set_trace()
    for i in genreReduceDataframe.Genre:
        i = i.strip()
        i = i.lower()
        if i == mergeto:
            found = True
            break
    if found == False:
        print(mergeto + "-- Genre not find")
        break
    else:
        genreReduceDic[item.Genre.strip().lower()] = mergeto

print(finalGenreLst)
print(genreReduceDic)
print(genreReduceDataframe)
col = ['gameId', 'title'] + finalGenreLst
GenreStatDf = pd.DataFrame(columns=col)

gameDetailDataframe = pd.read_csv('../GameDetail.csv')
for item in gameDetailDataframe.iloc:
    genre = item.genre.strip().lower()
    genreFlagLst = [0] * len(finalGenreLst)
    for i in genre.split(','):
        i = i.strip().lower();
        if i != "":
            if genreReduceDic.__contains__(i) and genreReduceDic[i] != None:
                i = genreReduceDic[i]
                if(i == "x"):
                    continue
                
            for index in range(len(finalGenreLst)):
                if(finalGenreLst[index] == i):
                    genreFlagLst[index] = 1
    
    genreFlagLst = [item.gameId, item.title] + genreFlagLst
    #pdb.set_trace()
    newDf = pd.DataFrame(data = [genreFlagLst], columns = col)
    GenreStatDf = GenreStatDf.append(newDf, ignore_index = True)
GenreStatDf.to_csv('GenreStat.csv', index = False)
