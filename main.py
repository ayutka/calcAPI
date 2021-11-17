#
from fastapi import FastAPI
import calc
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def root(formula): #
    moji = formula.split(' ') #fomulaで空白による文字列の受け取り
    ans = calc.Calc(moji) #calc.pyのCalc(moji)を受け取る
    return {"ans":ans}
#uvicorn main:app --reload --workers 1 --host 0.0.0.0 --port 8080
# http://localhost:8080