class CartController < ApplicationController
  def create
    add_to_cart
  end

  def add_to_cart
    logger.debug("Adding #{params[:car_id]} to cart.")
    id = params[:car_id].to_i
    quantity = params[:quantity].to_i
    quantity.times do
      session[:shopping_cart] << id
    end

    create_flash(id, quantity)
  end

  def create_flash(id, quantity)
    car = Car.find(id)
    flash[:notice] = "✚ #{quantity} #{car.name.pluralize(quantity)} added to cart."
    redirect_to root_path
  end

  def destroy
    remove_from_cart
  end

  def remove_from_cart
    logger.debug("Removing #{params[:car_id]} to cart.")
    id = params[:car_id].to_i
    quantity = params[:quantity].to_i

    remove_items(id, quantity)

    destroy_flash(id, quantity)
  end

  def remove_items(id, quantity)
    quantity.times do
      index = session[:shopping_cart].find_index(id)
      session[:shopping_cart].delete_at(index)
    end
  end

  def destroy_flash(id, quantity)
    car = Car.find(id)
    flash[:notice] = "- #{quantity} #{car.name.pluralize(quantity)} removed from cart"
    redirect_to root_path
  end
end
