def get_input_sequence():
    try:
        sequence = list(map(int, input().split()))
        if len(sequence) == 0:
            raise ValueError("L")
        if len(sequence) > 2000:
            raise ValueError("LL")
        return sequence
    except ValueError as e:
        print("Error:", e)
        return None

def find_interval_sums(sequence):
    interval_sums = {}
    n = len(sequence)
    for i in range(n):
        interval_sum = 0
        for j in range(i, n):
            interval_sum += sequence[j]
            if j > i:
                interval_sums[interval_sum] = interval_sums.get(interval_sum, 0) + 1
    return interval_sums

def count_same_sums_pairs(interval_sums):
    pairs_count = 0
    for count in interval_sums.values():
        pairs_count += count * (count - 1) // 2
    return pairs_count

def main():
    print("Zadej cisla")
    sequence = get_input_sequence()
    if sequence is None:
        return
    
    interval_sums = find_interval_sums(sequence)
    pairs_count = count_same_sums_pairs(interval_sums)
    
    print("Počet dvojic intervalů se stejným součtem:", pairs_count)

if __name__ == "__main__":
    main()
