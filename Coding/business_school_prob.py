import math
# math.lcm()
# The logic for this was basically that the amount of times the smallest multiple has appeared (index count) by the time it encounters the other letter, is the other letter's multiple factor. And vice versa. Idk if its correct, didn't exhaustively test by any means but it seems to work for the examples given.

def index_collector(letters: list) -> dict:
    """Takes in a list of letters which correspond to their respective multiples from a chain of numbers (unseen).
    Returns a dictionary with each of the letters and their corresponding index numbers."""
    index_tracker = {}
    lowest_common_multiple_index_tracker = {}

    for i, letter in enumerate(letters):
        if len(list(letter)) > 1:
            if letter not in lowest_common_multiple_index_tracker.keys():
                lowest_common_multiple_index_tracker[letter] = [i]

            for letter in list(letter):
                if letter not in index_tracker.keys():
                    index_tracker[letter] = [i]
                else:
                    index_tracker[letter].append(i)
 
        else:
            if letter not in index_tracker.keys():
                index_tracker[letter] = [i]
            else:
                index_tracker[letter].append(i)

    print("\nindex_tracker:", index_tracker)

    # The first index numbers which 2 letters have in common is their lowest common multiple
    print("lowest_common_multiple_index_tracker:", lowest_common_multiple_index_tracker)
    
    return index_tracker, lowest_common_multiple_index_tracker


def solve_for_multiples(index_dict: dict, lowest_common_multiple_index_tracker: dict) -> dict:
    """Takes in a dict of letter & their corresponding index appearances and derives their multiples based on ratios of appearance to the other letters."""
    
    letter_multiples = {}

    # from the letter with the largest multiple (last appearing letter in the original index series):
        # the length of this letters index series when it first encounters the smallest letter = the smallest letter's multiple
        # the length of the smallest letters index series when it first encounters the largest letter = the largest letter's multiple
            
    smallest_multiple_letter = max(index_dict, key=lambda k: len(index_dict[k]))
    print("\nsmallest_multiple_letter:", smallest_multiple_letter)

    # How to get the latest appearing key in a dictionary? Below isn't reliable as dictionary insertion order does not ecplicity require the "largest" added last.
    largest_multiple_letter = list(index_dict.keys())[-1]
    print("\nlargest_multiple_letter:", largest_multiple_letter)

    key_to_access = smallest_multiple_letter + largest_multiple_letter
    if key_to_access in lowest_common_multiple_index_tracker:
        common_multiple_index = lowest_common_multiple_index_tracker[key_to_access][0]

    # print("\n type(max_min_collision_index):", type(max_min_collision_index))

    number_of_smallest_multiple_appearances_before_collision = len([index for index in index_dict[smallest_multiple_letter] if index <= common_multiple_index]) 
    letter_multiples[largest_multiple_letter] = number_of_smallest_multiple_appearances_before_collision

    number_of_largestt_multiple_appearances_before_collision = len([index for index in index_dict[largest_multiple_letter] if index <= common_multiple_index])
    letter_multiples[smallest_multiple_letter] = number_of_largestt_multiple_appearances_before_collision

    # How to generalise to all the letters encountered?
    # Cba to work it out without a pen, ask Sam and Charlie for help. Maybe below is correct?
    if len(index_dict.keys()) > 2:
        for letter in index_dict.keys():
            if letter not in [smallest_multiple_letter, largest_multiple_letter]:
                common_multiple_index = lowest_common_multiple_index_tracker[smallest_multiple_letter+letter][0]
                letter_multiples[letter] = len([index for index in index_dict[smallest_multiple_letter] if index <= common_multiple_index])

    return letter_multiples


def main():
    example_list_1 = ['a','b','a','ab']
    ans_1 = {'a':2, 'b': 3}
    example_list_2= ['a','ab','c','a','ab','ac']
    ans_2 = {'a':2, 'b':4, 'c': 5}
    example_list_3= ['a','b','c','a','b','a','c','ab','ac']
    ans_3 = {'a':3, 'b':4, 'c': 5}

    for example_list, ans in [(example_list_1, ans_1), (example_list_2, ans_2), (example_list_3, ans_3)]:
        index_tracker, lowest_common_multiple_index_tracker = index_collector(example_list)
        print(f"\nFor example, {example_list}: index_tracker -  {index_tracker} \n lowest common multiple tracker - {lowest_common_multiple_index_tracker}")

        multiples = solve_for_multiples(index_tracker, lowest_common_multiple_index_tracker)
        print(f"\nExpected {ans}, Calculated {multiples}")

if __name__ == "__main__":
    main()