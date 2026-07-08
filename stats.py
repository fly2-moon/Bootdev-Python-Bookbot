def open_book(book:str) -> str:
    with open(book) as b:
        return b.read()

def get_num_words(contents:str) -> int:
    return len(contents.split())

def count_characters(contents:str) -> dict[chr, int]:
    ch_cnt:dict[chr,int] = {}
    for ch in contents.lower():
        # increase count if character already seen
        if ch in ch_cnt: 
            ch_cnt[ch] += 1 
        # ensure all characters counted
        else:
            ch_cnt[ch] = 1
    return ch_cnt

def sort_on(target:tuple[int, chr]) -> int:
    return target[0]

def chars_dict_to_sorted_list(ch_cnt:dict) -> list[tuple[int, chr]]:
    chars:list[tuple[int, chr]] = []
    for ch, cnt in ch_cnt.items():
        chars.append((cnt, ch))
    return sorted(chars, reverse=True, key=sort_on)

