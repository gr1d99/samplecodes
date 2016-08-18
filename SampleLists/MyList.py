class MyList:
    """
    a simple class that allows you to manipulate lists.

    Usage:
    l = MyList()
    l.add_items(1,2,3)

    all functions defined in this class are self explanatory.
    """

    def __init__(self):
        self.items = []

    def add_items(self, *items):
        """
        items are added to the attribute `self.items` which is initialized
        as a list.

        :param items: holds items to be added to the list.
        :return: returns all items.
        """
        for item in items:
            self.items.append(item)
        return self.items

    def get_item_index(self, item):
        return 'item {0} index is {1}'.format(item, self.items.index(item))

    def show_all_items(self):
        """
        :return: returns all items of the current object.
        """
        return self.items

    def count_items(self):
        """
        counts and returns the number of all items.
        """
        return len(self.items)

    def replace_item_using_its_index(self, item_index, new_item):
        try:
            self.items[item_index] = new_item
        except IndexError:
            raise IndexError('index %s is out of range' % item_index)
        else:
            return self.items

    def remove_specific_item(self, item):
        """
        :param item: refers to the specific item in the list that you want to remove.
        :return: returns all items of the current object.
        """
        self.items.remove(item)
        return self.items

    def remove_any_item(self):
        """
        removes any item at the end of the list.
        :return:
        """
        self.items.pop()
        return self.items

    def add_another_list_to_items(self, iterable):
        """
        it adds anything that is iterable to the current object list.
        :param iterable: anything iterable eg. [1,2,4], {1: 2}
        """
        self.items.extend(iterable)
        return self.items

    def reverse_items(self):
        """
        reverses the oder of items.
        """
        self.items.reverse()
        return self.items

    def sort_items(self):
        self.items.sort()
        return self.items


