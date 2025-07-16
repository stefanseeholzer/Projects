class CarsController < ApplicationController
  def index
    @cars = Car.all
    @all_cars = @cars

    @cars = @cars.where(car_model_id: params[:model]) if params[:model].present?

    filter_params_by_search if params[:text_search].present?

    filter_params_by_radios

    @cars = @cars.page(params[:page]).per(10)
  end

  def show
    @car = Car.find(params[:id])
  end

  def filter_params_by_search
    search = "%#{params[:text_search]}%"
    @cars = @cars.where("description LIKE ? OR name LIKE ?", search, search)
  end

  def filter_params_by_radios
    if params[:car_filter] == "new"
      @cars = @cars.where("created_at >= ?", 3.days.ago)
    elsif params[:car_filter] == "updated"
      @cars = @cars.where("updated_at >= ?", 3.days.ago)
      @cars = @cars.where.not("created_at >= ?", 3.days.ago)
    end
  end
end
