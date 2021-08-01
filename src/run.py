import sys
from smith_waterman import Smithwaterman
from pattern_generator import PatternGenerator

a, b = Smithwaterman().water("Apr 21, 2021 5:01:33 PM com.nirima.jenkins.plugins.docker.DockerContainerWatchdog loadNodeMap", 
"Apr 21, 2021 5:06:33 PM com.nirima.jenkins.plugins.docker.DockerContainerWatchdog execute")

print(''.join(PatternGenerator().create_pattern(a, b)))

# print(''.join(a))
# print(''.join(b))