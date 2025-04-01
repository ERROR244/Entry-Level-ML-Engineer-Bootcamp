import time

def ft_progress(lst: range) -> None: # type: ignore
    total= len(lst)
    for i, item in enumerate(lst, 1):
        progress = int(50 * i / total)
        bar = f"{'█' * progress}{' ' * (50 - progress)}"
        print(f"\r{int(progress/2.54)}%|{bar}| {i}/{total}", end="", flush=True)
        yield item

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
