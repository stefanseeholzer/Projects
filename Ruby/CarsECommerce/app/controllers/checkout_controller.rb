class CheckoutController < ApplicationController
  def index
    @cart_items = session[:shopping_cart].map { |id, quantity| [Car.find(id), quantity] }
    @province_abbreviations = Province.pluck(:abbreviation)
    @province_taxes = Province.pluck(:abbreviation, :gst, :pst)

    load_cart_items

    @subtotal = calculate_subtotal(@cart_items)
    calculate_subtotal_taxes

    assign_user

    @total = @subtotal + @taxes[2]

    render "index"
  end

  def load_cart_items
    @cart_items = checkout_service.load_cart_items
  end

  def update_customer_address
    if session[:province]
      province = Province.find_by(abbreviation: session[:province])
      @customer.province = province
      session.delete(:province)
    end
    if session[:address]
      @customer.address = session[:address]
      session.delete(:address)
    end
    @customer.save
  end

  def set_taxes_for_guest
    @taxes = checkout_service.set_taxes_for_guest
  end

  def calculate_subtotal_taxes
    if session[:customer_id]
      @customer = Customer.find_by(id: session[:customer_id])
      update_customer_address
      @taxes = calculate_taxes(@subtotal, @customer.province.abbreviation)
    else
      set_taxes_for_guest
    end
  end

  def assign_user
    if session[:customer_id]
      @province_selected = @customer.province.abbreviation
      @address = @customer.address
    else
      guest_user_address_info
    end
  end

  def guest_user_address_info
    guest_user_province_info
    if session[:address]
      @address = session[:address]
      session.delete(:address)
    else
      @address = ""
    end
  end

  def guest_user_province_info
    if session[:province]
      @province_selected = session[:province]
      session.delete(:province)
    else
      @province_selected = "AB"
    end
  end

  def create
    session[:province] = params[:province]
    session[:address] = params[:address]

    redirect_to checkout_index_path
  end

  # Helpers
  def calculate_subtotal(cart_items)
    cart_items.sum { |car, quantity| car.price * quantity }
  end

  def calculate_taxes(subtotal, province)
    @province = Province.find_by(abbreviation: province)

    @gst = (subtotal * (@province.gst / 100)).round(2)
    @pst = (subtotal * (@province.pst / 100)).round(2)
    [@gst, @pst, (@gst + @pst).round(2)]
  end

  def create_order
    checkout_service.create_order

    delete_sessions

    redirect_to root_url
    flash[:notice] = "Checkout completed!"
  end

  # def check_for_session_user
  #   if session[:customer_id]
  #     @customer = Customer.find_by(id: session[:customer_id])
  #   else
  #     create_guest_user
  #   end
  # end

  # def create_guest_user
  #   province = Province.find_by(abbreviation: params[:province])
  #   @address =
  #     if params[:address] != ""
  #       params[:address]
  #     else
  #       "N/A"
  #     end
  #   create_guest_customer(province)
  # end

  # def create_guest_customer(province)
  #   @customer = Customer.create(
  #     address:         @address,
  #     province:,
  #     name:            "guest",
  #     email:           "a@a.a",
  #     phone_number:    0,
  #     password_digest: "asvjnvkuirnvznxhv243515gr"
  #   )
  # end

  # def create_one_order
  #   @total = params[:total]
  #   @order = Order.create(
  #     customer_id:  @customer.id,
  #     order_date:   DateTime.now,
  #     total_amount: @total,
  #     status:       "New"
  #   )
  # end

  # def add_items_to_order
  #   @cart_items.uniq.each do |car|
  #     quantity = @cart_items.count(car)
  #     single_car = Car.find_by(id: car)
  #     cars_price = single_car.price * quantity
  #     hst = params[:taxes].to_f
  #     create_order_item(car, quantity, cars_price, hst)
  #   end
  # end

  # def create_order_item(car, quantity, cars_price, hst)
  #   @order_item = OrderItem.create(
  #     order_id:  @order.id,
  #     car_id:    car,
  #     quantity:,
  #     car_price: cars_price,
  #     taxes:     cars_price * hst
  #   )
  # end

  def delete_sessions
    session.delete(:shopping_cart)
    session.delete(:address)
    session.delete(:province)
  end

  private

  def checkout_service
    CheckoutService.new(
      session[:shopping_cart],
      [
        @subtotal, session[:province], session[:customer_id],
        params[:province], params[:address], params[:total]
      ],
      session[:shopping_cart], params[:taxes]
    )
  end
end
