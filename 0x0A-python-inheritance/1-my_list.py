#!/usr/bin/python3
class MyList(list):

    def print_sorted(self):
        self.sort()
        for item in self:
            print(item, end=" ")
        print()


my_list = MyList([1, 5, 3, 2, 4])
my_list.print_sorted()

# Output:
# 1 2 3 4 5
