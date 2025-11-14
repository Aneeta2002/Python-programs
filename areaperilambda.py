def main():
	print("Rectangle")
	print("................")
	l=int(input("enter the length of the rectangle:"))
	b=int(input("enter the breadth of the rectangle:"))
	area_rect=lambda l,b:l*b
	print("Area of the rectangle:",area_rect(l,b))
	peri_rect=lambda l,b:2*(l+b)
	print("Perimeter of the rectangle:",peri_rect(l,b))
	print("\nSquare")
	print("................")
	a=int(input("Enter the length of one side of a square:"))
	area_sqr=lambda a:a*a
	print("Area of square:",area_sqr(a))
	peri_sqr=lambda a:4*a
	print("Perimeter of the square:",peri_sqr(a))
if _name__== "_main_":
	main()
