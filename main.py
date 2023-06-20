import park, pool, Scientist, soccer

import random

if __name__ == "__main__":
  madlib_choices = [park, pool, Scientist, soccer]
  madlib_function = random.choice(madlib_choices)
  madlib_function.madlib()

print()