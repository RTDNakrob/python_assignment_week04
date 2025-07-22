children = [
    {"name": "Alice", "age": 2, "height": 95},
    {"name": "Bob", "age": 4, "height": 105},
    {"name": "Charlie", "age": 3, "height": 110},
    {"name": "David", "age": 5, "height": 102},
    {"name": "Eve", "age": 6, "height": 99}
]

eligible_children = [item for item in children if item["age"] > 3 and item["height"] > 100]

print(eligible_children)