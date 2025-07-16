class ModelsController < ApplicationController
  def index
    @models = CarModel.all
    @models = @models.page(params[:page]).per(15)
  end

  def show
    @model = CarModel.find(params[:id])
    @cars = @model.cars
    @cars = @cars.page(params[:page]).per(10)
  end
end
