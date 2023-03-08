import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
headers = {
    'accept': 'application/json',
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters, headers= headers)
question_data = response.json()["results"]

# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
#              "you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, "
#              "you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# question_data2 = [
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Gumbo is a stew that originated in Louisiana.", "correct_answer": "True",
#      "incorrect_answers": ["False"]},
#     {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
#      "question": "Undertale is an RPG created by Toby Fox and released in 2015.", "correct_answer": "True",
#      "incorrect_answers": ["False"]}, {"category": "Geography", "type": "boolean", "difficulty": "easy",
#                                        "question": "Alaska is the largest state in the United States.",
#                                        "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
#      "question": "Luigi is taller than Mario?", "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Entertainment: Film", "type": "boolean", "difficulty": "easy",
#      "question": "In the original script of The Matrix,"
#                  " the machines used humans as additional computing power instead of batteries.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
#      "question": "In Sonic Adventure, "
#                  "you are able to transform into Super Sonic at will after completing the main story.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Entertainment: Video Games", "type": "boolean", "difficulty": "easy",
#      "question": "Gordon Freeman, the protagonist of &quot;Half-Life&quot;, is said to have once had a ponytail.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Animals", "type": "boolean", "difficulty": "easy",
#      "question": "The Killer Whale is considered a type of dolphin.", "correct_answer": "True",
#      "incorrect_answers": ["False"]}, {"category": "Entertainment: Television", "type": "boolean", "difficulty": "easy",
#                                        "question": "In Star Trek;, Klingons are aliens.",
#                                        "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Ping-Pong originated in England", "correct_answer": "True", "incorrect_answers": ["False"]}]
