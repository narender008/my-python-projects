from fastapi import FastAPI, HTTPException

app = FastAPI()

db = [{"first": "1"}, {"second": "2"}, {"third": "3"}, {"forth": "4"}]
# db = [1, 2, 3, 4, 5, 6, 7, 8]


@app.get("/items")
async def get_values(start: int = 0, end: int = 3):
    if start < end:
        new = db[start:end]
        return new
    else:
        raise HTTPException(404, detail="please enter correct start values.")


@app.get("/{item_id}/{user_id}")
async def get_bool(
    user_id: str, item_id: str, var: str | None = None, switch: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if var:
        item.update({"var": var})
    if switch:
        item.update({"disc": "this is the discription after switching is on"})
    return item
