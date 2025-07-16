class CustomersController < ApplicationController
  def new
    @customer = Customer.new
    @provinces = Province.pluck(:abbreviation)
  end

  def create
    @customer = Customer.new(customer_params)

    assign_province
    @customer.password = params[:customer][:password]

    if @customer.save
      session[:customer_id] = @customer.id
      redirect_to root_url, notice: "Account created successfully!"
    else
      render :new
    end
  end

  def assign_province
    province_abbreviation = params[:customer][:province]
    province = Province.find_by(abbreviation: province_abbreviation)
    @customer.province = province
  end

  def customer_params
    params.require(:customer).permit(:name, :phone_number, :address, :email)
  end

  def show
    @customer = Customer.find_by(id: session[:customer_id])
    @orders = @customer.orders.all
  end
end
