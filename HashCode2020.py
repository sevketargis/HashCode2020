
import statistics

class Library:
    def __init__(self, library_id, library_book_num, signup_day_num, books_per_day_num, library_book_list, mean_book_score):
        self.library_id = library_id;
        self.library_book_num = library_book_num;
        self.signup_day_num = signup_day_num;
        self.books_per_day_num = books_per_day_num;
        self.library_book_list = library_book_list;
        self.mean_book_score = mean_book_score
        self.daily_gain_metric = books_per_day_num * mean_book_score
    library_id = 0
    library_book_num = 0
    signup_day_num = 0
    books_per_day_num = 0
    library_book_list = []
    mean_book_score = 0
    daily_gain_metric = 0
    reading_start_day = 0
    start_flag = False
    read_book_list = list()

library_dict = dict()

sign_day_order_dict = dict()


with open("f_libraries_of_the_world.txt") as fp:
    line = fp.readline().split()
    book_num = int(line[0])
    lib_num = int(line[1])
    day_num = int(line[2])
    book_scores = list(map(int, fp.readline().split()))
    for i in range(lib_num):
        line_2 = list(map(int, fp.readline().split()))
        library_book_num = int(line_2[0])
        signup_day_num = int(line_2[1])
        books_per_day_num = int(line_2[2])
        library_book_list = list(map(int, fp.readline().split()))
        library_book_list.sort(reverse=True)
        mean_book_score = statistics.mean(library_book_list)

        library_dict[i] = Library(i, library_book_num, signup_day_num, books_per_day_num, library_book_list, mean_book_score)

        debug = 0

dict_list = list()
for key in library_dict:
    dict_list.append(library_dict[key])


daily_gain_metric_sorted = sorted(dict_list, key=lambda x: x.daily_gain_metric, reverse=False)

selected_library_list = list()
control_day = 0
remaining_day = day_num
while remaining_day >= 0 and control_day < day_num:
    possbile_gain = dict()
    for lib in daily_gain_metric_sorted:
        possbile_gain[lib.library_id] = lib.daily_gain_metric * (remaining_day - lib.signup_day_num)
        debug88 = 0

    max_score = -1000
    max_id = -1000
    for key in possbile_gain.keys():
        if possbile_gain[key] > max_score:
            max_id = key
            max_score = possbile_gain[key]
    selected_library_id = max_id


    remaining_day = remaining_day - lib.signup_day_num
    control_day = control_day + lib.signup_day_num
    if remaining_da y> =0:
        selected_library_list.append(library_dict[selected_library_id])
        selected_lib = library_dict[selected_library_id]
        selected_lib.reading_start_day = control_day
        daily_gain_metric_sorted.remove(library_dict[selected_library_id])


debug999 = 0

global_read_book_set = set()

total_capacity = 0
passed_day = 0
while passed_day < day_num:
    for lib in selected_library_list:
        if lib.reading_start_day == passed_day:
            total_capacity = total_capacity + lib.books_per_day_num
            for global_book in global_read_book_set:
                lib.library_book_list.remove(global_book)
            lib.start_flag = True

    for lib in selected_library_list:
        if lib.start_flag == True:
            lib.read_book_list = lib.read_book_list + lib.library_book_list[:lib.books_per_day_num]
            global_read_book_set.union(lib.library_book_list[:lib.books_per_day_num])
            del lib.library_book_list[:lib.books_per_day_num]

    passed_day = passed_day + 1
    debug88 = 0

print(len(selected_library_list))
for lib in selected_library_list:
    print(str(lib.library_id) + " " + str(len(lib.read_book_list)))
    book_list_text = ""
    for book in lib.read_book_list:
        book_list_text = book_list_text + " " + str(book)
    book_list_text = book_list_text[1:]
    print(book_list_text)