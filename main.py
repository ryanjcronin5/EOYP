from functions import *
from time import perf_counter
from datetime import date

MAXCARDS = 9
MAXPOINTS = 25
MINPOINTS = 1
NAMELIMIT = r"^[a-zA-Z0-9]*$"
eFlag = 0
iFlag = 0
day = date.today()
today = day.strftime("%d - %m - %y")



if __name__ == "__main__":
    functions.main()