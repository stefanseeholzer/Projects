class CheckoutService
  def initialize(shopping_cart, value, cart_items, params_taxes)
    @shopping_cart = shopping_cart
    @subtotal = value[0]
    @province = value[1]
    @session_customer_id = value[2]
    @params_province = value[3]
    @params_address = value[4]
    @params_total = value[5]
    @cart_items = cart_items
    @params_taxes = params_taxes
  end

  def load_cart_items
    @cart_items = {}
    @shopping_cart.each do |car_id|
      car = Car.find(car_id)
      if @cart_items.key?(car)
        @cart_items[car] += 1
      else
        @cart_items[car] = 1
      end
    end
    @cart_items
  end

  def set_taxes_for_guest
    @taxes =
      if @province
        calculate_taxes(@subtotal, @province)
      else
        calculate_taxes(@subtotal, "AB")
      end
    [@gst, @pst, (@gst + @pst).round(2)]
  end

  def calculate_taxes(subtotal, province)
    @province_found = Province.find_by(abbreviation: province)

    @gst = (subtotal * (@province_found.gst / 100)).round(2)
    @pst = (subtotal * (@province_found.pst / 100)).round(2)
  end

  def create_order
    check_for_session_user
    create_one_order
    add_items_to_order
  end

  def check_for_session_user
    if @session_customer_id
      @customer = Customer.find_by(id: @session_customer_id)
    else
      create_guest_user
    end
  end

  def create_guest_user
    province = Province.find_by(abbreviation: @params_province)
    @address =
      if @params_address != ""
        @params_address
      else
        "N/A"
      end
    create_guest_customer(province)
  end

  def create_guest_customer(province)
    @customer = Customer.create(
      address:         @address,
      province:,
      name:            "guest",
      email:           "a@a.a",
      phone_number:    0,
      password_digest: "asvjnvkuirnvznxhv243515gr"
    )
  end

  def create_one_order
    @total = @params_total
    @order = Order.create(
      customer_id:  @customer.id,
      order_date:   DateTime.now,
      total_amount: @total,
      status:       "New"
    )
  end

  def add_items_to_order
    @cart_items.uniq.each do |car|
      quantity = @cart_items.count(car)
      single_car = Car.find_by(id: car)
      cars_price = single_car.price * quantity
      hst = @params_taxes.to_f
      create_order_item(car, quantity, cars_price, hst)
    end
  end

  def create_order_item(car, quantity, cars_price, hst)
    @order_item = OrderItem.create(
      order_id:  @order.id,
      car_id:    car,
      quantity:,
      car_price: cars_price,
      taxes:     cars_price * hst
    )
  end
end
