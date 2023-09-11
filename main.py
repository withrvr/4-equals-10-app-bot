# imports
import itertools

# declaration
numbers = [_ for _ in input("Enter Numbers: ")]
operators = ['+', '-', '*', '/']
result = int(input("Want result = "))

list_numbers = list(itertools.permutations(numbers))
list_operator = list(itertools.product(operators, repeat = len(numbers)-1))

combination_possible = len(list_operator) * len(list_numbers)
solution_equals = []

# looping
print()
for n in list_numbers:
	for o in list_operator:

		# to find the formula how it looks
		def return_formula():
			s = ""
			for i in range(len(n)-1):
				s+=(n[i]+o[i])
			s+=n[-1]
			return s

		formula = return_formula()

		try:
			sol = eval(formula)
		except:
			sol = -1
		finally:
			if sol == result:
				solution_equals.append(formula)
				print(formula)


print()
print(f"""Out of all {combination_possible} combinations possible
of numbers     {numbers}
with operators {operators}
this {len(solution_equals)} combinations gives result = {result}""")
print()

