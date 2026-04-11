#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # dir() modulun içindəki bütün adları siyahı kimi qaytarır
    names = dir(hidden_4)
    # Adları əlifba sırası ilə sıralayırıq
    for name in sorted(names):
        # Yalnız '__' ilə başlamayanları çap edirik
        if not name.startswith("__"):
            print(name)
