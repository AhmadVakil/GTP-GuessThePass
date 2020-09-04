# Guess The Password
Guessing all possible passwords that a victim might use inorder to easily remember them.

## Disclaimer
The idea and codes in this project is made for educational purposes. I take no responsibility if you use it for malicious purposes.

## Getting Started

This project can be used to guess all possibilities that a victim might use as password. Beside using dictionary/wordlist for brute force attack, you can append the output of this code to your wordlist to use it against a specific victim that you already know in some ways.

By using this project, still there is no guaranty that your victim use one of the output word as password, BUT probabilities is 50% positive if you know how to use it instead of guessing all possibilities yourself.  

## Where to use this

After running the code you will get a .txt wordlist. You can use this on all brute force attacks, such as, Burp Suite intruder, Instagram attacks, WIFI attackes, etc.

## OS

Works fine on both Windows and Linux.

## Clone

Firstly clone the project

```
git clone https://github.com/AhmadVakil/GTP-GuessThePass.git
```

<img src="https://raw.githubusercontent.com/AhmadVakil/GTP-GuessThePass/master/demonstration/clone.gif">

## Run

```
cd GTP-GuessThePass
python3 GTP.py
```
<img src="https://raw.githubusercontent.com/AhmadVakil/GTP-GuessThePass/master/demonstration/run.gif">

## Create your dictionary

Just answer the questions as you know about the victim. These questions can be edited in the source code, so these are just examples and feel free to modify it for your self.

Remember, the more you add options the more time it takes to produce the dictionary, so keep it short and use KEY words!

<img src="https://raw.githubusercontent.com/AhmadVakil/GTP-GuessThePass/master/demonstration/create-dictionary.gif">

## Now, let's open our dictionary
As you can see 55986 possibilities created. 

<img src="https://raw.githubusercontent.com/AhmadVakil/GTP-GuessThePass/master/demonstration/output.gif">

