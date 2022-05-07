from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb
import random
import pytest

my_range = 5
def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(my_range):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]
    

    # This loop will repeat the statements inside it 4 times.
    for _ in range(my_range):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


        
def test_get_noun():
    # Testing SINGLE NOUN
    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(my_range):
        noun = get_noun(1)
        assert noun in single_noun
    
    # Testing PLURAL NOUN
    plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(my_range):
        noun = get_noun(2)
        assert noun in plural_noun

def test_get_verb():
    # Testing SINGLE PAST verbs
    single_past_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(my_range):
        verb = get_verb(1, "past")
        assert verb in single_past_verb
    
    #Testing SINGLE PRESENT verbs
    single_present_verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(my_range):
        verb = get_verb(1, "present")
        assert verb in single_present_verb 

    #Testing SINGLE FUTURE verbs
    single_future_verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(my_range):
        verb = get_verb(1, "future")
        assert verb in single_future_verb 
    
    # Testing PLURAL PAST verbs
    plural_past_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(my_range):
        verb = get_verb(2, "past")
        assert verb in plural_past_verb

    #Testing PLURAL PRESENT verbs
    plural_present_verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(my_range):
        verb = get_verb(2, "present")
        assert verb in plural_present_verb
    
    #Testing PLURAL FUTURE verbs
    plural_future_verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(my_range):
        verb = get_verb(2, "future")
        assert verb in plural_future_verb 

# Test GETTING PREPOSITIONS
def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(my_range):
        preposition = get_preposition()
        assert preposition in prepositions 

#Test SINGULAR PREPOSITIONAL PHRASES
def test_get_prepositional_phrase():
    singular_prepositional = (f'{get_preposition()} {get_determiner(1)} {get_noun(1)}')
    



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])