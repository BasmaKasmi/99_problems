def little_boxes(s: str) -> str:
    ascii_count = [0] * 128
    
    for char in s:
        ascii_count[ord(char)] += 1

    sorted_str = ''.join(chr(i) * ascii_count[i] for i in range(128))



