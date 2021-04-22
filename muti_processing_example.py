import threading

class EP:

    def __init__(self):
        self.t_list = []

    def dosomething(self, i):
        print('第' + str(i))
        print('執行緒 ID:' + str(threading.get_ident()))

    def run(self):
        for i in range(5):
            self.t_list.append(threading.Thread(target=self.dosomething, args=(str(i))))
            self.t_list[i].start()

        for i in self.t_list:
            i.join()

if __name__ == "__main__":
    d = EP()
    d.run()