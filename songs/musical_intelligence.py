import random
# Aka a drummer (lol)
def random_partition_with_choices_differing_length(n, choices):
    # assuming the choices will always give rise to a paritition
    # a bad input would be n = 10 and choices = [3]
    # a good input would be n = 10 and choices = [2,3]
    partition = []
    while sum(partition) !=  n:
        x = random.choice(choices)
        # Keep trying ones until it's a valid choice
        while x + sum(partition) > n:
            x = random.choice(choices)
        partition.append(x)
    return partition

