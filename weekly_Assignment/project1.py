import sys
import os


class StudentInfo:

    student_info = dict()

    def __init__(self):
        if len(sys.argv) < 2:
            print("ERROR: please insert file")
        else:
            read_file_name = sys.argv[1]

            if os.path.exists(read_file_name):
                fr = open(read_file_name, "r")
                # fd = dict()
                fn = fr.readlines()
                s = ''.join(fn).split('\n')
                for x in range(0, len(s)):
                    info_list = s[x].split('\t')
                    StudentInfo.student_info[info_list[0]] = info_list[1::]

                print("++++++++++File Read!!!++++++++++\n")
                fr.close()

            else:
                print("ERROR: File Name is wrong or not exist!")

    def show(self, keys):
        print("+++++++this is show+++++++\n")
        st_dic = StudentInfo.student_info

        print("Student\t\tName \tMidterm\t Final \t Average \t Grage")
        print("-------------------------------------------------------")
        for key in st_dic:
            if key in keys:
                print("{}\t{}\t{}\t{}".format(key, st_dic[key][0], st_dic[key][1], st_dic[key][2]))

    def search(self, keys):
        sid = input("Student ID: ")
        flag = 0

        # print(self.student_info.keys())
        for key in keys:
            if sid == key:
                flag = 1
                self.show(sid)

        if flag == 0:
            print("NO SUCH PERSON.")

    def changescore(self, dic):
        print("this si Changescore")
        


    def searchgrade(self, dic):
        print("this is searchgrade")


    def add(self, dic):
        print("this is Add")


    def remove(self, dic):
        print("this is remove")


    def quit(self, dic):
        print("Quit")


def main():
    stinfo = StudentInfo()

    while 1:
        command = input("# ").lower()

        if command == 'show':
            stinfo.show(stinfo.student_info.keys())

        elif command == 'search':
            stinfo.search(stinfo.student_info.keys())

        elif command == 'changescore':
            stinfo.changescore()

        elif command == 'searchgrad':
            stinfo.searchgrade()

        elif command == 'add':
            stinfo.add()

        elif command == 'remove':
            stinfo.remove()

        elif command == 'quit':
            # answ = input("Save data?[yes/no] ")
            break
        else:
            command = input("# ").lower()


if __name__ == '__main__':
    main()
