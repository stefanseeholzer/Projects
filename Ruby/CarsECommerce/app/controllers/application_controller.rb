class ApplicationController < ActionController::Base
  before_action :initialize_session
  helper_method :cart

  private

  def initialize_session
    session[:shopping_cart] ||= []
  end

  def cart
    Car.find(session[:shopping_cart])
  end
end
