class Solution:
	def fractionToDecimal(self, numerator: int, denominator: int) -> str:
		if numerator == 0: 
			return '0'
		if denominator == 0: 
			return False
		negative_flag = False    
		if numerator<0 and denominator>0: 
			negative_flag = True    
		elif numerator>0 and denominator<0:
			negative_flag = True       
		positive_numerator = abs(numerator)    
		positive_denominator = abs(denominator) 
		if positive_numerator % positive_denominator == 0: 
			res = positive_numerator // positive_denominator
			return str(res) if negative_flag is False else '-'+str(res)

		res_list = list()
		hashmap = dict()
		remainder = positive_numerator % positive_denominator
		quotient = positive_numerator // positive_denominator
		res_list.append(str(quotient)) 
		res_list.append('.')  
		idx = len(res_list)
		while remainder > 0:
			if remainder not in hashmap: 
				hashmap[remainder] = idx
				quotient = remainder * 10  // positive_denominator
				res_list.append(str(quotient)) 
				idx += 1
				remainder = remainder * 10  % positive_denominator

			elif remainder in hashmap:    
				insert_idx = hashmap[remainder]
				res_list.insert(insert_idx, "(")
				res_list.append(")")
				break 

		# print(res_list)    
		if negative_flag is False: 
			return ''.join(res_list) 
		elif negative_flag is True: 
			return '-' + ''.join(res_list) 