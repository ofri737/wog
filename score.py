from utils import SCORES_FILE_NAME

def add_score(difficulty):
    #params - score_file, current_score, POINT_OF_WINNING, newscore
    score_file = open(SCORES_FILE_NAME, "r+")
    current_score = score_file.readline()

    #newscore calculation
    if current_score.strip() != '':
        #file is not empty - not the first time
        current_score = int(current_score)
        POINT_OF_WINNING = (difficulty * 3) + 5
        newscore = current_score + POINT_OF_WINNING

    else:
        #file is empty - first time
        POINT_OF_WINNING = (difficulty * 3) + 5
        newscore = POINT_OF_WINNING

    #pointer postion - go to start
    score_file.seek(0)
    #override current score with new score
    score_file.write(str(newscore))