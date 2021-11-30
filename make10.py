import itertools
import calc


def calc_make10(numbers: list) -> list:
    if len(numbers) != 4:  # 4文字以上ならエラー
        return ["[Error] Number lenght is not 4"]
    elif sum([(not numbers[i] in [str(x) for x in range(10)]) for i in range(4)]) != 0:
        # 0未満10以上の数値が含まれていたらエラーを吐く
        return ["[Error] 0 <= numbers < 10 is ok"]

    ops = ["+", "-", "*", "/"]
    ops_combinations = []

    for op1 in ops:
        for op2 in ops:
            for op3 in ops:
                ops_combinations.append([op1, op2, op3])

    numbers_and_ops = []
    for op in ops_combinations:
        numbers_and_op = op
        numbers_and_op.extend(
            numbers
        )  # 演算子と数値を同じ配列扱いにする['+', '+', '+', '1','2','3','4']
        numbers_and_ops.append(numbers_and_op)

    formulas = []
    for i in range(len(ops_combinations)):
        permutations = list(
            itertools.permutations(sorted(numbers_and_ops[i]))
        )  # 数字と演算子のソートからの順列
        for permutation_tuple in permutations:
            permutation = list(permutation_tuple)
            ans = calc.RPN_Calc(permutation)

            if not type(ans) is int:
                continue
            elif abs(ans - 10) <= 0.001:

                formulas.append(permutation)
    if len(formulas) == 0:
        return ["[Error] value not found"]
    else:
        return [calc.to_infix(formula) for formula in formulas]


if __name__ == "__main__":  # 実質メイン関数
    print(calc_make10(["4", "3", "2", "1"]))
    
