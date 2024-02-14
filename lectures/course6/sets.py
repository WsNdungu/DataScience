cookies_eaten_today = ["chocolate chip", "peanut butter", "choclate chip", "oatmeal cream", "chocolate chip"]

type_of_cookies_eaten = set(cookies_eaten_today)
print(type_of_cookies_eaten)

# Modifying a set - .add() method - add a single element
type_of_cookies_eaten.add("biscotti")
type_of_cookies_eaten.add("chocolate chip")
print(type_of_cookies_eaten)

# Modifying sets - .update() method - merges a set to another or list
cookies_hugo_ate = ["chocolate chip", "anzac"]
type_of_cookies_eaten.update(cookies_hugo_ate)
print(type_of_cookies_eaten)

# Removing data from sets
# 1 .discard() method - removes an element from the set by value(no error when value is not found)
# 2 .pop() method - Removes and returns an arbitrary elements from set(KeyError when empty)
type_of_cookies_eaten.discard("biscotti")
print(type_of_cookies_eaten)

type_of_cookies_eaten.pop()
type_of_cookies_eaten.pop()
