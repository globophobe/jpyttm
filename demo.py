from jpyttm import USD, get_historical_ttm

if __name__ == "__main__":
    ttm = get_historical_ttm(USD)
    for quote in ttm:
        print(quote[0], quote[1])
