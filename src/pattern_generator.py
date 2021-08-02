from .smith_waterman import Smithwaterman

class PatternGenerator():
    def __init__(self, placeholder='---'):
        """Placeholder for similar texts"""
        self._placeholder = placeholder
    
    def create_pattern(self, target, representative):
        if len(target) == 0 and len(representative) == 0:
            return []

        (target, representative) = Smithwaterman().water(target, representative)
        pattern = []

        for i in range(len(target)):
            if target[i] == representative[i]:
                pattern.append(target[i])
            else:
                pattern.append(self._placeholder)
        
        return pattern