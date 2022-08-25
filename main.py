from functions import *
from time import perf_counter

if __name__ == "__main__":
    start_time = perf_counter()
    functions.TCF()
    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.4f} second(s) to complete.')
    