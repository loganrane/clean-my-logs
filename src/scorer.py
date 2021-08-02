class Scorer():
    def __init__(self, k1, k2, placeholder='---'):
        self.k1 = k1  # k1 if x = y and both are strings
        self.k2 = k2  # k2 if both are placeholders
        self._placeholder = placeholder

    def score(self, f1, f2):
        """Score the string based on their match"""
        if(isinstance(f1, str) and isinstance(f2, str) and f1 == f2):
            return self.k1
        if(isinstance(f1, str) and isinstance(f2, str) and f1 == self._placeholder and f2 == self._placeholder):
            return self.k2
        return 0

    def distance(self, fields1, fields2):
        """Get distance between two lists of strings"""
        if not(isinstance(fields1, list) and isinstance(fields2, list)):
            raise TypeError('Fields must be a list')

        max_len = max(len(fields1), len(fields2))
        min_len = min(len(fields1), len(fields2))

        total = 0
        for i in range(min_len):
            total += 1.0 * self.score(fields1[i], fields2[i]) / max_len

        return 1 - total
