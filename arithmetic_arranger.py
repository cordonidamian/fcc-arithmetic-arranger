# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:12:31 2020

@author: dcordoni
"""

def arithmetic_arranger(problems, show_result=False):

  sep = list()

# Error: Too many problems
  if len(problems) > 5:
    return 'Error: Too many problems.'

# Splitting list
  for i in range(len(problems)):
    sep.append(problems[i].split(" "))

# Error: Operator must be '+' or '-'
  for i in range(len(sep)):
    if (sep[i][1] != '+') and (sep[i][1] != '-'):
        return "Error: Operator must be '+' or '-'."

# Error: Numbers cannot be more than four digits
    elif sep[i][0].isdigit() and sep[i][2].isdigit() == False:
        return 'Error: Numbers must only contain digits.'
               
# Error: Numbers cannot be more than four digits
    elif len(sep[i][0]) > 4 or len(sep[i][2]) > 4:
        return 'Error: Numbers cannot be more than four digits.'


  firstOperand = list()
  sign = list()
  secondOperand = list()
  space = 0
  result = list()

  var_first_line = list()
  var_second_line = list()
  var_dash = list()
  var_result = list()


  for i in range(len(sep)):
      firstOperand.append(sep[i][0])
      sign.append(sep[i][1])
      secondOperand.append(sep[i][2])
      
      if len(firstOperand[i]) > len(secondOperand[i]):
          space = len(firstOperand[i])
      else:
          space = len(secondOperand[i])
          
      if sep[i][1] == '+':
          result.append(int(sep[i][0]) + int(sep[i][2]))
      else:
          result.append(int(sep[i][0]) - int(sep[i][2]))
          
      var_first_line.append(firstOperand[i].rjust(space+2))
      var_second_line.append(sign[i] + " " + secondOperand[i].rjust(space))
      var_dash.append('-' * (space +2))
      var_result.append(str(result[i]).rjust(space+2))


 
  if show_result == True:    
    arranged_problems = "    ".join(var_first_line) + '\n' + "    ".join(var_second_line) + '\n' + "    ".join(var_dash) + '\n' + "    ".join(var_result)
  else:
    arranged_problems = "    ".join(var_first_line) + '\n' + "    ".join(var_second_line) + '\n' + "    ".join(var_dash)


  return arranged_problems    

    


print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))