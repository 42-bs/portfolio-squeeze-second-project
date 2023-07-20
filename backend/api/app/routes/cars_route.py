from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from app.schemas.cars_schema import CarCreateSchema
import app.controllers.cars_controller as cars_controller

cars_router = APIRouter(prefix="/cars")

@cars_router.get("/")
def get_cars() -> JSONResponse:
    cars = cars_controller.get_cars()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "cars": cars},
    )

@cars_router.post("/")
def create_car(car: CarCreateSchema) -> JSONResponse:
    response = cars_controller.create_car(car)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": "success", "message": response},
    )

# @cars_router.get("/{model}")
# def get_car_by_model(model: str) -> JSONResponse:
#     car = cars_controller.get_car_by_model(model)
#     return JSONResponse(
#         status_code=status.HTTP_200_OK,
#         content={"status": "success", "car": car},
#     )

@cars_router.get("/maker/{maker_name}")
def get_cars_by_maker(maker_name: str) -> JSONResponse:
    cars = cars_controller.get_cars_by_maker(maker_name)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "cars": cars},
    )