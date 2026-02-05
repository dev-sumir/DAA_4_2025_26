import heapq

class Node:
    def __init__(self, ch, f):
        self.ch = ch
        self.f = f
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.f < other.f


def make_codes(root, cur, codes):
    if root is None:
        return

    if root.left is None and root.right is None:
        codes[root.ch] = cur
        return

    make_codes(root.left, cur + "0", codes)
    make_codes(root.right, cur + "1", codes)


def decode_text(root, bits):
    out = ""
    cur = root

    for b in bits:
        if b == '0':
            cur = cur.left
        else:
            cur = cur.right

        if cur.left is None and cur.right is None:
            out += cur.ch
            cur = root

    return out


def huffman(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    heap = []
    for ch in freq:
        heapq.heappush(heap, Node(ch, freq[ch]))

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)

        parent = Node('#', n1.f + n2.f)
        parent.left = n1
        parent.right = n2

        heapq.heappush(heap, parent)

    root = heap[0]

    codes = {}
    make_codes(root, "", codes)

    encoded = ""
    for ch in text:
        encoded += codes[ch]

    decoded = decode_text(root, encoded)

    return encoded, decoded, codes


text = input("Enter string: ")

enc, dec, codes = huffman(text)

print("\nCodes:")
for ch in codes:
    print(ch, ":", codes[ch])

print("\nEncoded:", enc)
print("Decoded:", dec)
