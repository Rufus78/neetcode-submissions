
class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, encoded_string: str) -> list[str]:
        decoded = []
        i = 0

        while i < len(encoded_string):
            j = i

            while encoded_string[j] != "#":
                j += 1

            length = int(encoded_string[i:j])
            start = j + 1
            end = start + length

            decoded.append(encoded_string[start:end])
            i = end

        return decoded

