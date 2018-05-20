import input_output as io
import functions as af
import method as SIT
import zeidel


A = io.Input_matrix()
b = io.Input_matrix()
# x = SIT.simple_iter_method(A, b)
# io.print_matrix(x, "Answer: ")
# io.print_matrix(af.subtraction(af.multiplying(A, x), b), "r = A*x - b =")

print("========================")
x = zeidel.zaidel(A, b)
io.print_matrix(x, "Answer via Zaidel: ")
io.print_matrix(af.subtraction(af.multiplying(A, x), b), "r = A*x - b =")