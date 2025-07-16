Rails.application.routes.draw do
  get 'models/index'
  devise_for :admin_users, ActiveAdmin::Devise.config
  ActiveAdmin.routes(self)

  root 'cars#index'

  resources :cars, only: [:show, :index]
  resources :models, only: [:show, :index]

  resources :cart, only: %i[create destroy]

  resources :checkout, only: [:index, :create]

  resources :customers, only: [:index, :show]
  
  scope "/checkout" do
    post 'create_order', to: "checkout#create_order", as: "checkout_create_order"
    post "create", to: "checkout#create", as: "checkout_create"
    post "create_stripe", to: "checkout#create_stripe", as: "checkout_create_stripe"
    get "success", to: "checkout#success", as: "checkout_success"
    get "cancel", to: "checkout#cancel", as: "checkout_cancel"
  end

  get 'login', to: 'logins#new'
  post 'login', to: 'logins#create'
  delete 'logout', to: 'logins#destroy'
  get 'signup', to: 'customers#new'
  post 'signup', to: 'customers#create'

  get '/contact', to: 'contacts#show'
  get '/about', to: 'abouts#show'
end
