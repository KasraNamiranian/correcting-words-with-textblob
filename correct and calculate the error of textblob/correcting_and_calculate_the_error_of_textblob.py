from textblob import TextBlob

# A function that compares two texts and returns 
# the number of matches and differences
def compare(text1, text2):  
    l1 = text1.split()
    l2 = text2.split()
    good = 0
    bad = 0
    for i in range(0, len(l1)):
        if l1[i] != l2[i]:
            bad += 1
        else:
            good += 1
    return (good, bad)

# Helper function to calculate the percentage of misspelled words
def percentageOfBad(x):
    return (x[1] / (x[0] + x[1])) * 100


with open("test.txt", "r") as f1: # test.txt contains the same typo-filled text from the last example 
    t1 = f1.read()

with open("original.txt", "r") as f2: # original.txt contains the text from the actual book 
    t2 = f2.read()

t3 = TextBlob(t1).correct()

mistakesCompOriginal = compare(t1, t2)
originalCompCorrected = compare(t2, t3)
mistakesCompCorrected = compare(t1, t3)

print("Mistakes compared to original ", mistakesCompOriginal)
print("Original compared to corrected ", originalCompCorrected)
print("Mistakes compared to corrected ", mistakesCompCorrected, "\n")

print("Percentage of mistakes in the test: ", percentageOfBad(mistakesCompOriginal), "%")
print("Percentage of mistakes in the corrected: ", percentageOfBad(originalCompCorrected), "%")
print("Percentage of fixed mistakes: ", percentageOfBad(mistakesCompCorrected), "%", "\n")