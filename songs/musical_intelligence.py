import random
from math import ceil
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

#class ChordPlayer:

class Drummer:
    def __init__(self, beat_length):
        self.beat = {}
        self.beat_length = beat_length
        self.EIGHT_BEATS_OF_JAZZ_RIDE = {
                0: [("Ride Cymbal 1", 1, 100)], 
                1: [("Ride Cymbal 1", 2/3, 100)], 
                1 + 2/3: [("Ride Cymbal 1", 1/3, 80)],
                1 + 2/3 + 1/3: [("Ride Cymbal 1", 1,90)], 
                1 + 2/3 + 1/3 + 1 : [("Ride Cymbal 1", 2/3, 100)], 
                1 + 2/3 + 1/3 + 1 + 2/3:  [("Ride Cymbal 1", 1/3, 100)],
                4 + 0: [("Ride Cymbal 1", 1, 100)], 
                4 + 1: [("Ride Cymbal 1", 2/3, 100)], 
                4 + 1 + 2/3: [("Ride Cymbal 1", 1/3, 80)],
                4 + 1 + 2/3 + 1/3: [("Ride Cymbal 1", 1,90)], 
                4 + 1 + 2/3 + 1/3 + 1 : [("Ride Cymbal 1", 2/3, 100)], 
                4 + 1 + 2/3 + 1/3 + 1 + 2/3:  [("Ride Cymbal 1", 1/3, 100)]
                }
        self.EIGHT_BEATS_OF_1_3_BD = {
                0: [("Acoustic Bass Drum", 1, 100)],
                2: [("Acoustic Bass Drum", 1, 80)],
                4 + 0: [("Acoustic Bass Drum", 1, 90)],
                4 + 2: [("Acoustic Bass Drum", 1, 100)]
                }

        self.EIGHT_BEATS_OF_2_4_HH = {
                1: [("Pedal Hi-hat", 1, 100)],
                3: [("Pedal Hi-hat", 1, 80)],
                4 + 1: [("Pedal Hi-hat", 1, 90)],
                4 + 3: [("Pedal Hi-hat", 1, 100)]
                }

    def create_snare_pattern(self):
        snare_pattern = [x/3 for x in random_partition_with_choices_differing_length(self.beat_length * 3, [2, 4, 6, 8, 10, 12])]
        time_stamp = 0
        for duration in snare_pattern:
            if time_stamp not in self.beat:
                self.beat[time_stamp] = []
            velocity = random.randint(80, 127)
            self.beat[time_stamp].append(("Acoustic Snare", duration, velocity))
            time_stamp += duration

    def create_custom_pattern(self, pat):
        # this is to be removed
        time_stamp = 0
        for b in pat:
            if time_stamp not in self.beat:
                self.beat[time_stamp] = []
            self.beat[time_stamp].append(b)
            time_stamp += b[1]

    def play_for_whole_song(self, song_length):
        # song length measured in beats
        beat_repeats = ceil(song_length/self.beat_length)
        # So that we don't clobber existing beat
        beat_copy = self.beat.copy()
        for i in range(1, beat_repeats + 1):
            for k, v in beat_copy.items():
                if k + i * self.beat_length not in self.beat:
                    self.beat[k + i * self.beat_length] = []
                # coping it over
                for event in v:
                    self.beat[k + i * self.beat_length].append(event)

    def merge_in_more_rhythm(self, new_beat):
        for k, v in new_beat.items():
            if k not in self.beat:
                self.beat[k] = []
            for event in v:
                self.beat[k].append(event)

    def create_jazz_groove(self, duration):
        self.merge_in_more_rhythm(self.EIGHT_BEATS_OF_JAZZ_RIDE)
        self.merge_in_more_rhythm(self.EIGHT_BEATS_OF_1_3_BD)
        self.merge_in_more_rhythm(self.EIGHT_BEATS_OF_2_4_HH)
        self.create_snare_pattern()
        self.play_for_whole_song(duration)
