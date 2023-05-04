from transformers import pipeline # transformers by HuggingFace
import threading as t

# set up a question answering pre-built and pre-trained model
transformer_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad',
                                tokenizer='distilbert-base-cased')
# multithreaded code
def question():
    user_input1 = input('Is your question Theological or Shakespearean?')
    thread1 = t.Thread(target=get_response, args=[user_input1])
    user_input2 = input('Is your question Theological or Shakespearean?')
    thread2 = t.Thread(target=get_response, args=[user_input2])
    user_input3 = input('Is your question Theological or Shakespearean?')
    thread3 = t.Thread(target=get_response, args=[user_input3])
    user_input4 = input('Is your question Theological or Shakespearean?')
    thread4 = t.Thread(target=get_response, args=[user_input4])
    user_input5 = input('Is your question Theological or Shakespearean?')
    thread5 = t.Thread(target=get_response, args=[user_input5])

def get_response(Topic_user_input):
    while True:
        try:
            question_input = input("Please enter your question: ")

            if Topic_user_input.upper() == "THEOLOGICAL":
                with open("Theological_Knowledge_Base.txt",'r', encoding='utf-8') as TheologicalKnowledgeBase:
                    KnowledgeBase = TheologicalKnowledgeBase.read()
                    answer = transformer_pipeline(question=question_input, context=KnowledgeBase)
                    print( f"You asked in the context of {Topic_user_input}.",
                           f" The question is: {question_input} \n The answer is: {answer['answer']}.",
                           f" \n The confidence score of this answer is: {answer['score']}.",sep="\n")

            elif Topic_user_input.upper() == "SHAKESPEAREAN":
                with open("Shakespearean_Knowledge_Base.txt", 'r', encoding='utf-8') as ShakespeareanKnowledgeBase:
                    KnowledgeBase = ShakespeareanKnowledgeBase.read()
                    answer = transformer_pipeline(question=question_input, context=KnowledgeBase)
                    print( f"You asked in the context of {Topic_user_input}.",
                           f" The question is: {question_input} \n The answer is: {answer['answer']}. ",
                           f"\n The confidence score of this answer is: {answer['score']}.", sep="\n")

            else: print("Please choose a correct option.")

        except:
            import traceback as t
            t.print_exc()
            return "Sorry, I could not find an answer to your question."

# run the code
question()

