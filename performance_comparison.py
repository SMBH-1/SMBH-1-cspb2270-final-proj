import timeit
import random
import string


def generate_random_words_list(length):
    words = []
    for _ in range(length):
        word = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        words.append(word)
    words.sort()
    return words

# def generate_random_words_list(length):
#     words = []
#     for _ in range(length):
#         word = ''.join(random.choice(string.ascii_lowercase) for _ in range(9))
#         words.append(word)
#     words.sort()
#     left_part = words[:length // 2]
#     right_part = words[length // 2:]
#     imbalanced_words = []
#     for i in range(len(left_part)):
#         imbalanced_words.append(left_part[i])
#         if i < len(right_part):
#             imbalanced_words.append(right_part[i])
#     return imbalanced_words


def run_performance_comparison(instance_skip_list, instance_avl_tree, words_list):
    # Measure insertion time
    skip_list_insert_time = timeit.timeit(stmt="for word in words_list: instance_skip_list.skip_list_insert(word)",
                                          globals={"instance_skip_list": instance_skip_list, "words_list": words_list},
                                          number=1)
    avl_tree_insert_time = timeit.timeit(
        stmt="for word in words_list: instance_avl_tree.avl_tree_insert(instance_avl_tree.root, word, word)",
        globals={"instance_avl_tree": instance_avl_tree, "words_list": words_list},
        number=1)
    print("Insertion time (SkipList):", skip_list_insert_time)
    print("Insertion time (AVLTree):", avl_tree_insert_time)

    # Randomly select a word for search and deletion
    search_word = random.choice(words_list)
    delete_word = random.choice(words_list)

    # Measure searching time
    skip_list_search_time = timeit.timeit(stmt="instance_skip_list.skip_list_search(search_word)",
                                          globals={"instance_skip_list": instance_skip_list,
                                                   "search_word": search_word},
                                          number=1000)
    avl_tree_search_time = timeit.timeit(stmt="instance_avl_tree.avl_tree_search(instance_avl_tree.root, search_word)",
                                         globals={"instance_avl_tree": instance_avl_tree, "search_word": search_word},
                                         number=1000)
    print("Search time (SkipList):", skip_list_search_time)
    print("Search time (AVLTree):", avl_tree_search_time)

    # Measure deletion time
    skip_list_delete_time = timeit.timeit(stmt="instance_skip_list.skip_list_delete(delete_word)",
                                          globals={"instance_skip_list": instance_skip_list,
                                                   "delete_word": delete_word},
                                          number=1000)
    avl_tree_delete_time = timeit.timeit(stmt="instance_avl_tree.avl_tree_delete(instance_avl_tree.root, delete_word)",
                                         globals={"instance_avl_tree": instance_avl_tree, "delete_word": delete_word},
                                         number=1000)
    print("Deletion time (SkipList):", skip_list_delete_time)
    print("Deletion time (AVLTree):", avl_tree_delete_time)
