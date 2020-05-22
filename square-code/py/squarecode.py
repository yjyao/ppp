from itertools import zip_longest
import click
import math


def encode(msg):
  msg = ''.join(msg.split())  # Strip all whitespaces.
  width = math.ceil(math.sqrt(len(msg)))
  height = len(msg) // width
  square = (msg[i*width:min((i+1)*width, len(msg))]
            for i in range(height))
  return ' '.join(map(''.join, zip_longest(*square, fillvalue='')))


@click.command()
@click.argument('msg', default='')
def main(msg):
  '''Encode MSG to square-code.'''
  if not msg:
    msg = input()
  print(encode(msg))


if __name__ == '__main__':
  main()
