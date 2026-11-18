def sma(values, window: int):
    return [sum(values[i:i+window]) / window for i in range(len(values) - window + 1)]

if __name__ == "__main__":
    print(sma([10, 12, 14, 16, 18], 3))
