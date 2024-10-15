

def WhoLikes(alst):

    
    if len(alst)==0:
        return "no one likes this"
    elif len(alst)==1:
        return f"{alst[0]} likes this"
    elif len(alst)==2:
        return f"{alst[0]} and {alst[1]} likes this"
    elif len(alst)==3:
        return f"{alst[0]},{alst[1]} and {alst[2]} likes this"
    else :
        return f"{alst[0]},{alst[1]} and 2 others likes this"
    
    







def main():
     print(WhoLikes([]))
     print(WhoLikes(['Peter']))
     print(WhoLikes(['Peter', 'Alex']))
     print(WhoLikes(['Peter','Alex','Mark']))
     print(WhoLikes(['Peter','Alex','Mark','Jacob']))
    
   


if __name__ == "__main__":
    main()


