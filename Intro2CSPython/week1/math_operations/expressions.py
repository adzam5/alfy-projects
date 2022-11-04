# Basic Calculator
def calc_math_expression(num1, num2, operator):

	if operator == ':' and (num1 == 0 or num2 == 0):
		return None

	math = {
		'+': num1 + num2,
		'-': num1 - num2,
		'*': num1 * num2,
		':': num1 / num2
	}

	return math[operator]


def calc_math_expression_from_str(str_input):
	operators = ['+', '-', '*', ':']
	x = str_input.split()

	if x[1] not in operators:
		return None

	return calc_math_expression(float(x[0]), float(x[2]), x[1])


# Largest and Smallest
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
	numbers = [num1, num2, num3]
	return (max(numbers), min(numbers))


# Quadratic Equation Solver
def quadratic_equation_solver(a, b, c):

	if a == 0 or ((b**2) < (4 * a * c)):
		return (None, None)

	solution_1 = (-(b) + ((b**2) - (4 * a * c))**0.5) / (2 * a)
	solution_2 = (-(b) - ((b**2) - (4 * a * c))**0.5) / (2 * a)

	if solution_1 == solution_2:
		return (solution_1, None)

	return (solution_1, solution_2)


def quadratic_equation_solver_from_user_input(str_input):
	str_input = str_input.split()

	a = str_input[0]
	b = str_input[1]
	c = str_input[2]

	return quadratic_equation_solver(float(a), float(b), float(c))


# Temp Checker
def temp_checker(min_temp, temp_1, temp_2, temp_3):
	return True if len([x for x in [temp_1, temp_2, temp_3] if x > min_temp]) >=2 else False
