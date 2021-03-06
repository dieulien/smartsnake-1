import random
import datetime
import time

class GameLogger:
    def __init__(self, info):
        self.log_file = open("autogame_log.txt", "a")
        current_time = datetime.datetime.now()
        self.log_file.write("--------------- LOGGING BEGINS --------------")
        self.log_file.write("GameLogger called at" + str(current_time) + ", for agent: " + info + "\n")
        print(("GameLogger called at" + str(current_time) + ", for agent: " + info))
        # self.log_file.close()
        self.snakelength = 0
        self.start_time = time.time()
        self.duration = 0.0
        self.duration_list = []
        self.duration_list2 = []
        self.path_list = []
        self.successor_counts = []
        self.agent_name = info
        self.snakelength = 0

    def list_to_string(self, list):
        ', '.join(list)

    #called when the game is over
    def record_snake_length(self, snakelength):
        self.snakelength = snakelength

    def log_snake_length(self):
        self.log_file.write("Total Snake length: " + str(self.snakelength) + "\n")
        print("Total Snake length: " + str(self.snakelength) + "\n")

    def start_timer(self):
        self.start_time = time.time()

    def record_get_path_time(self):
        end_time = time.time()
        duration = round(end_time - self.start_time, 6)
        print("Algorithm runs for " + str(duration) + " seconds")
        self.duration_list.append(duration)

    def record_eat_fruit_time(self):
        end_time = time.time()
        duration = end_time - self.start_time
        self.duration_list2.append(duration)

    def record_path(self, path_length):
        self.path_list.append(path_length)

    def log_path_lengths(self):
        path_lengths = self.path_list
        self.log_file.write((', '.join(str(x) for x in path_lengths))+ "\n")

    def record_succesor_count(self, successor_count):
        self.successor_counts.append(successor_count)
        print("States Expanded so far: " + str(successor_count))

    def log_succesor_counts(self):
        self.log_file.write("Succesor counts: " + str(self.successor_counts) + "\n")

    def log_path_list(self):
        self.log_file.write("path list: ")
        self.log_file.write(str(self.path_list) +"\n")

    def log_path_length(self):
        path_list_lens = map(len, self.path_list)
        self.log_file.write(str(path_list_lens))

    def get_avg_path_length(self):
        self.log_file.write("average path length: ")
        if not len(self.path_list) == 0:
            self.log_file.write(str((sum(self.path_list) / float(len(self.path_list))))+ "\n")

    def get_avg_duration(self):
        self.log_file.write("average duration: ")
        if not len(self.path_list) == 0:
            avg_duration = round(sum(self.duration_list)/ float(len(self.duration_list)), 6)
            self.log_file.write(str(avg_duration) + "\n")

    def log_duration(self):
        self.log_file.write(', '.join(str(x) for x in self.duration_list) + "\n")

    def report_exit(self):
        self.log_file.write("urgent exit")
        self.log_succesor_counts()
        self.log_path_list()
        self.log_file.close()

    def normal_game_end(self):

        self.log_file.write("SUMMARY of GAME RESULT using Agent "+ str(self.agent_name) + "\n")
        self.log_snake_length()
        self.log_succesor_counts()
        self.log_duration()
        self.log_path_lengths()
        self.get_avg_path_length()
        self.get_avg_duration()
        self.log_file.close()


