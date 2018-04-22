# merge sort
#author: vysakh

def merge_sort(array, order = 'asc'):

	inversion_count = 0
	if len(array) > 1:
		middle = len(array)//2
		lefthalf = array[:middle]
		righthalf = array[middle:]
		inversion_count = merge_sort(lefthalf, order) 
		inversion_count += merge_sort(righthalf, order)
		i,l,r = 0,0,0

		lefthalf_length, righthalf_length = len(lefthalf), len(righthalf)

		while l < lefthalf_length and r < righthalf_length:
			if order == 'asc':
				if lefthalf[l] < righthalf[r]:
					array[i] = lefthalf[l]
					l += 1
				elif lefthalf[l] > righthalf[r]:
					array[i] = righthalf[r]
					r += 1
					inversion_count += inversion_count + (middle - i);
				else:
					array[i] = righthalf[r]
					l,r = l+1, r+1
			else:
				if lefthalf[l] > righthalf[r]:
					array[i] = lefthalf[l]

					l += 1
				elif lefthalf[l] < righthalf[r]:
					array[i] = righthalf[r]
					
					r += 1
				else:
					array[i] = righthalf[r]
					l,r = l+1, r+1

			
			i += 1

		while l < lefthalf_length:
			array[i] = lefthalf[l]
			l,i = l+1, i+1

		while r < righthalf_length:
			array[i] = righthalf[r]
			r,i = r+1, i+1

		return inversion_count



if __name__ == "__main__":

	num_array = list()
	num = input("Enter how many elements you want:")
	print('Enter numbers in array: ')
	for i in range(int(num)):
		n = input("num :")
		num_array.append(int(n))
	inversion_count = merge_sort(num_array,'asc')  # sorted in ascending
	#merge_sort(num_array,'desc')  # sorted in descending
	print(inversion_count)







