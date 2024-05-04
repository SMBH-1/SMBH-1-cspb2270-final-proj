from skip_list import SkipList
from avl_tree import AVLTree
from performance_comparison import run_performance_comparison, generate_random_words_list


def main():
    instance_skip_list = SkipList()
    instance_avl_tree = AVLTree()
    new_words_list = generate_random_words_list(100)
    run_performance_comparison(instance_skip_list, instance_avl_tree, new_words_list)


if __name__ == "__main__":
    main()
