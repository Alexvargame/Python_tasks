from pprint import pprint
import random
import math

TIMESTAMPS_COUNT =50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps




def get_score(game_stamps, offset=0):
    home=away=0
    for st in game_stamps:
        if st.get('offset',None):
            home,away=st['score']['home'],st['score']['away']
        if st['offset']>offset:
            #print(st['offset'],st.get('offset',None)==offset)
            st_previous=game_stamps[game_stamps.index(st)-1]
            home, away = st_previous['score']['home'], st_previous['score']['away']
            break
    return home, away
                                                    
def main():
    game_stamps = generate_game()
    for off in range(30000,100000,1121):
        score=get_score(game_stamps,off)
        print(score)

   

    


   


if __name__ == "__main__":
    main()

