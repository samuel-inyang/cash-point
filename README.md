# Cash point

A menu-driven cash machine written in Python. It keeps your balance in a file,
so the money you take out is still gone the next time you run it.

## The story behind it

I made this during my T Level in Digital Software Development, when I was
learning how Python reads and writes files. A cash machine was a good way to
practise: every transaction has to read the balance, change it, and save it
again.

Since then I have been adding to it bit by bit. Each time I came back to it I
fixed something I had learned more about:

## What it currently does 

1. **Mobile top-up:** takes the amount off your balance
2. **Cash withdrawal:** refuses anything over your balance
3. **Balance check**
4. **Order a statement** by email or post
5. **Change PIN:** checks your current PIN first, and only accepts a new
   4-digit one
6. **Quit**

The first time you run it, it opens an account with £5,000 and pin set to "1234".

## Running it

```bash
python3 scripts/cash_point.py
```

It only uses the Python standard library, so there is nothing to install.

## How it works

- The balance is stored in `balance.txt` and read and written on every
  transaction, which is why it is remembered between runs. If the file does not
  exist yet, the program creates it instead of crashing.
- Each option is its own function, so a new one can be added without touching
  the others.
- Amounts are checked twice: `try` and `except ValueError` catch anything that
  is not a number, and a range check refuses amounts that are zero, negative or
  more than the balance.

## What I would add next

- Ask for the PIN before showing the menu. At the moment the PIN is only used
  when changing it.
- Save the PIN to a file like the balance, so a changed PIN is still there next
  time.

*Thanks for reading. Spend wisely.*
