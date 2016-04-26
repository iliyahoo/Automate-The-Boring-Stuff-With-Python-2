#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

pupils = 35

# Generate 35 quiz files.
for quizNum in range(pupils):
  # TODO: Create the quiz and answer key files.
  quizFile = open("capitalsQuiz/capitalsQuiz%d" % (quizNum + 1), "w")
  answerKeyFile = open("capitalsQuiz/capitalsQuiz_answers%d" % (quizNum + 1), "w")

  # TODO: Write out the header for the quiz.
  quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
  title = "State Capitals Quiz (Form %s)\n\n" % (quizNum + 1)
  quizFile.write(" " * 20 + title)

  # TODO: Shuffle the order of the states.
  states = list(capitals.keys())
  random.shuffle(states)

  # TODO: Loop through all 50 states, making a question for each.
  for questionNum in range(len(capitals)):
    state = states[questionNum]
    correctAnswer = capitals[state]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = [correctAnswer] + wrongAnswers
    random.shuffle(answerOptions)

    quizFile.write("%d. What is the capital of %s?\n" % (questionNum + 1, state))
    for i in range(len(answerOptions)):
      quizFile.write("    %s. %s\n" % ("ABCD"[i], answerOptions[i]))
    quizFile.write("\n")

    answerKeyFile.write("%d. %s\n" % (questionNum + 1, "ABCD"[answerOptions.index(correctAnswer)].rjust(4 - len(str(questionNum + 1)))))

  quizFile.close()
  answerKeyFile.close()
