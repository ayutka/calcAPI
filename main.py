from fastapi import FastAPI
import calc

app = FastAPI()


@app.get("/")
async def root(formula):
    moji = formula.split(' ') #' 'で文字列を分割
    ans = calc.Calc(moji)
    return {"ans":ans}
#uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8080
# http://localhost:8080