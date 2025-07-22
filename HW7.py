children = [
    {"name": "Alice", "age": 2, "height": 95},
    {"name": "Bob", "age": 4, "height": 105},
    {"name": "Charlie", "age": 3, "height": 110},
    {"name": "David", "age": 5, "height": 102},
    {"name": "Eve", "age": 6, "height": 99}
]
is_filter = lambda children:children["age"]>3 and children["height"]>100

eligible_children = list(filter(is_filter,children))
print(eligible_children)