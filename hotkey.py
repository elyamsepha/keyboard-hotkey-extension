from keyboard import is_pressed


def hotkey(*args):
	string = "True if "
	for i in range(len(args)):
		if i == len(args) - 1:
			string = string + f"is_pressed('{args[i]}') == True else False"
		else:
			string = string + f"is_pressed('{args[i]}') == True and "
	return eval(string)