class RandList:
    def __init__(self):
        self.all_list = [self.rl1, self.rl2, self.rl3, self.rl4, self.rl5, self.rl6, self.rl7, self.rl8, self.rl9]
        self.rl1 = [5, 2, 0, 7, 3, 0, 4, 5, 7, 4, 1, 6, 5, 3, 6, 1,
                    2, 6, 3, 6, 7, 0, 3, 5, 4, 2, 4, 1, 2, 5, 5, 6,
                    4, 7, 1, 2, 1, 0, 3, 3, 0, 3, 6, 0, 5, 3, 6, 6,
                    3, 7, 5, 3, 7, 3, 4, 3, 5, 7, 1, 4, 7, 5, 7, 4,
                    4, 7, 0, 3, 5, 6, 1, 1, 1, 4, 7, 3, 4, 7, 4, 7,
                    5, 1, 2, 0, 4, 0, 1, 1, 5, 6, 7, 1, 5, 3, 5, 6,
                    7, 1, 0, 2, 0, 2, 7, 6, 2, 5, 7, 6, 5, 6, 4, 2,
                    5, 1, 1, 2, 7, 0, 5, 3, 3, 5, 3, 2, 7, 7, 3, 4]

        self.rl2 = [1,3,4,2,5,5,4,1,0,6,4,4,3,2,4,2,
                    2,2,1,1,7,4,5,6,7,6,1,6,2,6,4,4,
                    4,0,4,6,4,2,5,6,2,0,7,7,3,3,7,4,
                    0,3,3,7,1,3,7,4,0,1,3,6,6,5,4,7,
                    7,3,2,6,0,4,2,2,1,1,2,5,7,0,1,5,
                    1,5,4,7,0,0,5,6,6,0,6,4,7,4,7,7,
                    2,7,5,6,4,0,5,3,6,6,0,4,1,2,1,3,
                    7,3,1,5,5,0,2,1,6,4,5,3,2,3,7,1]

        self.rl3 = [6,4,0,7,2,5,1,7,4,4,6,5,4,1,0,7,
                    0,6,2,0,4,3,5,1,5,3,5,3,0,0,0,1,
                    4,7,7,7,7,6,5,1,5,2,3,7,4,3,7,6,
                    6,2,2,1,1,1,1,3,7,0,5,3,3,2,3,6,
                    0,4,6,6,6,6,1,2,0,0,0,4,6,0,3,7,
                    5,2,1,3,4,1,2,7,6,1,7,3,5,5,6,2,
                    2,6,3,4,3,3,0,6,3,7,4,4,4,4,5,0,
                    5,6,2,3,5,4,1,4,3,4,3,4,1,5,2,6]

        self.rl4 = [1,5,4,1,1,3,2,6,4,5,3,6,4,5,7,4,
                    0,6,2,7,4,2,2,6,1,6,2,0,1,6,1,5,
                    6,5,1,1,3,4,7,3,5,7,4,3,4,2,5,3,
                    2,3,6,3,5,2,2,5,3,7,0,2,1,4,3,3,
                    7,1,1,2,3,0,5,3,6,1,1,5,4,1,4,5,
                    2,3,3,3,7,6,6,3,4,6,3,1,7,0,5,2,
                    7,0,4,3,6,1,1,6,1,4,7,0,3,0,1,5,
                    4,7,5,0,7,7,4,0,3,7,4,0,1,2,6,6]

        self.rl5 = [4,6,1,2,4,3,1,3,2,3,1,7,0,1,1,3,
                    7,5,3,1,6,2,6,1,0,0,1,7,6,6,7,5,
                    4,4,1,0,1,0,0,4,1,2,4,1,2,7,4,4,
                    1,1,1,6,7,4,5,0,3,2,0,4,1,7,5,4,
                    2,2,2,0,0,2,6,0,0,6,3,4,1,0,2,5,
                    4,3,0,5,6,5,1,0,1,4,4,2,5,4,5,7,
                    7,3,6,1,6,4,1,3,7,1,3,0,3,3,2,7,
                    6,1,7,4,7,5,5,5,7,7,3,2,3,5,5,3]

        self.rl5 = [4, 6, 1, 2, 4, 3, 1, 3, 2, 3, 1, 7, 0, 1, 1, 3,
                    7, 5, 3, 1, 6, 2, 6, 1, 0, 0, 1, 7, 6, 6, 7, 5,
                    4, 4, 1, 0, 1, 0, 0, 4, 1, 2, 4, 1, 2, 7, 4, 4,
                    1, 1, 1, 6, 7, 4, 5, 0, 3, 2, 0, 4, 1, 7, 5, 4,
                    2, 2, 2, 0, 0, 2, 6, 0, 0, 6, 3, 4, 1, 0, 2, 5,
                    4, 3, 0, 5, 6, 5, 1, 0, 1, 4, 4, 2, 5, 4, 5, 7,
                    7, 3, 6, 1, 6, 4, 1, 3, 7, 1, 3, 0, 3, 3, 2, 7,
                    6, 1, 7, 4, 7, 5, 5, 5, 7, 7, 3, 2, 3, 5, 5, 3]

        self.rl6 = [0,0,3,2,6,2,5,0,6,0,4,6,0,3,6,6,
                    5,0,0,3,6,1,5,3,7,6,5,3,2,2,1,0,
                    1,1,7,2,3,2,3,2,5,6,0,7,4,4,7,3,
                    6,3,4,6,7,0,6,3,0,6,1,0,5,0,4,2,
                    3,4,4,2,2,2,5,6,1,5,3,3,3,6,2,4,
                    1,1,4,1,7,0,1,2,7,3,2,6,0,5,5,1,
                    1,1,4,0,6,4,7,3,3,0,3,3,3,0,6,4,
                    3,1,0,7,2,3,4,0,6,4,7,5,3,1,7,6]

        self.rl7 = [0,6,5,1,7,4,6,5,6,6,4,7,2,3,6,1,
                    4,2,1,4,7,0,4,7,1,0,0,7,4,7,7,7,
                    0,7,1,7,7,1,5,6,0,6,6,4,5,4,7,4,
                    1,6,1,1,2,3,6,3,0,1,6,3,5,2,6,1,
                    2,0,2,2,2,2,5,7,3,2,1,4,4,1,3,2,
                    0,4,3,1,7,1,3,3,5,3,2,4,2,6,2,6,
                    7,2,6,4,2,6,7,6,6,1,1,0,2,6,0,7,
                    6,4,3,4,2,3,2,2,1,3,3,6,4,3,0,0]

        self.rl8 = [4,3,6,0,1,2,7,2,7,4,7,2,4,1,7,0,
                    0,6,4,7,0,1,4,3,4,0,1,6,0,6,4,2,
                    0,2,2,0,6,7,2,2,7,4,6,3,2,4,0,3,
                    5,2,2,1,3,2,6,3,5,4,4,6,2,3,1,6,
                    1,3,4,6,5,6,7,3,5,3,5,7,2,6,4,3,
                    2,5,5,1,1,4,3,4,2,7,2,5,7,6,4,0,
                    6,2,5,0,7,2,5,4,6,0,1,7,2,7,2,5,
                    3,5,7,6,2,3,6,6,2,4,4,3,2,3,5,6]

        self.rl9 = [7,2,3,6,1,4,6,1,6,5,0,7,6,6,7,0,
                    1,7,5,5,1,6,3,6,6,5,0,4,2,5,7,6,
                    5,6,0,1,5,3,7,2,5,0,7,4,0,2,4,5,
                    4,5,4,5,4,5,5,2,1,0,5,0,4,2,0,2,
                    7,6,4,3,5,1,0,3,3,6,4,5,2,4,6,5,
                    4,2,3,7,7,7,7,0,6,6,7,5,2,2,1,4,
                    3,5,6,7,3,6,7,6,5,3,4,4,7,0,7,1,
                    0,5,5,5,7,1,3,1,6,4,1,6,3,5,0,1]

        self.rl10 = [3,1,3,4,6,6,1,4,0,3,7,0,6,7,5,2,
                    4,1,7,0,7,2,1,2,7,7,2,1,7,0,7,7,
                    1,0,6,5,5,7,7,2,5,3,7,4,7,6,3,3,
                    0,7,0,3,3,1,4,3,5,7,4,2,7,6,3,6,
                    7,5,0,3,7,2,2,2,4,4,1,7,3,1,0,4,
                    7,3,5,4,1,4,5,2,2,1,0,6,5,3,5,6,
                    5,4,4,6,5,3,5,6,3,4,4,6,6,1,1,3,
                    1,6,1,1,5,5,0,6,2,2,2,4,7,5,3,0]

#RandListGenerator: create random lists on-the-go
class RandListGenerator:
    def __init__(self):
        self.list = []
        for i in range(0, 8):
            for j in range(0, 16):
                num = random.randrange(0, 8)
                self.list.append(num)

    def rand_list(self):
        return self.list
