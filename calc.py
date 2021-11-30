# 電卓の機能

OPERATORS = {"(": 1, ")": 1, "+": 2, "-": 2, "*": 3, "/": 3, "^": 3}

# 中置記法から後置記法へ変換
def Calc(moji):  # 関数内で入力値を後置記法に直す
    stack = []  # 演算子
    postfix = []  # 完成形

    for char in moji:
        if char not in OPERATORS:  # 演算子が入っていなかったら
            postfix.append(char)  # postfixに中置記法での数値を入れる
        else:
            if len(stack) == 0:  # 演算子を格納するstackが空の場合
                stack.append(char)  # とりあえず入れる
            else:
                if char == "(":  # カッコの処理
                    stack.append(char)  # とりあえず入れる
                elif char == ")":
                    while stack[len(stack) - 1] != "(":  # カッコ開が来るまで
                        postfix.append(stack.pop())  # 中身を取り出しpostfixへ代入
                    stack.pop()  # stackから'('を中身削除
                elif OPERATORS[char] <= OPERATORS[stack[len(stack) - 1]]:
                    # 演算子の優先度, 新しく来る記号とstackの一番上にある記号との比較
                    while len(stack) != 0:
                        if stack[len(stack) - 1] == "(":
                            break
                        postfix.append(stack.pop())
                    stack.append(char)
                else:
                    stack.append(char)  # 格納されると+*のようになる

    while len(stack) != 0:
        postfix.append(stack.pop())

    return RPN_Calc(postfix)


# 逆ポーランド記法を計算
def RPN_Calc(RPN: list):
    num_stack = []  # 最終計算結果を格納
    # RPN = moji_to_postfix(moji)
    sp = 0  # スタックポインタを底に設定
    for i in RPN:  # 数値と演算子を判別
        if (
            "!" <= i <= "'"
            or ":" <= i <= "]"
            or "_" <= i <= "~"
            or i == ","
            or i == "."
        ):
            print("その入力では計算できません。")
            break
        elif i in ["+", "-", "*", "/", "^"]:  # 文字判別　iに[]の中身が含まれているか
            try:
                num2 = num_stack.pop()  # 最後尾から取り出し
                sp -= 1
                num1 = num_stack.pop()
                sp -= 1
                if i == "+":
                    sp += 1
                    num_stack.append(num1 + num2)
                elif i == "-":
                    sp += 1
                    num_stack.append(num1 - num2)
                elif i == "*":
                    sp += 1
                    num_stack.append(num1 * num2)
                elif i == "/":
                    if num2 == 0:  # 0は除算できない
                        return "[Error] can not warizann"
                    else:
                        sp += 1
                        num_stack.append(num1 / num2)
                elif i == "^":
                    sp += 1
                    if num2 == 0:
                        num_stack.append(1)
                    else:
                        num_stack.append(num1 ** num2)
            except IndexError as e:
                return "[Error] IndexError"
        elif i in ["(", ")"]:  # カッコが来たら
            continue
        else:
            sp += 1
            num_stack.append(int(i))  # 数値スタックに数値のみを格納

    return num_stack[0]


def to_infix(RPN_formula: list):
    stack = []
    print(RPN_formula)
    for char in RPN_formula:
        if char not in OPERATORS:  # 演算子が入っていなかったら
            stack.append(char)  # ansに数値を入れる
        else:
            if len(stack) == 0:  # 演算子を格納するstackが空の場合
                stack.append(char)  # とりあえず入れる
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(f"({num1} {char} {num2})")

    return stack


if __name__ == "__main__":  # 実質メイン関数
    # moji = input().split(' ') #' 'で文字列を分割
    ans = RPN_Calc(["1", "+", "2", "+", "3", "+", "4"])
    print(ans)
