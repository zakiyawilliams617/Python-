class LFSR:
    # create an LFSR with initial state "seed" and tap "tap"\
    def __init__(self, seed: str, tap: int):
        self.state = seed
        self.tap = tap

    # return the bit at index "i"
    def bit(self, i: int):
        return int(self.state[i])

    # execute one LFSR iteration and return new (rightmost) bit as an int
    def step(self):
        # XDR the leftmost bit (index 0) with the bit at the tap position
        # bits are numbered right to left, tap position from right
        # index from left (N - self.tap)
        N = len(self.state)
        left_bit = int(self.state[0])
        # tap is 1 - indexed from the right, tap position is string index = N - tap
        tap_index = N - self.tap
        tap_bit = int(self.state[tap_index])
        new_bit = left_bit ^ tap_bit

        # shift left, drop leftmost bbit, append new_bit on the right
        self.state = self.state[1:] + str(new_bit)

        return new_bit

    # return string representation of the LFSR
    def __str__(self):
        return self.state

# invokes LFSR


def main():
    seeds_and_taps = [
        ('0110100111', 2),
        ('0100110010', 8),
        ('1001011101', 5),
        ('0001001100', 1),
        ('1010011101', 7),
    ]

    for seed, tap in seeds_and_taps:
        lfsr = LFSR(seed, tap)
        new_bit = lfsr.step()
        print(str(lfsr) + ' ' + str(new_bit))


if __name__ == '__main__':
    main()
