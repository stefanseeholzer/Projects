class LoginsController < ApplicationController
  def new; end

  def create
    customer = Customer.find_by(email: params[:email])
    if customer&.authenticate(params[:password])
      session[:customer_id] = customer.id
      redirect_to root_url, notice: "Logged in successfully!"
    else
      flash.now[:alert] = "Invalid email or password"
      render :new
    end
  end

  def destroy
    session[:customer_id] = nil
    redirect_to root_url, notice: "Logged out successfully!"
  end
end
