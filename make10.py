import itertools
import calc


def calc_make10(numbers:list)->list:
    if len(numbers) != 4: #4文字以上ならエラー
        return ['error']
    elif sum([(not numbers[i] in [str(x) for x in range(10)]) for i in range(4)])!=0:
        # 0未満10以上の数値が含まれていたらエラーを吐く
        return ['error']

    ops = ['+','-','*','/']
    ops_combinations = [] 
        
    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                ops_combinations.append([ op1,op2,op3 ])
        
    numbers_and_ops = []
    for op in ops_combinations:
        numbers_and_op = op
        numbers_and_op.extend(numbers)# 演算子と数値を同じ配列扱いにする['+', '+', '+', '1','2','3','4']
        numbers_and_ops.append(numbers_and_op)
        
    formula = []
    for i in range(len(ops_combinations)):
        permutations=list(itertools.permutations(sorted(numbers_and_ops[i]))) #数字と演算子のソートからの順列
        for permutation_tuple in permutations:
            permutation=list(permutation_tuple)
            ans=calc.Calc(permutation)
            if ans == 'error':
                continue
            elif abs(ans-10) <= 0.001:
                formula.append(permutation)
                
    if len(formula) == 0:
        return ['error' ]
    else:
        return formula



if __name__ == "__main__": #実質メイン関数
    print(calc_make10(['4','3','2','1']))
    # print(calc_make10(['10','2','-3','4']))
    # print(calc_make10([1,2,3,4]))
    