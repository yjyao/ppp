One classic method for composing secret messages is called a square code. The
spaces are removed from the English text and the characters are written into a
square (or rectangle). For example, the sentence "If man was meant to stay on
the ground god would have given us roots" is 54 characters long, so it is
written into a rectangle with 7 rows and 8 columns.

```
ifmanwas
meanttos
tayonthe
groundgo
dwouldha
vegivenu
sroots
```

The coded message is obtained by reading down the columns going left to right.
For example, the message above is coded as:

```
imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
```

In your program, have the user enter a message in English with no spaces
between the words. Have the maximum message length be 81 characters. Display
the encoded message. (Watch out that no "garbage" characters are printed.)
Here are some more examples:

- Input

  ```
  haveaniceday
  feedthedog
  chillout
  ```

- Output

  ```
  hae and via ecy fto ehg ee dd clu hlt io
  ```
