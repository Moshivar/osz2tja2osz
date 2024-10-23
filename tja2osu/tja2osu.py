# $Id$
import sys
import copy

# jiro data
TITLE = "NO TITLE"
SUBTITLE = "NO SUBTITLE"
BPM = 0.0
WAVE = "NO WAVE FILE"
OFFSET = 0.0
DEMOSTART = 0.0
COURSE = "Oni"

# osu data
AudioFilename = ""
Title = ""
Source = ""
Tags = "taiko jiro tja"
Artist = "unknown"
Creator = "unknown"
Version = "Oni"
AudioLeadIn = 2000
CountDown = 0
SampleSet = "Normal"
StackLeniency = 0.7
Mode = 1
LetterboxInBreaks = 1
PreviewTime = 0.0
TimingPoints = []
HitObjects = []
HPDrainRate = 3
CircleSize = 5
OverallDifficulty = 3
ApproachRate = 5
SliderMultiplier = 1.4
SliderTickRate = 4
CircleX = 416
CircleY = 176

# const_data
BRANCH = "BRANCH"
END = "END"
START = "START"
BPMCHANGE = "BPMCHANGE"
MEASURE = "MEASURE"
GOGOSTART = "GOGOSTART"
GOGOEND = "GOGOEND"
DELAY = "DELAY"
SCROLL = "SCROLL"

# guess str
def convert_str(str):
    try:
        ret1 = str.decode("gbk").encode("utf-8")
    except:
        ret1 = None

    try:
        ret2 = str.decode("shift-jis").encode("utf-8")
    except:
        ret2 = None

    try:
        ret3 = str.decode("big5").encode("utf-8")
    except:
        ret3 = None    
    
    ret = []
    if ret1: 
        ret.append(ret1)
        print(len(ret1))  # Updated for Python 3
    if ret2: 
        ret.append(ret2)
        print(len(ret2))  # Updated for Python 3
    if ret3: 
        ret.append(ret3)
        print(len(ret3))  # Updated for Python 3
    if not ret:
        return str
    else:
        ans = None
        for ret0 in ret:
            if ans is None or len(ret0) < len(ans):
                ans = ret0
        return ans

# The rest of the code is unchanged, but ensure you update all other print statements to:
# print(value) instead of print value
