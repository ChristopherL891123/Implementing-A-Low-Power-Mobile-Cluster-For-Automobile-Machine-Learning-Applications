# code from https://www.youtube.com/watch?v=QEaBAZQCtwE&ab_channel=AssemblyAI
# more info on transformers on https://www.youtube.com/watch?v=SZorAJ4I-sA&ab_channel=GoogleCloudTech
from transformers import pipeline
# import tensorflow

transformer_pipeline = pipeline('question-answering')
question = "What is the main action?"
corpus = """ Hamlet
by William Shakespeare
Edited by Barbara A. Mowat and Paul Werstine
  with Michael Poston and Rebecca Niles
Folger Shakespeare Library
https://shakespeare.folger.edu/shakespeares-works/hamlet/
Created on Jul 31, 2015, from FDT version 0.9.2
Characters in the Play
======================
THE GHOST
HAMLET, Prince of Denmark, son of the late King Hamlet and Queen Gertrude
QUEEN GERTRUDE, widow of King Hamlet, now married to Claudius
KING CLAUDIUS, brother to the late King Hamlet
OPHELIA
LAERTES, her brother
POLONIUS, father of Ophelia and Laertes, councillor to King Claudius
REYNALDO, servant to Polonius
HORATIO, Hamlet's friend and confidant
Courtiers at the Danish court:
  VOLTEMAND
  CORNELIUS
  ROSENCRANTZ
  GUILDENSTERN
  OSRIC
  Gentlemen
  A Lord
Danish soldiers:
  FRANCISCO
  BARNARDO
  MARCELLUS
FORTINBRAS, Prince of Norway
A Captain in Fortinbras's army
Ambassadors to Denmark from England
Players who take the roles of Prologue, Player King, Player Queen, and Lucianus in <title>The Murder of Gonzago</title>
Two Messengers
Sailors
Gravedigger
Gravedigger's companion
Doctor of Divinity
Attendants, Lords, Guards, Musicians, Laertes's Followers, Soldiers, Officers

 """

import click


@click.command()
def question():
    user_input = click.prompt('What is your question', type=str)
    response = get_response(user_input)
    click.echo(response)


# This is where I put the code that Christopher is working on to generate the response.
def get_response(user_input):
    try:
        answer = transformer_pipeline(question=user_input, context=corpus)
        return f"You asked: {user_input}.\n The answer is: {answer['answer']}. \n The confidence score of this answer is: {answer['score']}."
    except:
        return "Sorry, I could not find an answer to your question."


if __name__ == '__main__':
    question()

