import cryptanalib as ca
import feathermodules

def break_columnar_transposition(ciphertexts):
   arguments=feathermodules.current_options
   results = []
   for ciphertext in ciphertexts:
      result = ca.break_columnar_transposition(ciphertext, num_answers=int(arguments['num_answers']))
      result = '\n'.join(result)
      results.append(result)
   print 'Best results of columnar transposition solve:'
   print '-'*80
   print '\n'.join(results)
   return results


feathermodules.module_list['column_trans'] = {
   'attack_function':break_columnar_transposition,
   'type':'classical',
   'keywords':['transposition'],
   'description':'A brute force attack against columnar transposition ciphers.',
   'options':{'num_answers':'3'}
}
