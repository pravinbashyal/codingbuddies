### Implement a program that asks user for a series of string and prints 'Palindrome' or 'Not Palindrome' depending on whether it is Palindrome or not. Palindrome are set of strings which reads same regardless of reading it from start to end or end to start. for eg: dad, abba, or this beautiful poem by Dimitri Martin:

```
Dammit I’m mad.
Evil is a deed as I live.
God, am I reviled? I rise, my bed on a sun, I melt.
To be not one man emanating is sad. I piss.
Alas, it is so late. Who stops to help?
Man, it is hot. I’m in it. I tell.
I am not a devil. I level “Mad Dog”.
Ah, say burning is, as a deified gulp,
 In my halo of a mired rum tin.
I erase many men. Oh, to be man, a sin.
Is evil in a clam? In a trap?
No. It is open. On it I was stuck.
Rats peed on hope. Elsewhere dips a web.
Be still if I fill its ebb.
Ew, a spider… eh?
We sleep. Oh no!
Deep, stark cuts saw it in one position.
Part animal, can I live? Sin is a name.
Both, one… my names are in it.
Murder? I’m a fool.
A hymn I plug, deified as a sign in ruby ash.
A Goddam level I lived at.
On mail let it in. I’m it.
Oh, sit in ample hot spots. Oh wet!
A loss it is alas (sip). I’d assign it a name.N
ame not one bottle minus an ode by me:
“Sir, I deliver. I’m a dog”
Evil is a deed as I live.
Dammit I’m mad.
```

###  Implement a vowel shifter that:
  - asks user for a word
  - shifts the vowel to next adjacent vowel a => e, e => i, i => o, o => u, u => a
  - use the function say to call the word by passing it to the function. For eg following code will pronunce the work `Hello`


```python
import os

def say(val):
    os.system('say ' + val)

# your code here

say('Hello')
```
