str_="пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете."

print(str_)
if str_.islower(): str_.capitalize()
print(str_.find("сопровождать"))
print(str_.replace("сопровождать","поддерживать"))
lst=str_.split(",")
print(lst)
str_1=(",").join(lst)
print(str_1)
