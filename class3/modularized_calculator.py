#! /usr/bin/python3

def read_number(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    decimal = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * decimal
      decimal /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def read_plus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def read_minus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def read_mul(line, index):
  token = {'type': 'MUL'}
  return token, index + 1

def read_divide(line, index):
  token = {'type': 'DIVIDE'}
  return token, index + 1

def read_bra(line, index):
  token = {'type': 'BRA'}
  return token, index + 1

def read_ket(line, index):
  token = {'type': 'KET'}
  return token, index + 1


def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = read_number(line, index)
    elif line[index] == '+':
      (token, index) = read_plus(line, index)
    elif line[index] == '-':
      (token, index) = read_minus(line, index)
    elif line[index] == '*':
      (token, index) = read_mul(line, index)
    elif line[index] == '/':
      (token, index) = read_divide(line, index)
    elif line[index] == '(':
      (token, index) = read_bra(line, index)
    elif line[index] == ')':
      (token, index) = read_ket(line, index)
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


def calc_mul_divide(tokens): # calculate '*' and '/'
  index = 1
  while index < len(tokens):
    if tokens[index]['type'] == 'MUL':
      if tokens[index - 1]['type'] == 'NUMBER' and tokens[index + 1]['type'] == 'NUMBER':
        tokens[index - 1]['number'] *= tokens[index + 1]['number']
        del tokens[index] # delete '*'
        del tokens[index] # delete next number(tokens[index + 1])
      else:
        print('Invalid syntax')
        exit(1)
    elif tokens[index]['type'] == 'DIVIDE':
      if tokens[index - 1]['type'] == 'NUMBER' and tokens[index + 1]['type'] == 'NUMBER':
        tokens[index - 1]['number'] /= tokens[index + 1]['number']
        del tokens[index] # delete '/'
        del tokens[index] # delete next number(tokens[index + 1])
      else:
        print('Invalid syntax')
        exit(1)
    else:
      index += 1

def process_braket(tokens):
  index = 0
  inside_braket = []
  flag_bra = 0
  no_braket_tokens = []
  while index < len(tokens):
    if tokens[index]['type'] == 'BRA':
      index += 1
      flag_bra += 1
      while tokens[index]['type'] != 'KET':
        inside_braket.append(tokens[index])
        index += 1
      ans_in_bra = evaluate(inside_braket)
      tmp = 0
      ans_token, hoge = read_number(str(ans_in_bra), tmp)
      no_braket_tokens.append(ans_token)
      index += 1
      flag_bra -= 1

    else:
      no_braket_tokens.append(tokens[index])
      index += 1
  
  return no_braket_tokens
    
def evaluate(tokens):
  answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  tokens = process_braket(tokens)
  calc_mul_divide(tokens)
  index = 1
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        answer += tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
        answer -= tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  return answer


def test(line):
  tokens = tokenize(line)
  actual_answer = evaluate(tokens)
  expected_answer = eval(line)
  if abs(actual_answer - expected_answer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expected_answer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
  print("==== Test started! ====")
  test("1+2")
  test("1.0+2.1-3")
  test("2*3")
  test("2.0*3")
  test("1+2.0*3.2")
  test("3/2")
  test("1+3/2-0.5")
  test("2*3*4/5/6")
  test("3.0+4*2-1/5")
  test("(1+2)")
  test("3*(1+2)")
  test("3.0/(2.0+1)")
  # test("3*(1+1)+4/(3-1)") # :(
  # test("(3+4*(3-2))/5") # :(
  print("==== Test finished! ====\n")

run_test()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
