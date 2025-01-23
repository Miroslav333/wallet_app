from fastapi import FastAPI, Body, HTTPException
from pydantic_models import Operation
from pony.orm import db_session
from database.db import Wallet
from asyncio import Lock


api = FastAPI()
wallet_lock = Lock()



@api.get('/v1/wallets/{WALLET_UUID}')
async def show_wallet_balance(WALLET_UUID: str):
    with db_session:
        wallet = Wallet.get(WALLET_UUID=WALLET_UUID)
        if wallet:
            return {"balance": wallet.amount, "owner": wallet.owner.name}
        else:
            raise HTTPException(status_code=404, detail="Wallet not found")



@api.post('/v1/wallets/{WALLET_UUID}/operation')
async def change_wallet_balance(WALLET_UUID: str, operation: Operation = Body()):
    async with wallet_lock:
        with db_session:
            wallet = Wallet.get(WALLET_UUID=WALLET_UUID)
            if wallet:
                if operation.operation == 'DEPOSIT':
                    wallet.amount += operation.amount
                elif operation.operation == 'WITHDRAW':
                    if wallet.amount - operation.amount < 0:
                        raise HTTPException(status_code=400, detail='Not enough money in the account')
                    wallet.amount -= operation.amount
                else:
                    raise HTTPException(status_code=400, detail="Invalid operation type")
            else:
                raise HTTPException(status_code=404, detail="Wallet not found")





