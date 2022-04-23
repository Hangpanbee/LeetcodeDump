class Codec:
    def __init__(self):
        self.prefix = "http://tinyurl.com/"
        self.map = dict()

    def _hash(self, s):
        BASE, MOD = 13331, 1e9 + 7
        res = 0
        for c in s:
            res = (res * BASE + ord(c)) % MOD
        return res
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = str(self._hash(longUrl))
        self.map[key] = longUrl
        return self.prefix + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.map[shortUrl.split("/")[-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))