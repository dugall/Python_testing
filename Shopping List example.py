class ShoppingList:
    def __init__(self, items):
        """ Parameters
            ----------
            items : Union[str, Iterable[str]]
                Iterable of item-names to add to shopping list"""
        if isinstance(items, str):
            items = [items]
        self._needed = set(items)
        self._purchased = set()
 
    def add_new_items(self, items):
        """ Add more items to the shopping list

            Parameters
            ----------
            items : Union[str, Iterable[str]]
                Iterable of item-names to add to shopping list"""
        if isinstance(items, str):
            items = [items]
        # set.update adds elements of an iterable to a set
        self._needed.update(items)

    def mark_purchased_items(self, items):
        """ Provide names of items to mark as 'purchased'

            Parameters
            ----------
            items : Union[str, Iterable[str]]"""
        if isinstance(items, str):
            items = [items]
        # only mark items as purchased that are on our list to begin with
        self._purchased.update(set(items) & self._needed)
        # remove all purchased items from our unpurchased set
        self._needed.difference_update(self._purchased)

    def list_purchased_items(self):
        """ Return a sorted list of the items that have been purchased"""
        return sorted(self._purchased)

    def list_unpurchased_items(self):
        """ Return a sorted list of the items still on the list"""
        return sorted(self._needed)


my_list = ShoppingList(["apples", "apples", "grapes", "peaches", "milk", "bread"])
print (my_list.list_unpurchased_items())
print (my_list.list_purchased_items())

# mark items as purchased on our list
my_list.mark_purchased_items(["grapes", "pineapples"])
print (my_list.list_purchased_items())
print (my_list.list_unpurchased_items())




