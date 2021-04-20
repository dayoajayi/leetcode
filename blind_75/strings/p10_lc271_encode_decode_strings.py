import random
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(s.replace('|', '||') + ' | ' for s in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        return [t.replace('||', '|') for t in s.split(' | ')[:-1]]
      

# Your Codec object will be instantiated and called as such:
strs = ["hello", "world"]
codec = Codec()
print(codec.decode(codec.encode(strs)))

