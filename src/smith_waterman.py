# Python implementation of Smith-Waterman Algorithm
# This was originally implemented by alevchuk 2011-04-10 in python2.x
# This implmentation is on python 3.8.3 with an object-oriented approach

class Smithwaterman():
    def __init__(self, match_award=10, mismatch_penalty=1, gap_penalty=0):
        """Contructor for smith waterman implementation with opening parameters

        Args:
            match_award (int, optional): Points given when the letters match. Defaults to 10.
            mismatch_penalty (int, optional): Points deducted when there is a mis match. Defaults to 1.
            gap_penalty (int, optional): The penalty when there is no chars left in one of the strings. Defaults to 0.
        """
        self._match_award = match_award
        self._mismatch_penalty = mismatch_penalty
        self._gap_penalty = gap_penalty

    # Zeros() function is taken from NumPy
    def _zeros(self, shape):
        """Generate matrix shaped x*y (shape[0] * shape[1]) filled with zeros"""
        return [[0] * shape[1] for _ in range(shape[0])]

    def _match_score(self, alpha, beta):
        """Score for 2 letters based on their comparison"""
        if alpha == beta:
            return self._match_award
        elif alpha is None or beta is None:
            return self._gap_penalty
        else:
            return self._mismatch_penalty

    def _finalize(self, align1, align2):
        # reverse the alignments as they are in reverse order when tracing back
        align1.reverse()
        align2.reverse()

        i, j = 0, 0

        # Calculate identity, score, and aligned sequences
        symbol = ''
        found = 0
        score = 0
        identity = 0
        for i in range(0, len(align1)):
            # if two AAs are the same, then output the letter
            if align1[i] == align2[i]:
                symbol = symbol + align1[i]
                identity = identity + 1
                score += self._match_score(align1[i], align2[i])

            # if they are not identical and none of them is gap
            elif align1[i] != align2[i] and align1[i] is not None and align2[i] is not None:
                score += self._match_score(align1[i], align2[i])
                symbol += ' '
                found = 0

            # if one of them is a gap, output a space
            elif align1[i] is None or align2[i] is None:
                symbol += ' '
                score += self._gap_penalty

        identity = float(identity) / len(align1) * 100

        return align1, align2

    def water(self, seq1, seq2):
        m, n = len(seq1), len(seq2)

        # Generate the dp and traceback pointer
        score = self._zeros((m+1, n+1))
        pointer = self._zeros((m+1, n+1))

        max_score = 0  # Record the max score obtained through DP

        # Build up the DP for sequence score and tracing
        for i in range(1, m+1):
            for j in range(1, n+1):

                # Take the max score from left, up and upper-left diagonal
                score_up = score[i][j-1] + self._gap_penalty
                score_left = score[i-1][j] + self._gap_penalty
                score_diagonal = score[i-1][j-1] + \
                    self._match_score(seq1[i-1], seq2[j-1])

                # for this indices
                score[i][j] = max(0, score_up, score_left, score_diagonal)

                # assign traceback pointers for constructing the sequence back
                if score[i][j] == 0:
                    pointer[i][j] = 0  # End of path
                if score[i][j] == score_left:
                    pointer[i][j] = 1  # trace up, we need to go up
                if score[i][j] == score_up:
                    pointer[i][j] = 2  # trace left, we need to go left
                if score[i][j] == score_diagonal:
                    # trace diagonal, we need to go upper-left
                    pointer[i][j] = 3
                if score[i][j] >= max_score:
                    max_i = i
                    max_j = j
                    max_score = score[i][j]

        align1 = []
        align2 = []

        i, j = max_i, max_j  # Starting point, will start from max score to form best cluster

        # Traceback and make alignment -> follow traceback pointers
        while pointer[i][j] != 0:  # as long as we have path
            if pointer[i][j] == 3:  # trace diagonal
                align1.append(seq1[i-1])
                align2.append(seq2[j-1])
                i -= 1
                j -= 1

            elif pointer[i][j] == 2:  # trace left
                align1.append(None)
                align2.append(seq2[j-1])
                j -= 1

            elif pointer[i][j] == 1:  # trace up
                align1.append(seq1[i-1])
                align2.append(None)
                i -= 1

        return self._finalize(align1, align2)
