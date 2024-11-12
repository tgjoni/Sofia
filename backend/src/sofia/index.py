import csv

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic model to validate incoming data
class Item(BaseModel):
    item: str


@app.post("/save_csv")
async def save_csv(item: Item):
    # Append the item to CSV
    with open("saved_items.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item.item])  # Write the item as a new row

    return {"message": "Item saved successfully"}
