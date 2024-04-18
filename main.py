import time
import os
import random


print("Welcome to Community AI! This AI needs your Questions and Answers that we should add to the AI.")
print("If your question is not here, you can add it trough our Discord.")
time.sleep(2)

def generating():
    print("The answer is generating... Please wait.")
    time.sleep(2)

question = input("Your Question: ")

if question == "Hello!":
        generating()
        x = random.randint(1,2)
        if x == int("1"):
            print("Hello, I am Community AI! How can I help You?")
        if x == int("2"):
            print("Hi! How Can I help you?")
if question == "Hi!":
      generating()
      x = random.randint(1,2)
      if x == int("1"):
        print("Hi! I'm Community AI! How Can I help you?")
      if x == int("2"):
        print("Hello! How Can I help?")
if question == "What's your name?":
        generating()
        x = random.randint(1,2)
        if x == int("1"):
            print("Thanks for your question. My name is Community AI because my Questions and Answers are fully controlled by our Community.")
        if x == int("2"):
            print("My name is Community AI.")