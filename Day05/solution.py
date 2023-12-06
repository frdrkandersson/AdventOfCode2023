from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    seeds, *mapChunks = f.read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

def part1():
    result = seeds.copy()
    for chunk in mapChunks:
        mappings = []
        for mapping in chunk.splitlines()[1:]: # skip first text-row
            dest, src, length = map(int, mapping.split())
            mappings.append([dest, src, length])

        temp = []

        for seed in result:
            replaced = False
            for dest, src, length in mappings:
                if seed in range(src, src + length):
                    offset = seed - src
                    temp.append(dest + offset)
                    replaced = True
                    break

            if not replaced:
                temp.append(seed)

        result = temp

    return min(result)

def part2():
    seedRanges = []
    for i in range(0, len(seeds), 2):
        start, end = seeds[i], seeds[i] + seeds[i + 1]
        seedRanges.append((start, end))

    for chunk in mapChunks:
        mappings = []
        for mapping in chunk.splitlines()[1:]: # skip first text-row
            dest, src, length = map(int, mapping.split())
            mappings.append([dest, src, length])

        temp = []

        while len(seedRanges) > 0:
            start, end = seedRanges.pop()
            hadOverlaps = False
            for dest, src, length in mappings:
                overlap_start = max(start, src)
                overlap_end = min(end, src + length)
                isOverlaping = overlap_start < overlap_end
                if isOverlaping:
                    hadOverlaps = True
                    if overlap_start > start:
                        seedRanges.append((start, overlap_start)) # if overlap left a part to the left append that range to be processed again
                    if overlap_end < end:
                        seedRanges.append((overlap_end, end)) # if overlap left a part to the right append that range to be processed again

                    offset = dest - src
                    temp.append((overlap_start + offset, overlap_end + offset))
                    break

            if not hadOverlaps:
                temp.append((start, end)) # if no overlap just add the seedrange

        seedRanges = temp

    return min(seedRanges)[0]

print(part1())
print(part2())