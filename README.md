TODO:

make the waves continuous between frequency changes:
Use a midi libarary to generate sounds

Scratch ideas:

Lowest note: 
110 * 2 ^ (-5/12) = 82.4068892282

Highest note:
880 * 2 ^ (5/12) = 1174.65907167
110 * 2^ (41/12)

Middlest note: (-5, ..., 0, 41) means 47 different frequncies on the guitar, so take the middle one.
110 * 2 ^ (23/12) ~= 110 * 2 ^2 = 440

Strings:
Low E: E3
A: A3
D: D4
G: G4
B: B4
High E: E5

Use this to do fretboard_to_freq and freq_to_fretboard:

pseudo, string num ~> maps to frequncy multy by 2 ^ (fretnum/12)

generate a frequency band per string, like from base string freq to base string freq * 2 ^(total_frets/12)

then figure out which bands it exists withing and then interate in them and put the matching ones.
