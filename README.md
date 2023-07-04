# QuBu
The qubu is an open source project that is created to help people 
especially teachers to make n choice questions with t answers faster
and quicly. The idea comes from the situation when you have a lot of questions that 
they all look to have the same pattern. Like these questions.

1-What is the simplified polynomial of the following polynomial?
5*x+3+7*x+5+23

2-What is the simplified polynomial of the following polynomial?
90*x+3+7*x+5+2

or 

1-how to say hello word in german?

2-how to say good word in german?

3-how to say hello word in Farsi?

...

they all look the same right?
the only different is this that some words and some numbers and
symbols are different, however the pattern, concept and the solution
of all of them is the same.

Now this is a little project named QuBu that will help you to generate
such questions.

# installation:

for installing the project you can simply use pip and your cmd:

```cmd
# for Uix/MacOS
python3 -m pip install QuBuilders

# for windows
py -m pip install QuBuilders
```

# How to use

## NchTan
### QuestionDataSaver
to use this project first let's go to talk about how to make 
a simple question:

For making a question you can simply use QuestionDataSaver class to save 
your questions and manage them in an appropriate way. to save your question 
you can do like the following code:

``` python
from QuBuilders.NchTan import QuestionDataSaver

newquestion = QuestionDataSaver(question_title = "what is hello in french?",
                                answers = ['bonjour'],
                                choices = ["bonjour", "hello", "et"],
                                hints = "hello is for greeting :)",
                                descriptions = "checking your general vocab")
```

#### notes: note that the two last arguments are optional, and you can just ignore them

this class have a method named shuffle_choices that you can use it to shuffle
the choices you have each time.

``` python 
newquestion.shuffle_choices()
```

### QuSeq

in most times you will have a lot of questions, and it is a good thing
to gather them in one object to use them with more options.

``` python
from QuBuilders.NchTan import QuestionDataSaver, QuSeq

newquestion_1 = QuestionDataSaver(question_title = "what is hello in french?",
                                answers = ['bonjour'],
                                choices = ["bonjour", "hello", "et"],
                                hints = "hello is for greeting :)",
                                descriptions = "checking your general vocab")

newquestion_2 = QuestionDataSaver(question_title = "what is hello in french?",
                                answers = ['bonjour'],
                                choices = ["bonjour", "hello", "et"],
                                hints = "hello is for greeting :)",
                                descriptions = "checking your general vocab")


# name_quseq and descriptions_quseq are optional
newquseq = QuSeq(name_quseq = "french vocab", descriptions_quseq = """holding all
                 the french vocab questions :)""")

newquseq += newquestion_1
newquseq += newquestion_2
```

here we added each item using += operators. you get each a specific question
by index and [] operator, Also you can get the length of the quseq.

``` python
print(len(newquseq))
print(newquseq[0])
print(newquseq[1])
```

## quwriters

the QuWriters helps you to write your questions in json files or a csv 
file and save them.

### 



