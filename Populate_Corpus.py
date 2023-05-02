import os
import PyPDF2

TheologicalKnowledgeBase = ""
ShakespeareanKnowledgeBase = ""

for Corpus_File in os.listdir("Corpus_Data"):

    if Corpus_File.endswith(".txt"): # it's Shakespeare
        the_File = open("Corpus_Data/"+Corpus_File) # open each file and read it
        ShakespeareanKnowledgeBase += the_File.read()
        the_File.close()

    else:
        PDF = PyPDF2.PdfReader("Corpus_Data/"+Corpus_File)
        # iterate through the PDF and get and extract pages at index
        for Page_num in range(len(PDF.pages)):
            Text = PDF.pages[Page_num].extract_text()
            TheologicalKnowledgeBase += Text


file = open("Theological_Knowledge_Base.txt", 'w', encoding='utf-8')
file.write(TheologicalKnowledgeBase)
file.close()

file2 = open("Shakespearean_Knowledge_Base.txt",'w', encoding='utf-8')
file2.write(ShakespeareanKnowledgeBase)
