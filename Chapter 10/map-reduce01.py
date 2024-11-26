from collections import defaultdict


def map_function(text):
    words = text.split()
    print("Map results: ", [(word, 1) for word in words])
    return [(word, 1) for word in words]


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    print("Shuffle results: ", shuffled.items())
    return shuffled.items()


def reduce_function(shuffled_values):
    reduced = {}
    for key, values in shuffled_values:
        reduced[key] = sum(values)
    print("Reduce results: ",   reduced)
    return reduced


# Виконання MapReduce
def map_reduce(text):
    # Крок 1: Маппінг
    mapped_values = map_function(text)

    # Крок 2: Shuffle
    shuffled_values = shuffle_function(mapped_values)

    # Крок 3: Редукція
    reduced_values = reduce_function(shuffled_values)

    return reduced_values


if __name__ == "__main__":
    # Вхідний текст для обробки
    text = "hello world hello Python hello Student"

    # Виконання MapReduce на вхідному тексті
    result = map_reduce(text)

    print("Результат підрахунку слів:", result)
